"""Compare both PDF masters and refresh only changed inspection images.

All PDF pages are rasterized in memory at the recorded scale. RGB pixel hashes
are compared with the previous PNGs and with the other master. No source or
final prose document is changed. Inspection images remain outside the package.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import re
import unicodedata

import fitz
from PIL import Image, ImageDraw, ImageFont

from render_pdf import page_map


def sha(data):
    return hashlib.sha256(data).hexdigest()


def contact_sheet(directory, batch, number, thumb_height):
    columns, width, gap, margin, label_height = 4, 240, 18, 18, 28
    rows = (len(batch) + columns - 1) // columns
    canvas = Image.new("RGB", (2 * margin + columns * width + (columns - 1) * gap,
                               2 * margin + rows * (thumb_height + label_height) + (rows - 1) * gap), "#e6e6e6")
    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 17)
    except OSError:
        font = ImageFont.load_default()
    for index, item in enumerate(batch):
        x = margin + (index % columns) * (width + gap)
        y = margin + (index // columns) * (thumb_height + label_height + gap)
        draw.text((x, y + 2), f"PDF {item['pdf_page']:02d}  |  {item['page_label']}", fill="black", font=font)
        with Image.open(directory / item["image"]) as image:
            thumbnail = image.convert("RGB")
            thumbnail.thumbnail((width, thumb_height), Image.Resampling.LANCZOS)
            canvas.paste(thumbnail, (x, y + label_height))
            draw.rectangle((x, y + label_height, x + thumbnail.width, y + label_height + thumbnail.height), outline="#777777", width=1)
    canvas.save(directory / f"contact_{number:02d}.png")


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--current", type=Path, default=root / "pdf/ptbr_current.pdf")
    parser.add_argument("--other", type=Path, default=root / "pdf/ptbr_original.pdf")
    parser.add_argument("--images", type=Path, default=root.parent / "tmp/pdf_final")
    parser.add_argument("--baseline-pdf", type=Path)
    args = parser.parse_args()
    images = args.images.resolve()
    metadata_file = root / "records/PDF_RENDER_METADATA.json"
    previous = json.loads(metadata_file.read_text(encoding="utf-8"))
    scale = previous["render_scale"]
    current = fitz.open(args.current)
    other = fitz.open(args.other)
    changed, comparison, mapping, writes = [], [], [], {}
    for index, page in enumerate(current):
        number = index + 1
        name = f"page_{number:03d}.png"
        pixel = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
        size = [pixel.width, pixel.height]
        pixel_hash = sha(pixel.samples)
        old_hash = None
        old_size = None
        if (images / name).exists():
            with Image.open(images / name) as image:
                rgb = image.convert("RGB")
                old_hash, old_size = sha(rgb.tobytes()), list(rgb.size)
        different = old_hash != pixel_hash or old_size != size
        if different:
            changed.append(number)
            writes[name] = pixel.tobytes("png")
        other_hash, other_size = None, None
        if index < len(other):
            second = other[index].get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
            other_hash, other_size = sha(second.samples), [second.width, second.height]
            if other_hash != pixel_hash or other_size != size:
                writes[f"original_page_{number:03d}.png"] = second.tobytes("png")
        comparison.append({"pdf_page": number, "size_px": size, "rgb_sha256_current": pixel_hash,
                           "rgb_sha256_original": other_hash, "masters_pixel_identical": pixel_hash == other_hash and size == other_size,
                           "previous_rgb_sha256": old_hash, "changed_from_previous_render": different})
        item = page_map(page, number, name)
        item.update({"width_px": pixel.width, "height_px": pixel.height})
        mapping.append(item)
    removed = list(range(len(current) + 1, previous["page_count"] + 1))
    baseline = previous.get("baseline_toc")
    if args.baseline_pdf:
        baseline_doc = fitz.open(args.baseline_pdf)
        matches = []
        for index, page in enumerate(baseline_doc):
            normalized = "".join(char for char in unicodedata.normalize("NFKD", page.get_text())
                                 if not unicodedata.combining(char)).upper()
            if re.search(r"\bEXPOSICAO\s+XI\b", normalized) and "CRITERIOS DE REPRESENTABILIDADE" in normalized:
                matches.append(index)
        if len(matches) != 1:
            raise ValueError("Expected exactly one baseline contents page with Exposition XI.")
        number = matches[0]
        writes["baseline_toc.png"] = baseline_doc[number].get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False).tobytes("png")
        baseline = {"pdf": args.baseline_pdf.name, "scope": "isolated preliminary infrastructure baseline",
                    "pdf_sha256": sha(args.baseline_pdf.read_bytes()), "pdf_page": number + 1,
                    "page_label": baseline_doc[number].get_label() or str(number + 1),
                    "image": "baseline_toc.png", "render_scale": scale}
    # Writes begin only after all comparisons and the optional baseline lookup succeed.
    for name, data in writes.items():
        (images / name).write_bytes(data)
    for number in removed:
        (images / f"page_{number:03d}.png").unlink(missing_ok=True)
    contacts = []
    changed_sheets = {(number - 1) // 12 + 1 for number in changed + removed}
    thumb_height = round(240 * current[0].rect.height / current[0].rect.width)
    for start in range(0, len(mapping), 12):
        number = start // 12 + 1
        batch = mapping[start:start + 12]
        name = f"contact_{number:02d}.png"
        if number in changed_sheets or not (images / name).exists():
            contact_sheet(images, batch, number, thumb_height)
        contacts.append({"image": name, "first_pdf_page": batch[0]["pdf_page"], "last_pdf_page": batch[-1]["pdf_page"]})
    equal = len(current) == len(other) and all(item["masters_pixel_identical"] for item in comparison)
    metadata = {"created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
                "pdf": args.current.name, "pdf_sha256": sha(args.current.read_bytes()),
                "page_count": len(current), "render_scale": scale, "dpi_equivalent": 72 * scale,
                "contact_sheets": contacts, "pages": mapping,
                "pixel_comparison": {"method": "SHA-256 of raw RGB raster samples, with dimensions compared separately",
                                     "other_pdf": args.other.name, "other_pdf_sha256": sha(args.other.read_bytes()),
                                     "other_page_count": len(other), "all_pages_identical": equal,
                                     "different_master_pages": [item["pdf_page"] for item in comparison if not item["masters_pixel_identical"]],
                                     "pages": comparison},
                "transition_from_previous_render": {"previous_pdf_sha256": previous["pdf_sha256"],
                                                    "previous_page_count": previous["page_count"],
                                                    "changed_pages": changed, "removed_pages": removed,
                                                    "refreshed_contact_sheets": sorted(changed_sheets)},
                "inspection_status": "Rendered for inspection; no visual approval is asserted by this script."}
    if baseline:
        metadata["baseline_toc"] = baseline
    output = io.StringIO(newline="")
    fields = ["pdf_page", "page_label", "first_line", "first_body_line", "first_three_body_lines", "headings_by_font_size", "image"]
    writer = csv.DictWriter(output, fieldnames=fields, delimiter="\t", extrasaction="ignore")
    writer.writeheader()
    writer.writerows(mapping)
    (root / "records/PDF_PAGE_MAP.tsv").write_text(output.getvalue(), encoding="utf-8")
    temporary = metadata_file.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(metadata_file)
    print(json.dumps({"page_count": len(current), "all_master_pages_pixel_identical": equal,
                      "changed_pages_from_previous_render": changed, "removed_pages": removed,
                      "refreshed_contact_sheets": sorted(changed_sheets), "baseline_toc": baseline,
                      "current_pdf_sha256": metadata["pdf_sha256"],
                      "original_pdf_sha256": metadata["pixel_comparison"]["other_pdf_sha256"],
                      "metadata": "records/PDF_RENDER_METADATA.json"}, ensure_ascii=False, indent=2))
    if not equal:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
