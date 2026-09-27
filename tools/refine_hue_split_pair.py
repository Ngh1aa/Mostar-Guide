#!/usr/bin/env python3
"""Post-process the Huế Imperial Threshold split pair after human visual veto.

The first split treatment duplicated the gate when the two animated layers were
combined. This refinement keeps both layers registered to the same full-frame
Ngọ Môn crop and changes only their alpha masks, so the pair reconstructs one
continuous architectural scene before the doors separate in motion.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

import build_hue_assets as builder

BG = (10, 17, 16)


def split_mask(side: str) -> Image.Image:
    w, h = builder.CANVAS
    mask = Image.new("L", builder.CANVAS, 0)
    d = ImageDraw.Draw(mask)
    if side == "left":
        d.rectangle((0, 0, 980, h), fill=255)
    else:
        d.rectangle((940, 0, w, h), fill=255)
    return mask.filter(ImageFilter.GaussianBlur(12))


def build_pair(source: Image.Image) -> tuple[Image.Image, Image.Image]:
    full = builder.cover(source, builder.CANVAS, focus=(0.50, 0.60))
    full = builder.grade(
        full,
        saturation=0.88,
        contrast=1.02,
        brightness=0.94,
        tint=(64, 27, 20, 10),
    )
    left = full.copy()
    right = full.copy()
    left.putalpha(split_mask("left"))
    right.putalpha(split_mask("right"))
    return left, right


def contact_sheet(scene_paths: list[Path], left: Image.Image, right: Image.Image) -> None:
    tile_w, tile_h = 480, 270
    gap = 24
    entries: list[tuple[str, Image.Image]] = []

    for path in scene_paths:
        img = Image.open(path).convert("RGBA")
        dark = Image.new("RGBA", img.size, (*BG, 255))
        rendered = Image.alpha_composite(dark, img).convert("RGB")
        entries.append((path.name, rendered))
        if path.name == "05-imperial-right.webp":
            pair_bg = Image.new("RGBA", builder.CANVAS, (*BG, 255))
            pair_bg = Image.alpha_composite(pair_bg, left)
            pair_bg = Image.alpha_composite(pair_bg, right)
            entries.append(("04+05 split-pair preview", pair_bg.convert("RGB")))

    cols = 2
    rows = math.ceil(len(entries) / cols)
    sheet = Image.new(
        "RGB",
        (cols * tile_w + (cols + 1) * gap, rows * (tile_h + 44) + (rows + 1) * gap),
        BG,
    )
    d = ImageDraw.Draw(sheet)
    f = builder.font(18)
    for i, (label, rendered) in enumerate(entries):
        thumb = builder.cover(rendered, (tile_w, tile_h))
        col, row = i % cols, i // cols
        x = gap + col * (tile_w + gap)
        y = gap + row * (tile_h + 44 + gap)
        sheet.paste(thumb, (x, y))
        d.text((x, y + tile_h + 10), label, fill=(239, 231, 211), font=f)

    builder.save_webp(sheet, builder.PREVIEW_DIR / "scene-contact-sheet.webp", quality=85)


def update_metadata() -> None:
    manifest_path = builder.OUT / "asset-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["visual_veto_revision"] = "v5"

    changes = {
        "scenes/04-imperial-left.webp": "registered left half of one shared Ngọ Môn full-frame crop; centre-edge feather only; reconstructs a single scene with 05 before split motion",
        "scenes/05-imperial-right.webp": "registered right half of one shared Ngọ Môn full-frame crop; centre-edge feather only; reconstructs a single scene with 04 before split motion",
    }
    for item in manifest["generated"]:
        rel = item["path"]
        path = builder.OUT / rel
        if rel in changes:
            item["changes"] = changes[rel]
            item["sha256"] = builder.sha256(path)
            item["mode"] = Image.open(path).mode
        if rel == "previews/scene-contact-sheet.webp":
            item["changes"] = "visual-veto contact sheet of seven scene outputs plus aligned 04+05 split-pair preview"
            item["sha256"] = builder.sha256(path)
            item["size"] = list(Image.open(path).size)

    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    credits_path = builder.OUT / "CREDITS.md"
    credits = credits_path.read_text(encoding="utf-8")
    credits = re.sub(
        r"(### `scenes/04-imperial-left\.webp`.*?- \*\*Transformation:\*\* )[^\n]+",
        r"\1" + changes["scenes/04-imperial-left.webp"],
        credits,
        flags=re.S,
    )
    credits = re.sub(
        r"(### `scenes/05-imperial-right\.webp`.*?- \*\*Transformation:\*\* )[^\n]+",
        r"\1" + changes["scenes/05-imperial-right.webp"],
        credits,
        flags=re.S,
    )
    credits = re.sub(
        r"(### `previews/scene-contact-sheet\.webp`.*?- \*\*Transformation:\*\* )[^\n]+",
        r"\1visual-veto contact sheet of seven scene outputs plus aligned 04+05 split-pair preview",
        credits,
        flags=re.S,
    )
    credits_path.write_text(credits, encoding="utf-8")


def main() -> int:
    source = Image.open(builder.SOURCE_DIR / "ngo-mon.jpg").convert("RGB")
    left, right = build_pair(source)
    builder.save_webp(left, builder.SCENE_DIR / "04-imperial-left.webp")
    builder.save_webp(right, builder.SCENE_DIR / "05-imperial-right.webp")

    scene_paths = sorted(builder.SCENE_DIR.glob("*.webp"))
    contact_sheet(scene_paths, left, right)
    update_metadata()

    pair_bg = Image.new("RGBA", builder.CANVAS, (*BG, 255))
    pair_bg = Image.alpha_composite(pair_bg, left)
    pair_bg = Image.alpha_composite(pair_bg, right)
    pair_path = builder.PREVIEW_DIR / "split-pair-proof.webp"
    builder.save_webp(pair_bg.convert("RGB"), pair_path, quality=86)

    print("Refined Imperial split pair: aligned single-scene reconstruction")
    print(f"Proof: {pair_path}")
    return 0


raise SystemExit(main())
