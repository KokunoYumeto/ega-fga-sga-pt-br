"""Mechanical validation of the edition and its audit deliverables.

Run `python scripts/validate.py` for final validation, or add `--progress` for an
in-progress inventory. No source or correction row is changed. The resulting
technical report does not certify visual collation or mathematical truth.
"""
from __future__ import annotations

import argparse
import ast
from collections import defaultdict
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import unicodedata
import warnings

import build as build_support
import package as archive_support


CORRECTION_KINDS = {
    "re-edition removed", "1970 restored", "reading", "translation",
    "structure", "typesetting",
}
EVENT_TYPES = {
    "targeted proof check", "independent re-proof",
    "computation or formal certificate", "used and rechecked in this run",
    "carried as background without fault found", "refuted",
}


def uncomment(line):
    for index, character in enumerate(line):
        if character == "%" and (len(line[:index]) - len(line[:index].rstrip("\\"))) % 2 == 0:
            return line[:index]
    return line


def collect_labels(base):
    targets, links, macros = defaultdict(list), defaultdict(list), defaultdict(list)
    for path in sorted(base.rglob("*.tex")):
        for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = uncomment(raw)
            location = {"file": path.relative_to(base).as_posix(), "line": number}
            for name in re.findall(r"\\(?:SGARefTarget|SGAInlineRefTarget|label)\s*\{([^{}]+)\}", line):
                if "#" not in name:
                    targets[name].append(location)
            for name in re.findall(r"\\(?:SGARefLink|ref|pageref|eqref)\s*\{([^{}]+)\}", line):
                if "#" not in name:
                    links[name].append(location)
            for name in re.findall(r"\\(?:newcommand|renewcommand|providecommand)\*?\s*\{?\\([A-Za-z@]+)", line):
                macros[name].append(location)
            for name in re.findall(r"\\(?:gdef|edef|def)\s*\\([A-Za-z@]+)", line):
                macros[name].append(location)
    return dict(targets), dict(links), dict(macros)


def collect_numbered_headings(base):
    """Extract visible numbered headings from the current TeX sources only.

    This checks event coverage of the edited sources, not the original scan.
    Invisible retained targets are deliberately not treated as statements.
    """
    headings = defaultdict(list)
    pattern = re.compile(r"\\textbf\{([^{}]*?(\d+(?:\.\d+)+(?:\s*bis)?)[^{}]*)\}")
    for directory, expose in (("08_expose_viii", "VIII"), ("09_expose_ix", "IX")):
        for path in sorted((base / directory).rglob("*.tex")):
            text = "\n".join(uncomment(line) for line in path.read_text(encoding="utf-8").splitlines())
            for match in pattern.finditer(text):
                identifier = expose + "." + re.sub(r"\s+", "", match.group(2))
                headings[identifier].append({
                    "file": path.relative_to(base).as_posix(),
                    "line": text[:match.start()].count("\n") + 1,
                    "heading": match.group(1),
                })
    return dict(headings)


def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def tex_structure(text):
    text = "\n".join(uncomment(line) for line in text.splitlines())
    issues, depth, slashes, line_number = [], 0, 0, 1
    for character in text:
        if character in "{}" and slashes % 2 == 0:
            depth += 1 if character == "{" else -1
            if depth < 0:
                issues.append({"line": line_number, "issue": "closing brace without opening brace"})
        slashes = slashes + 1 if character == "\\" else 0
        line_number += character == "\n"
    if depth:
        issues.append({"issue": "nonzero brace balance", "balance": depth})
    stack = []
    for match in re.finditer(r"\\(begin|end)\{([^{}]+)\}", text):
        action, environment = match.groups()
        if action == "begin":
            stack.append(environment)
        elif not stack or stack.pop() != environment:
            issues.append({"line": text[:match.start()].count("\n") + 1,
                           "issue": "mismatched explicit environment", "environment": environment})
    if stack:
        issues.append({"issue": "unclosed explicit environments", "environments": stack})
    return issues


