"""Replay the correction history entirely in memory, leaving sources untouched.

Usage: python scripts/replay_corrections.py --write-report
Without --write-report, only a short JSON result is printed. The original
source directory or original attached ZIP must be available for the replay.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import zipfile

import package as archive_support


def digest(data):
    return hashlib.sha256(data).hexdigest()


def original_sources(directory, archive):
    prefix = "SGA3_PTBR_sources/"
    if archive:
        with zipfile.ZipFile(archive) as source:
            rows = list(csv.DictReader(io.StringIO(source.read("MANIFEST.tsv").decode("utf-8")), delimiter="\t"))
            files = {}
            for row in rows:
                name = row["path"]
                if not name.startswith(prefix):
                    continue
                relative = PurePosixPath(name[len(prefix):])
                if relative.is_absolute() or ".." in relative.parts:
                    raise ValueError("Unsafe source entry in original attachment.")
                data = source.read(name)
                if digest(data) != row["sha256"] or len(data) != int(row["bytes"]):
                    raise ValueError("Original source manifest mismatch: " + name)
                files["sources/" + relative.as_posix()] = data
            return files
    if not directory.is_dir():
        raise ValueError("Original sources unavailable; use --original-sources or --original-zip.")
    files = {"sources/" + path.relative_to(directory).as_posix(): path.read_bytes()
             for path in sorted(directory.rglob("*.tex"))}
    manifest = directory.parent / "MANIFEST.tsv"
    if manifest.exists():
        for row in archive_support.read_manifest(manifest):
            if row["path"].startswith(prefix):
                key = "sources/" + row["path"][len(prefix):]
                data = files.get(key)
                if data is None or digest(data) != row["sha256"] or len(data) != int(row["bytes"]):
                    raise ValueError("Original source manifest mismatch: " + key)
    return files


def current_sources(root):
    directory = root / "sources"
    return {"sources/" + path.relative_to(directory).as_posix(): path.read_bytes()
            for path in sorted(directory.rglob("*.tex"))}


def rights_block(data):
    start = b"\\SGACopyrightPage"
    end = b"% SGA-SEG END T2-FM-000002"
    if start not in data or end not in data:
        return None
    return data[data.index(start):data.index(end)]


def replay(root, originals):
    audit_path = root / "CORRECTIONS.tsv"
    audit = audit_path.read_bytes()
    rows = list(csv.DictReader(io.StringIO(audit.decode("utf-8")), delimiter="\t"))
    actual = current_sources(root)
    state = {name: data.decode("utf-8") for name, data in originals.items()}
    failures, line_failures, repeated = [], [], []
    touched = Counter()
    for number, row in enumerate(rows, 1):
        name = row["file"]
        relative = PurePosixPath(name)
        if relative.is_absolute() or ".." in relative.parts or not name.startswith("sources/"):
            failures.append({"row": number, "file": name, "error": "unexpected non-source or unsafe path"})
            continue
        text = state.setdefault(name, "")
        old, new = row["old"], row["new"]
        if old:
            occurrences = text.count(old)
            if not occurrences:
                failures.append({"row": number, "file": name, "printed_page": row["printed_page"],
                                 "error": "old text absent from replay state"})
                continue
            line = text[:text.index(old)].count("\n") + 1
            if occurrences > 1:
                repeated.append({"row": number, "file": name, "occurrences": occurrences})
            # audit.change requires old.count == count, so every occurrence is replaced.
            state[name] = text.replace(old, new)
        else:
            line = text.count("\n") + 1
            state[name] = text + new
        if row["line"] != str(line):
            line_failures.append({"row": number, "file": name, "recorded_line": row["line"], "replayed_line": line})
        touched[name] += 1
    file_results, differences = [], []
    for name in sorted(set(state) | set(actual)):
        expected = state[name].encode("utf-8") if name in state else None
        present = actual.get(name)
        same = expected is not None and present is not None and expected == present
        item = {"file": name, "correction_rows": touched[name],
                "original_sha256": digest(originals[name]) if name in originals else None,
                "replayed_sha256": digest(expected) if expected is not None else None,
                "current_sha256": digest(present) if present is not None else None,
                "replayed_bytes": len(expected) if expected is not None else None,
                "current_bytes": len(present) if present is not None else None,
                "identical": same}
        file_results.append(item)
        if not same:
            differences.append(name)
    rights = []
    for master in ("ptbr_current", "ptbr_original"):
        name = "sources/" + master + ".tex"
        original = rights_block(originals.get(name, b""))
        present = rights_block(actual.get(name, b""))
        rights.append({"master": master,
                       "original_block_sha256": digest(original) if original is not None else None,
                       "current_block_sha256": digest(present) if present is not None else None,
                       "original_block_bytes": len(original) if original is not None else None,
                       "current_block_bytes": len(present) if present is not None else None,
                       "byte_identical": original is not None and original == present})
    stable = audit == audit_path.read_bytes() and actual == current_sources(root)
    return {
        "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "method": "Sequential old/new substitutions in memory. All occurrences are replaced, matching audit.change; an empty old value appends new. Reversals are replayed in their recorded order.",
        "scope": "Technical history and rights-block integrity only; no scan reading or textual judgment.",
        "audit_sha256": digest(audit), "correction_rows": len(rows),
        "source_snapshot_stable": stable, "source_file_count": len(actual),
        "replay_errors": failures, "recorded_line_mismatches": line_failures,
        "multiple_occurrence_operations": repeated, "file_mismatches": differences,
        "files": file_results, "rights_notices": rights,
        "passed": stable and not failures and not line_failures and not differences
                  and all(item["byte_identical"] for item in rights),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--original-sources", type=Path)
    parser.add_argument("--original-zip", type=Path)
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    original = args.original_sources.resolve() if args.original_sources else root.parent / "inputs/SGA3_PTBR_sources"
    originals = original_sources(original, args.original_zip)
    result = replay(root, originals)
    if args.write_report:
        destination = root / "records/HISTORY_REPLAY.json"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = {key: result[key] for key in ("passed", "correction_rows", "source_snapshot_stable", "source_file_count",
                                          "replay_errors", "recorded_line_mismatches", "multiple_occurrence_operations",
                                          "file_mismatches", "rights_notices")}
    summary["report"] = "records/HISTORY_REPLAY.json" if args.write_report else None
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
