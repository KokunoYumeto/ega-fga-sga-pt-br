"""Render the corrected PDF for inspection and record a mechanical page map.

Images are written outside the deliverable tree by default and are not packed.
No visual inspection or mathematical verification is claimed by this program.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont


def page_map(page, number, image_name):
    lines = []
    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            spans = line.get("spans", [])
            text = "".join(span.get("text", "") for span in spans).strip()
            if text:
                lines.append({"text": text, "x": line["bbox"][0], "y": line["bbox"][1],
                              "bottom": line["bbox"][3],
                              "size": max((span.get("size", 0) for span in spans), default=0)})
    lines.sort(key=lambda item: (round(item["y"], 1), item["x"]))
    body = [line for line in lines if line["y"] >= 65 and line["bottom"] < page.rect.height - 35]
    headings = [line["text"] for line in body if line["size"] >= 13]
    return {"pdf_page": number, "page_label": page.get_label() or str(number),
            "first_line": lines[0]["text"] if lines else "",
            "first_body_line": body[0]["text"] if body else "",
            "first_three_body_lines": " | ".join(line["text"] for line in body[:3]),
            "headings_by_font_size": " | ".join(headings), "image": image_name}


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, default=root / "pdf/ptbr_current.pdf")
    parser.add_argument("--output-directory", type=Path, default=root.parent / "tmp/pdf_final")
    parser.add_argument("--scale", type=float, default=1.4)
    parser.add_argument("--per-sheet", type=int, default=12)
    args = parser.parse_args()
    if args.scale <= 0 or args.per_sheet <= 0:
        parser.error("scale and per-sheet must be positive")
    source, destination = args.pdf.resolve(), args.output_directory.resolve()
    if destination == root or root in destination.parents:
        parser.error("inspection images must be outside the deliverable tree")
    destination.mkdir(parents=True, exist_ok=True)
    document = fitz.open(source)
    mapping = []
    for index, page in enumerate(document):
        name = f"page_{index + 1:03d}.png"
        pixmap = page.get_pixmap(matrix=fitz.Matrix(args.scale, args.scale), alpha=False)
        pixmap.save(destination / name)
        item = page_map(page, index + 1, name)
        item.update({"width_px": pixmap.width, "height_px": pixmap.height})
        mapping.append(item)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 17)
    except OSError:
        font = ImageFont.load_default()
    columns, thumb_width, gap, margin, label_height = 4, 240, 18, 18, 28
    thumb_height = round(thumb_width * document[0].rect.height / document[0].rect.width)
    contacts = []
    for start in range(0, len(mapping), args.per_sheet):
        batch = mapping[start:start + args.per_sheet]
        rows = (len(batch) + columns - 1) // columns
        canvas = Image.new("RGB", (2 * margin + columns * thumb_width + (columns - 1) * gap,
                                   2 * margin + rows * (thumb_height + label_height) + (rows - 1) * gap), "#e6e6e6")
        draw = ImageDraw.Draw(canvas)
        for index, item in enumerate(batch):
            x = margin + (index % columns) * (thumb_width + gap)
            y = margin + (index // columns) * (thumb_height + label_height + gap)
            draw.text((x, y + 2), f"PDF {item['pdf_page']:02d}  |  {item['page_label']}", fill="black", font=font)
            with Image.open(destination / item["image"]) as original:
                thumbnail = original.convert("RGB")
                thumbnail.thumbnail((thumb_width, thumb_height), Image.Resampling.LANCZOS)
                canvas.paste(thumbnail, (x, y + label_height))
                draw.rectangle((x, y + label_height, x + thumbnail.width, y + label_height + thumbnail.height), outline="#777777", width=1)
        name = f"contact_{start // args.per_sheet + 1:02d}.png"
        canvas.save(destination / name)
        contacts.append({"image": name, "first_pdf_page": batch[0]["pdf_page"], "last_pdf_page": batch[-1]["pdf_page"]})
    records = root / "records"
    records.mkdir(parents=True, exist_ok=True)
    fields = ["pdf_page", "page_label", "first_line", "first_body_line", "first_three_body_lines", "headings_by_font_size", "image"]
    with (records / "PDF_PAGE_MAP.tsv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(mapping)
    metadata = {"created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
                "pdf": source.name, "pdf_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                "page_count": len(mapping), "render_scale": args.scale, "dpi_equivalent": 72 * args.scale,
                "contact_sheets": contacts, "pages": mapping,
                "inspection_status": "Rendered for inspection; no visual approval is asserted by this script."}
    (records / "PDF_RENDER_METADATA.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"page_count": len(mapping), "scale": args.scale, "contact_sheets": contacts,
                      "page_map": "records/PDF_PAGE_MAP.tsv", "metadata": "records/PDF_RENDER_METADATA.json"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
