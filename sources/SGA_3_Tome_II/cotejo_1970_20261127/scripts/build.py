"""Build both Portuguese masters and retain portable, sanitized TeX logs.

Run from any directory: python scripts/build.py
Requires Python 3 and a local TeX Live installation with the packages named in
sources/build_support.tex. No network connection is used. A private cache can
bootstrap a missing pdfLaTeX format from already installed TeX resources.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


def command(args, *, env=None, cwd=None):
    return subprocess.run(args, env=env, cwd=cwd, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def kpse(name, *, env=None, variable=False):
    args = ["kpsewhich", "--progname=pdflatex"]
    args.append(("-var-value=" if variable else "") + name)
    result = command(args, env=env)
    return result.stdout.strip() if result.returncode == 0 else ""


def tex_environment(cache: Path):
    env = os.environ.copy()
    if kpse("pdflatex.fmt", env=env) and kpse("amsmath.sty", env=env):
        return env, "Installed pdfLaTeX format and package database."
    roots = []
    for name in ("TEXMFDEBIAN", "TEXMFDIST", "TEXMFMAIN"):
        value = kpse(name, variable=True)
        if value and Path(value).is_dir() and value not in roots:
            roots.append(value)
    if not roots:
        raise RuntimeError("TeX resource directories could not be located.")
    local = cache / "texmf"
    config = local / "tex/generic/config"
    config.mkdir(parents=True, exist_ok=True)
    env["TEXMF"] = "{" + ",".join([str(local)] + roots) + "}"
    env["TEXMFDBS"] = ""
    languages = "english hyphen.tex\n=usenglish\n=american\n"
    portuguese = kpse("loadhyph-pt.tex", env=env)
    if portuguese:
        languages += "portuguese loadhyph-pt.tex\n=brazilian\n=brazil\n"
    (config / "language.dat").write_text(languages, encoding="utf-8")
    formats = cache / "formats"
    formats.mkdir(exist_ok=True)
    env["TEXFORMATS"] = str(formats) + os.pathsep
    if not (formats / "pdflatex.fmt").is_file():
        result = command(["pdftex", "-ini", "-etex", "-interaction=nonstopmode",
                          "-halt-on-error", "-jobname=pdflatex",
                          "-progname=pdflatex", "pdflatex.ini"],
                         cwd=formats, env=env)
        (cache / "format-build.txt").write_text(result.stdout, encoding="utf-8")
        if result.returncode:
            raise RuntimeError("Local pdfLaTeX format bootstrap failed. "
                               "Inspect the private format-build log.")
    maps = cache / "maps"
    maps.mkdir(exist_ok=True)
    content = []
    for name in ("cm.map", "cmextra.map", "symbols.map", "euler.map",
                 "latxfont.map", "rsfs.map", "lm.map"):
        path = kpse(name, env=env)
        if path:
            content.append(Path(path).read_text(encoding="utf-8"))
    (maps / "pdftex.map").write_text("\n".join(content), encoding="utf-8")
    env["TEXFONTMAPS"] = str(maps) + os.pathsep
    return env, ("Local pdfLaTeX format built from installed resources; "
                 + ("Portuguese patterns loaded." if portuguese else
                    "Portuguese patterns unavailable: no Portuguese word hyphenation."))


def sanitize(text: str, source: Path, build: Path, cache: Path):
    for prefix, replacement in ((str(source), "sources"),
                                (str(build), "build"),
                                (str(cache), "tex-cache")):
        text = text.replace(prefix, replacement)
    # Installed packages and fonts are identified by basename, not local path.
    text = re.sub(r"(?<![A-Za-z0-9])/(?:[^\s()<>\[\]{}]+/)+([^\s()<>\[\]{}]+)",
                  r"<tex-resource>/\1", text)
    text = re.sub(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", "<address omitted>", text)
    return text


def aux_digest(directory: Path, master: str):
    digest = hashlib.sha256()
    for suffix in (".aux", ".toc", ".out"):
        path = directory / (master + suffix)
        if path.exists():
            digest.update(path.read_bytes())
    return digest.hexdigest()


def source_digest(source: Path):
    digest = hashlib.sha256()
    for path in sorted(source.rglob("*.tex")):
        digest.update(path.relative_to(source).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def build_one(master: str, source: Path, output: Path, cache: Path, env):
    build = cache / master
    build.mkdir(parents=True, exist_ok=True)

    def source_link(path, target):
        # A cache reused after an isolated baseline must point at this tree.
        if target.is_symlink():
            if target.resolve() != path.resolve():
                target.unlink()
            else:
                return
        elif target.exists():
            raise RuntimeError("Unmanaged cache entry: " + target.name
                               + ". Choose a clean compilation cache.")
        target.symlink_to(path, target_is_directory=path.is_dir())

    for path in source.iterdir():
        target = build / path.name
        source_link(path, target)
    # Compatibility with the received body fragments' units/ prefix.
    if not (source / "units").exists():
        source_link(source, build / "units")
    master_path = source / (master + ".tex")
    content = master_path.read_text(encoding="utf-8")
    standalone = (r"\documentclass" in content or
                  re.search(r"\\input\s*\{build_support(?:\.tex)?\}", content))
    if standalone:
        entry = master + ".tex"
    else:
        entry = "assembly_" + master + ".tex"
        wrapper = ("\\input{build_support}\n\\begin{document}\n"
                   "\\input{" + master + "}\n\\mainmatter\n"
                   "\\input{08_expose_viii/body}\n"
                   "\\input{09_expose_ix/body}\n"
                   "\\input{99_notation_index/body}\n\\end{document}\n")
        (build / entry).write_text(wrapper, encoding="utf-8")
    previous = None
    settled = False
    for run in range(1, 7):
        result = command(["pdflatex", "-interaction=nonstopmode",
                          "-halt-on-error", "-file-line-error",
                          "-jobname=" + master, entry], env=env, cwd=build)
        console = sanitize(result.stdout, source, build, cache)
        (output / (master + f".pass-{run}.txt")).write_text(console, encoding="utf-8")
        if result.returncode:
            raise RuntimeError(master + " failed in pass " + str(run) +
                               ". Inspect its sanitized pass log.")
        current = aux_digest(build, master)
        if current == previous:
            settled = True
            break
        previous = current
    raw_log = (build / (master + ".log")).read_text(encoding="utf-8", errors="replace")
    clean_log = sanitize(raw_log, source, build, cache)
    (output / (master + ".log")).write_text(clean_log, encoding="utf-8")
    shutil.copy2(build / (master + ".pdf"), output / (master + ".pdf"))
    overflows = [float(value) for value in re.findall(
        r"Overfull \\[hv]box \(([\d.]+)pt too (?:wide|high)\)", raw_log)]
    summary = {"master": master, "passes": run, "references_settled": settled,
               "overfull_count": len(overflows),
               "overfull_over_2pt": sum(value > 2 for value in overflows),
               "overfull_over_10pt": sum(value > 10 for value in overflows),
               "maximum_overfull_pt": max(overflows, default=0),
               "undefined_reference_warnings": len(re.findall(
                   r"LaTeX Warning: Reference .*? undefined", raw_log)),
               "missing_character_warnings": raw_log.count("Missing character:"),
               "destination_warnings": raw_log.count("pdfTeX warning (dest):"),
               "wrapper_used": not bool(standalone)}
    if not settled:
        raise RuntimeError(master + " auxiliary files did not settle after six passes.")
    return summary


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, default=root / "sources")
    parser.add_argument("--output", type=Path, default=root / "pdf")
    parser.add_argument("--cache", type=Path)
    parser.add_argument("--masters", nargs="+", default=["ptbr_current", "ptbr_original"])
    args = parser.parse_args()
    source, output = args.sources.resolve(), args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    cache = args.cache.resolve() if args.cache else Path(tempfile.mkdtemp(prefix="sga3-tex-"))
    cache.mkdir(parents=True, exist_ok=True)
    for executable in ("kpsewhich", "pdftex", "pdflatex"):
        if not shutil.which(executable):
            raise SystemExit("Required executable missing: " + executable)
    env, setup = tex_environment(cache)
    before = source_digest(source)
    summaries = [build_one(name, source, output, cache, env) for name in args.masters]
    if source_digest(source) != before:
        raise SystemExit("Sources changed during compilation; rerun the build.")
    report = {"setup": setup, "source_tree_sha256": before, "builds": summaries}
    (output / "BUILD_SUMMARY.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