def command(arguments):
    result = subprocess.run(arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValueError("External verification command failed: " + arguments[0])
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--progress", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    report = {"created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
              "mode": "progress" if args.progress else "final", "errors": [],
              "warnings": [], "pending": [], "checks": {},
              "limits": "Mechanical checks only; no certification of scan collation, visual inspection, or mathematical truth."}
    checks = report["checks"]

    def finding(category, check, detail):
        report[category].append({"check": check, "detail": detail})

    def incomplete(check, detail):
        finding("pending" if args.progress else "errors", check, detail)

    required = sorted(archive_support.FINAL_REQUIRED | {"sources/build_support.tex", "scripts/build.py", "scripts/package.py"})
    missing = [name for name in required if not (root / name).is_file() or not (root / name).stat().st_size]
    checks["mandatory_outputs"] = {"required": required, "missing_or_empty": missing}
    if missing:
        incomplete("mandatory_outputs", ", ".join(missing))

    candidates = []
    privacy_issues, control_issues, syntax_issues, tex_issues = [], [], [], []
    prefixes = {str(root), str(root.parent), str(Path.home()), archive_support.tempfile.gettempdir()}
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if archive_support.exclusion(relative) or path.suffix not in archive_support.TEXT_SUFFIXES:
            continue
        candidates.append(relative.as_posix())
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            finding("errors", "text_encoding", relative.as_posix())
            continue
        private = archive_support.private_matches(text, prefixes)
        if private:
            privacy_issues.append({"file": relative.as_posix(), "match_count": len(private)})
        for index, value in enumerate(raw):
            if value < 32 and value not in (9, 10, 13):
                control_issues.append({"file": relative.as_posix(), "line": raw[:index].count(b"\n") + 1, "byte": value})
        if path.suffix == ".tex":
            for issue in tex_structure(text):
                tex_issues.append({"file": relative.as_posix(), **issue})
            for number, line in enumerate(raw.split(b"\n"), 1):
                if b"\t" in line.lstrip(b" \t") or b"\r" in line.rstrip(b"\r"):
                    finding("warnings", "tex_whitespace", relative.as_posix() + ":" + str(number))
        if path.suffix == ".py":
            try:
                with warnings.catch_warnings(record=True) as observed:
                    warnings.simplefilter("always", SyntaxWarning)
                    tree = ast.parse(text, filename=relative.as_posix())
                for warning in observed:
                    syntax_issues.append({"file": relative.as_posix(), "line": warning.lineno,
                                          "warning": str(warning.message)})
                for node in ast.walk(tree):
                    if isinstance(node, ast.Constant) and isinstance(node.value, str):
                        bad = sorted({ord(char) for char in node.value if ord(char) < 32 and ord(char) not in (9, 10, 13)})
                        if bad:
                            finding("warnings", "python_string_controls", relative.as_posix() + ":" + str(node.lineno) + " bytes=" + str(bad))
            except SyntaxError as exc:
                finding("errors", "python_syntax", relative.as_posix() + ":" + str(exc.lineno) + " " + exc.msg)
    checks["text_integrity"] = {"files_checked": len(candidates), "privacy_issues": privacy_issues,
                                "control_byte_issues": control_issues, "python_escape_warnings": syntax_issues,
                                "tex_structure_issues": tex_issues}
    if privacy_issues:
        finding("errors", "privacy", "Local paths or email addresses found; see file-only inventory.")
    if control_issues:
        finding("errors", "control_bytes", "Forbidden control bytes found; see file-only inventory.")
    if tex_issues:
        finding("errors", "tex_structure", "Unbalanced braces or explicit environments; see inventory.")
    if syntax_issues:
        finding("warnings", "python_escapes", "Non-raw TeX strings generated SyntaxWarnings; see inventory.")

    page_file = root / "records/pages.json"
    if page_file.exists():
        pages = json.loads(page_file.read_text(encoding="utf-8"))
        numbers = [item.get("page") for item in pages]
        checks["page_records"] = {"count": len(pages), "ordered_numbers": numbers}
        if numbers != list(range(1, len(pages) + 1)):
            finding("errors", "page_records", "Page records are not consecutive from 1.")
        if numbers != list(range(1, 77)):
            incomplete("page_records", str(len(pages)) + "/76 pages recorded.")
        if any(item.get("scan_page") != item.get("page", 0) + 7 for item in pages):
            finding("errors", "scan_page_mapping", "Unexpected mapping between printed and PDF page numbers.")
    else:
        incomplete("page_records", "records/pages.json absent.")
    check_record = root / "CHECK_RECORD.md"
    if check_record.exists():
        headings = [int(value) for value in re.findall(r"^## Página impressa (\d+)\s*$", check_record.read_text(encoding="utf-8"), re.M)]
        checks["check_record_sections"] = headings
        if headings != list(range(1, 77)):
            incomplete("check_record_sections", str(len(headings)) + "/76 page sections.")
    progress = root / "progress.log"
    if progress.exists():
        text = progress.read_text(encoding="utf-8")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC", text.splitlines()[0]):
            finding("errors", "progress_start", "First progress line is not the required UTC timestamp.")
        completed = [int(value) for value in re.findall(r"^page (\d+) done ", text, re.M)]
        checks["progress_pages"] = completed
        if completed != list(range(1, 77)):
            incomplete("progress_pages", str(len(completed)) + "/76 completion events.")

    correction_file = root / "CORRECTIONS.tsv"
    if correction_file.exists():
        fields, rows = read_tsv(correction_file)
        expected = ["file", "printed_page", "line", "old", "new", "kind", "evidence", "confidence"]
        if fields != expected:
            finding("errors", "correction_columns", "Unexpected correction-table columns.")
        unresolved = [number for number, row in enumerate(rows, 1)
                      if not re.match(r"^(confirmed|amended|withdrawn|confirmad|alterad|retirad)", row.get("confidence", ""), re.I)]
        missing_evidence = [number for number, row in enumerate(rows, 1) if not row.get("evidence", "").strip()]
        invalid_kinds = [{"row": number, "kind": row.get("kind", "")}
                         for number, row in enumerate(rows, 1)
                         if row.get("kind") not in CORRECTION_KINDS]
        checks["corrections"] = {"rows": len(rows), "second_reading_unresolved_rows": unresolved,
                                 "missing_evidence_rows": missing_evidence,
                                 "allowed_kinds": sorted(CORRECTION_KINDS),
                                 "invalid_kind_rows": invalid_kinds}
        if unresolved:
            incomplete("second_reading", "Unresolved rows: " + ", ".join(map(str, unresolved)))
        if missing_evidence:
            finding("errors", "correction_evidence", "Evidence missing from rows: " + ", ".join(map(str, missing_evidence)))
        if invalid_kinds:
            finding("errors", "correction_kind", "Kinds outside the required enumeration in rows: "
                    + ", ".join(str(item["row"]) for item in invalid_kinds))
    events = root / "CHECK_EVENTS.tsv"
    event_ids = set()
    if events.exists():
        fields, rows = read_tsv(events)
        if fields != ["statement_id", "date", "who", "type", "outcome"]:
            finding("errors", "check_event_columns", "Unexpected event-table columns.")
        empty = [number for number, row in enumerate(rows, 1) if any(not row.get(field, "").strip() for field in fields)]
        event_ids = {row.get("statement_id", "") for row in rows}
        invalid_types = [{"row": number, "type": row.get("type", "")}
                         for number, row in enumerate(rows, 1)
                         if row.get("type") not in EVENT_TYPES]
        checks["check_events"] = {"event_count": len(rows), "distinct_statement_ids": len(event_ids),
                                 "incomplete_rows": empty, "allowed_types": sorted(EVENT_TYPES),
                                 "invalid_type_rows": invalid_types}
        if empty:
            finding("errors", "check_events", "Event rows contain empty mandatory fields.")
        if invalid_types:
            finding("errors", "check_event_type", "Types outside the required enumeration in rows: "
                    + ", ".join(str(item["row"]) for item in invalid_types))

    source = root / "sources"
    headings = collect_numbered_headings(source)
    missing_events = sorted(set(headings) - event_ids)
    extra_events = sorted(event_ids - set(headings))
    repeated_headings = {identifier: places for identifier, places in headings.items() if len(places) > 1}
    checks["source_heading_event_coverage"] = {
        "scope": "Mechanical comparison with visible numbered headings in the current TeX sources; not a reading of the original scan.",
        "heading_count": sum(map(len, headings.values())),
        "distinct_heading_ids": len(headings),
        "source_heading_ids": sorted(headings),
        "headings_without_events": missing_events,
        "event_ids_without_headings": extra_events,
        "repeated_source_headings": repeated_headings,
    }
    if missing_events or extra_events or repeated_headings:
        incomplete("source_heading_event_coverage",
                   "Current source headings and event IDs differ or repeat; see the mechanical coverage inventory.")
    original_source = root.parent / "inputs/SGA3_PTBR_sources"
    current, links, macros = collect_labels(source)
    label_file = root / "records/LABEL_INVENTORY.json"
    original = original_macros = None
    if original_source.exists():
        original, _, original_macros = collect_labels(original_source)
    elif label_file.exists():
        saved = json.loads(label_file.read_text(encoding="utf-8"))
        original = saved.get("original_targets")
        original_macros = saved.get("original_macro_definitions")
    if original is not None:
        missing_targets = sorted(set(original) - set(current))
        missing_links = sorted((set(original) - set(current)) & set(links))
        duplicates = {name: places for name, places in current.items() if len(places) > 1}
        labels = {"created_utc": report["created_utc"], "original_target_count": len(original),
                  "current_target_count": len(current), "original_targets": original,
                  "original_macro_definitions": original_macros,
                  "preserved_original_target_count": len(set(original) & set(current)),
                  "missing_original_targets": missing_targets,
                  "remaining_links_to_missing_original_targets": missing_links,
                  "duplicate_current_targets": duplicates,
                  "missing_original_macro_definition_names": sorted(set(original_macros or {}) - set(macros))}
        label_file.parent.mkdir(parents=True, exist_ok=True)
        label_file.write_text(json.dumps(labels, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        checks["labels"] = {key: labels[key] for key in ("original_target_count", "current_target_count", "preserved_original_target_count", "missing_original_targets", "remaining_links_to_missing_original_targets", "duplicate_current_targets")}
        if missing_targets or duplicates:
            finding("warnings", "label_inventory", "Missing or repeated original targets are listed for the principal editor; no source was altered.")
        if missing_links:
            finding("errors", "dangling_internal_links", ", ".join(missing_links))
    else:
        finding("warnings", "label_baseline", "Original label inventory unavailable.")

    expected_sources = []
    manifest = root.parent / "inputs/MANIFEST.tsv"
    if manifest.exists():
        expected_sources = [{"file": "sources/" + row["path"][len(archive_support.SOURCE_PREFIX):], "sha256": row["sha256"]}
                            for row in archive_support.read_manifest(manifest) if row["path"].startswith(archive_support.SOURCE_PREFIX)]
    elif (root / "records/MANIFEST_VERIFICATION.json").exists():
        verified = json.loads((root / "records/MANIFEST_VERIFICATION.json").read_text(encoding="utf-8"))
        expected_sources = [{"file": "sources/" + row["file"][len(archive_support.SOURCE_PREFIX):], "sha256": row["sha256"]}
                            for row in verified["files"] if row["file"].startswith(archive_support.SOURCE_PREFIX)]
    absent_sources = [row["file"] for row in expected_sources if not (root / row["file"]).exists()]
    unchanged_sources = [row["file"] for row in expected_sources if (root / row["file"]).exists()
                         and hashlib.sha256((root / row["file"]).read_bytes()).hexdigest() == row["sha256"]]
    checks["source_tree"] = {"expected_files": len(expected_sources), "missing": absent_sources, "unchanged_from_attachment": unchanged_sources}
    if absent_sources or unchanged_sources:
        incomplete("source_tree", "Expected source files absent or still identical to the attachment; see inventory.")
    for name in ("ptbr_current", "ptbr_original"):
        path = source / (name + ".tex")
        if path.exists():
            text = path.read_text(encoding="utf-8")
            standalone = r"\begin{document}" in text and r"\end{document}" in text
            if not standalone:
                incomplete("master_assembly", name + " remains a front-matter fragment.")

    build_summary = root / "pdf/BUILD_SUMMARY.json"
    if build_summary.exists():
        summary = json.loads(build_summary.read_text(encoding="utf-8"))
        matched = summary.get("source_tree_sha256") == build_support.source_digest(source)
        checks["pdf_source_freshness"] = matched
        if not matched:
            incomplete("pdf_source_freshness", "PDF build does not record the current TeX-tree hash.")
        if {item.get("master") for item in summary.get("builds", [])} != {"ptbr_current", "ptbr_original"}:
            incomplete("both_masters_built", "Build summary does not contain both masters.")
        if any(not item.get("references_settled") for item in summary.get("builds", [])):
            finding("errors", "reference_stability", "A master has unsettled auxiliary files.")
    else:
        incomplete("build_summary", "pdf/BUILD_SUMMARY.json absent.")
    log_results = {}
    for name in ("ptbr_current", "ptbr_original"):
        path = root / "pdf" / (name + ".log")
        if not path.exists():
            incomplete("final_log", name + ".log absent.")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        overflows = [float(value) for value in re.findall(r"Overfull \\[hv]box \(([\d.]+)pt too (?:wide|high)\)", text)]
        unresolved = bool(re.search(r"There were undefined references|Reference .*? undefined|Label\(s\) may have changed", text))
        result = {"overfull_count": len(overflows), "over_2pt": sum(value > 2 for value in overflows),
                  "over_10pt": sum(value > 10 for value in overflows), "maximum_pt": max(overflows, default=0),
                  "unsettled_reference_warning": unresolved,
                  "missing_characters": text.count("Missing character:"),
                  "destination_warnings": text.count("pdfTeX warning (dest):")}
        log_results[name] = result
        if result["over_2pt"] or unresolved or result["missing_characters"] or result["destination_warnings"]:
            incomplete("pdf_log", name + " has unresolved layout, reference, or glyph issues.")
    checks["pdf_logs"] = log_results
    pdfs = [root / "pdf" / (name + ".pdf") for name in ("ptbr_current", "ptbr_original")]
    if all(path.is_file() for path in pdfs):
        if not shutil.which("pdftotext"):
            finding("errors", "pdf_equivalence", "pdftotext is required for the equivalence check.")
        else:
            texts = [unicodedata.normalize("NFC", command(["pdftotext", "-layout", str(path), "-"]).decode("utf-8")).replace("\r\n", "\n") for path in pdfs]
            same = texts[0] == texts[1] and bool(texts[0].strip())
            checks["pdf_text_equivalence"] = {"equal": same, "text_sha256": [hashlib.sha256(text.encode("utf-8")).hexdigest() for text in texts],
                                               "page_counts_from_form_feeds": [text.count(chr(12)) for text in texts]}
            if not same:
                finding("errors", "pdf_equivalence", "Extracted PDF texts differ or are empty.")
            pdf_privacy = []
            for path, text in zip(pdfs, texts):
                text_matches = archive_support.private_matches(text, prefixes)
                metadata_matches = []
                if shutil.which("pdfinfo"):
                    metadata = command(["pdfinfo", str(path)]).decode("utf-8", errors="replace")
                    metadata += command(["pdfinfo", "-meta", str(path)]).decode("utf-8", errors="replace")
                    metadata_matches = archive_support.private_matches(metadata, prefixes)
                else:
                    incomplete("pdf_metadata_privacy", "pdfinfo is required to inspect PDF metadata.")
                pdf_privacy.append({"file": path.relative_to(root).as_posix(),
                                    "text_match_count": len(text_matches),
                                    "metadata_match_count": len(metadata_matches)})
                if text_matches or metadata_matches:
                    finding("errors", "pdf_privacy", path.relative_to(root).as_posix()
                            + " contains a local path or email in text or metadata.")
            checks["pdf_privacy"] = pdf_privacy
    else:
        incomplete("pdf_equivalence", "Both final PDFs are required.")

    report["passed"] = not report["errors"] and (args.progress or not report["pending"])
    destination = root / "records/TECHNICAL_VALIDATION.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"mode": report["mode"], "passed": report["passed"], "errors": report["errors"],
                      "warnings": report["warnings"], "pending": report["pending"],
                      "report": "records/TECHNICAL_VALIDATION.json"}, ensure_ascii=False, indent=2))
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
