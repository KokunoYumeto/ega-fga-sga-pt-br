"""Package the current edition, excluding supplied material and private work.

Usage:
    python scripts/package.py --checkpoint 01
    python scripts/package.py --final

The caller controls the 45-minute checkpoint schedule and durable uploads.
This program never schedules a checkpoint, uploads a file, or overwrites a ZIP.
Use --dry-run to inspect an inventory without writing any file.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import tempfile
import zipfile


LIMIT_BYTES = 500_000_000
ATTACHMENT = "SGA3_PTBR_VIII_IX_1970.zip"
SOURCE_PREFIX = "SGA3_PTBR_sources/"
TEXT_SUFFIXES = {
    ".tex", ".sty", ".cls", ".bib", ".md", ".txt", ".log", ".json",
    ".tsv", ".csv", ".py", ".sh", ".yaml", ".yml", ".toml", ".ini",
    ".cfg", ".html", ".css", ".js", ".svg",
}
EXCLUDED_DIRECTORIES = {
    "__pycache__", ".git", ".cache", ".pytest_cache", ".mypy_cache",
    "cache", "caches", "tmp", "temp", "build", "build_environment",
    "build_baseline", "inputs", "input", "upload", "uploads", "scan",
    "scans", "crops", "crop", "renders", "rendered", "render",
    "extractions", "extraction", "extracts", "checkpoints",
}
EXCLUDED_SUFFIXES = {
    ".zip", ".tar", ".gz", ".bz2", ".xz", ".7z", ".rar", ".pyc",
    ".aux", ".toc", ".out", ".fls", ".fdb_latexmk", ".synctex",
    ".fmt", ".pfb", ".tfm", ".map", ".png", ".jpg", ".jpeg",
    ".webp", ".tif", ".tiff", ".bmp", ".gif",
}
FINAL_REQUIRED = {
    "CORRECTIONS.tsv", "CHECK_RECORD.md", "CHECK_EVENTS.tsv", "PDF_CHECK.md",
    "README.md", "progress.log", "pdf/ptbr_current.pdf", "pdf/ptbr_original.pdf",
}
RESERVED = {"records/PACKAGE_INVENTORY.json", "records/CHECKPOINT_RESTORE.md"}
EMAIL_RE = re.compile(r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@"
                      r"[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?"
                      r"\.[A-Za-z]{2,}")
UNIX_ROOT_NAMES = ("workspace", "home", "tmp", "mnt", "usr", "opt",
                   "var", "etc", "root", "Users", "private")
UNIX_PATH_RE = re.compile(
    r"(?<![A-Za-z0-9_:])/" + "(?:" + "|".join(UNIX_ROOT_NAMES) + ")/"
    + r"[^\s()<>\[\]{}\"']+")
WINDOWS_PATH_RE = re.compile(
    r"(?<![A-Za-z0-9_])[A-Za-z]:[\\/]"
    r"(?:Users|Windows|Program Files|ProgramData|Temp|Documents)[\\/]"
    r"[^\s()<>\[\]{}\"']+")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_manifest(path: Path):
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    if not rows or set(rows[0]) != {"path", "bytes", "sha256"}:
        raise ValueError("Unexpected attachment manifest columns.")
    for row in rows:
        name = PurePosixPath(row["path"])
        if name.is_absolute() or ".." in name.parts:
            raise ValueError("Unsafe relative entry in attachment manifest.")
        if not re.fullmatch(r"[0-9a-f]{64}", row["sha256"]):
            raise ValueError("Invalid SHA-256 in attachment manifest.")
    return rows


def exclusion(relative: PurePosixPath):
    if any(part.lower() in EXCLUDED_DIRECTORIES for part in relative.parts[:-1]):
        return "private input, cache, or inspection directory"
    if relative.suffix.lower() in EXCLUDED_SUFFIXES:
        return "archive, compiler intermediate, font resource, or inspection image"
    if relative.name.startswith("."):
        return "private metadata"
    if relative.as_posix() in RESERVED:
        return "superseded package-specific inventory"
    if relative.suffix.lower() == ".pdf" and relative.as_posix() not in {
        "pdf/ptbr_current.pdf", "pdf/ptbr_original.pdf"
    }:
        return "PDF other than the two edition masters"
    return None


def private_matches(text: str, prefixes):
    matches = []
    for prefix in prefixes:
        if prefix and prefix in text:
            matches.append(prefix)
    matches += [match.group() for expression in
                (EMAIL_RE, UNIX_PATH_RE, WINDOWS_PATH_RE)
                for match in expression.finditer(text)]
    return sorted(set(matches), key=len, reverse=True)


def safe_bytes(data: bytes, relative: PurePosixPath, prefixes):
    if relative.suffix.lower() not in TEXT_SUFFIXES:
        return data, 0
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("Non-UTF-8 text file: " + relative.as_posix()) from exc
    matches = private_matches(text, prefixes)
    if not matches:
        return data, 0
    # Logs may be sanitized in the archive without changing the working file.
    # Never silently rewrite sources, correction evidence, reports, or programs.
    if relative.suffix.lower() not in {".log", ".txt"}:
        raise ValueError("Local path or email found in " + relative.as_posix()
                         + "; remove it explicitly before packaging.")
    count = 0
    for match in matches:
        count += text.count(match)
        replacement = "<address omitted>" if EMAIL_RE.fullmatch(match) else "<local-path>"
        text = text.replace(match, replacement)
    if private_matches(text, prefixes):
        raise ValueError("A log could not be fully sanitized: " + relative.as_posix())
    return text.encode("utf-8"), count


def restore_note(omitted, mode):
    if mode == "final":
        return ("# Uso da entrega final\n\n"
                "Este pacote contém toda a árvore portuguesa corrigida e os dois PDFs.\n"
                "Extraia-o e execute python scripts/build.py para recompilar;\n"
                "não é necessário recuperar fontes do anexo original.\n\n"
                "O anexo original só é necessário para reproduzir o cotejo ou\n"
                "a auditoria histórica. Para esses usos, confira seu MANIFEST.tsv\n"
                "e mantenha os materiais de consulta fora dos entregáveis.\n\n"
                "O pacote não inclui anexos inalterados, escaneamentos, imagens\n"
                "de inspeção, extrações ou ZIPs de checkpoints anteriores.\n"
                "Consulte README.md, PDF_CHECK.md e records/PACKAGE_INVENTORY.json.\n").encode("utf-8")
    lines = ["# Restauração do estado de trabalho", "",
             "Este pacote não contém cópias inalteradas dos arquivos anexados,",
             "o escaneamento, suas imagens ou extrações, nem ZIPs anteriores.", "",
             "1. Disponibilize novamente o anexo `" + ATTACHMENT + "`.",
             "2. Confira o `MANIFEST.tsv` desse anexo.",
             "3. Para continuar um checkpoint, extraia a árvore",
             "   `SGA3_PTBR_sources/` do anexo como `sources/` no diretório",
             "   de trabalho. Extraia também os materiais de consulta do anexo",
             "   em um diretório separado, fora dos entregáveis.",
             "4. Sobreponha o conteúdo deste pacote ao diretório de trabalho.",
             "   Os arquivos corrigidos e os registros do checkpoint prevalecem.",
             "5. Leia `progress.log`, `CHECK_RECORD.md`, `CORRECTIONS.tsv` e",
             "   `records/PACKAGE_INVENTORY.json` antes de retomar o cotejo.", ""]
    if mode == "final":
        lines += ["A entrega final contém todos os arquivos esperados da árvore",
                  "portuguesa, modificados e prontos para a compilação.", ""]
    if omitted:
        lines += ["## Fontes ainda inalteradas, a recuperar do anexo", "",
                  "| Destino no trabalho | Entrada no anexo |",
                  "|---|---|"]
        for item in omitted:
            if item["file"].startswith("sources/"):
                lines.append("| `" + item["file"] + "` | `"
                             + item["attachment_entries"][0] + "` |")
        lines.append("")
    return "\n".join(lines).encode("utf-8")


def inventory(root: Path, manifest_rows, mode: str, checkpoint):
    hashes = {}
    for row in manifest_rows:
        hashes.setdefault(row["sha256"], []).append(row["path"])
    expected = {"sources/" + row["path"][len(SOURCE_PREFIX):]: row["sha256"]
                for row in manifest_rows if row["path"].startswith(SOURCE_PREFIX)}
    prefixes = {str(root), str(root.parent), str(Path.home()), tempfile.gettempdir()}
    payloads, included, omitted, excluded = {}, [], [], []
    for path in sorted(root.rglob("*")):
        if path.is_dir():
            continue
        relative = PurePosixPath(path.relative_to(root).as_posix())
        reason = exclusion(relative)
        if reason:
            excluded.append({"file": relative.as_posix(), "reason": reason})
            continue
        if path.is_symlink():
            raise ValueError("Symlink is not a self-contained deliverable: " + relative.as_posix())
        data = path.read_bytes()
        original_hash = sha256(data)
        if original_hash in hashes:
            omitted.append({"file": relative.as_posix(), "sha256": original_hash,
                            "attachment_entries": hashes[original_hash]})
            continue
        data, count = safe_bytes(data, relative, prefixes)
        packaged_hash = sha256(data)
        if packaged_hash in hashes:
            omitted.append({"file": relative.as_posix(), "sha256": packaged_hash,
                            "attachment_entries": hashes[packaged_hash]})
            continue
        payloads[relative.as_posix()] = data
        included.append({"file": relative.as_posix(), "bytes": len(data),
                         "sha256": packaged_hash, "sanitizations": count})
    missing = sorted(set(expected) - set(payloads))
    if mode == "final":
        absent = sorted((set(expected) | FINAL_REQUIRED) - set(payloads))
        if absent:
            raise ValueError("Final package lacks required, corrected files: " + ", ".join(absent))
    report = {
        "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "mode": mode, "checkpoint": checkpoint,
        "base_attachment": ATTACHMENT,
        "expected_source_count": len(expected),
        "expected_sources_omitted_from_this_package": missing,
        "included": included,
        "unchanged_attachment_files_omitted": omitted,
        "excluded_private_files": excluded,
        "restoration": ("Self-contained final sources; attachment not required to build." if mode == "final" else "Restore base sources from the attachment, then overlay this package."),
    }
    payloads["records/CHECKPOINT_RESTORE.md"] = restore_note(omitted, mode)
    payloads["records/PACKAGE_INVENTORY.json"] = (
        json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    return payloads, report


def main():
    default_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--checkpoint", type=int, metavar="NN")
    mode.add_argument("--final", action="store_true")
    parser.add_argument("--root", type=Path, default=default_root)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--output-directory", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.checkpoint is not None and not 1 <= args.checkpoint <= 99:
        parser.error("checkpoint NN must be from 01 through 99")
    root = args.root.resolve()
    manifest = args.manifest.resolve() if args.manifest else root.parent / "inputs/MANIFEST.tsv"
    output_dir = args.output_directory.resolve() if args.output_directory else root.parent / "deliverables"
    if output_dir == root or root in output_dir.parents:
        parser.error("the output directory must be outside the work tree")
    label = "final" if args.final else "checkpoint"
    filename = ("SGA3_PTBR_VIII_IX_1970.zip" if args.final else
                f"SGA3_PTBR_VIII_IX_1970_checkpoint_{args.checkpoint:02d}.zip")
    target = output_dir / filename
    if target.exists():
        raise SystemExit("Refusing to overwrite existing archive: " + filename)
    payloads, report = inventory(root, read_manifest(manifest), label, args.checkpoint)
    summary = {"file": filename, "dry_run": args.dry_run,
               "included_file_count": len(payloads),
               "unchanged_files_omitted": len(report["unchanged_attachment_files_omitted"]),
               "private_files_excluded": len(report["excluded_private_files"]),
               "sanitized_log_files": sum(item["sanitizations"] > 0 for item in report["included"]),
               "uncompressed_bytes": sum(map(len, payloads.values()))}
    if args.dry_run:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return
    output_dir.mkdir(parents=True, exist_ok=True)
    # Validate a private temporary file before exposing the checkpoint name.
    # Linking then removing the temporary name never replaces an earlier ZIP.
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=".sga3-package-", suffix=".partial", dir=output_dir)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED,
                                 compresslevel=9) as archive:
                for name, data in sorted(payloads.items()):
                    archive.writestr(name, data)
            stream.flush()
            os.fsync(stream.fileno())
        size = temporary.stat().st_size
        if size >= LIMIT_BYTES:
            raise ValueError("Archive reaches the 500 MB limit.")
        with zipfile.ZipFile(temporary) as archive:
            if archive.testzip() is not None:
                raise ValueError("Archive CRC verification failed.")
            if set(archive.namelist()) != set(payloads):
                raise ValueError("Archive entry inventory mismatch.")
        archive_hash = sha256(temporary.read_bytes())
        os.link(temporary, target)
    finally:
        temporary.unlink(missing_ok=True)
    summary.update({"bytes": size, "sha256": archive_hash})
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
