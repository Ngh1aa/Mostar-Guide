#!/usr/bin/env python3
"""Post-process Huế Imperial Threshold layers after rendered integration review.

V5 fixed the duplicated split pair. V6 removes the bright low-saturation sky from
the Ngọ Môn threshold/split layers so the architecture behaves like a cinematic
foreground cutout over the river world instead of an opaque rectangular photo.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter

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


def sky_key_mask(img: Image.Image) -> Image.Image:
    """Build a soft matte that removes bright neutral sky while preserving architecture.

    The source has an almost white/grey sky and substantially darker or more
    saturated roofs/walls/foliage. We key only bright + low-saturation pixels and
    feather the transition, avoiding a semantic segmentation dependency.
    """
    rgb = img.convert("RGB")
    hsv = rgb.convert("HSV")
    w, h = rgb.size
    hp = hsv.load()
    mask = Image.new("L", (w, h), 255)
    mp = mask.load()

    # Protect the lower architectural mass even when stone highlights are bright.
    protect_after = int(h * 0.67)
    for y in range(h):
        for x in range(w):
            if y >= protect_after:
                continue
            _hue, sat, val = hp[x, y]
            # Neutral + bright pixels are sky candidates. The range between
            # 180..225 creates a soft alpha ramp rather than a hard chroma key.
            if sat < 74 and val > 180:
                strength = min(1.0, max(0.0, (val - 180) / 45.0))
                neutral = min(1.0, max(0.0, (74 - sat) / 40.0))
                remove = strength * neutral
                mp[x, y] = round(255 * (1.0 - remove))

    return mask.filter(ImageFilter.GaussianBlur(2.2))


def grade_registered_source(source: Image.Image) -> Image.Image:
    full = builder.cover(source, builder.CANVAS, focus=(0.50, 0.60))
    full = builder.grade(
        full,
        saturation=0.88,
        contrast=1.02,
        brightness=0.94,
        tint=(64, 27, 20, 10),
    )
    return full


def build_pair(source: Image.Image) -> tuple[Image.Image, Image.Image]:
    full = grade_registered_source(source)
    keyed = sky_key_mask(full)

    left = full.copy()
    right = full.copy()
    left.putalpha(ImageChops.multiply(keyed, split_mask("left")))
    right.putalpha(ImageChops.multiply(keyed, split_mask("right")))
    return left, right


def rebuild_threshold(source: Image.Image) -> Image.Image:
    """Create one centered architectural portal with keyed sky and restrained edges."""
    panel_size = (1600, 900)
    panel = builder.cover(source, panel_size, focus=(0.50, 0.60))
    panel = builder.grade(
        panel,
        saturation=0.92,
        contrast=1.04,
        brightness=0.92,
        tint=(76, 28, 20, 12),
    )

    key = sky_key_mask(panel)
    edge = Image.new("L", panel_size, 0)
    ed = ImageDraw.Draw(edge)
    ed.rectangle((14, 14, panel_size[0] - 14, panel_size[1] - 14), fill=255)
    edge = edge.filter(ImageFilter.GaussianBlur(10))
    panel.putalpha(ImageChops.multiply(key, edge))

    canvas = Image.new("RGBA", builder.CANVAS, (0, 0, 0, 0))
    canvas.alpha_composite(panel, (160, 90))
    return canvas


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
            entries.append(("04+05 split-pair proof · sky keyed", pair_bg.convert("RGB")))

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
    manifest["visual_veto_revision"] = "v6-render-integration"

    changes = {
        "scenes/03-ngo-mon-threshold.webp": "centered Ngọ Môn architectural portal; bright low-saturation sky keyed to alpha; restrained edge feather for cinematic layering",
        "scenes/04-imperial-left.webp": "registered left half of shared Ngọ Môn crop; bright neutral sky keyed to alpha; centre-edge feather only",
        "scenes/05-imperial-right.webp": "registered right half of shared Ngọ Môn crop; bright neutral sky keyed to alpha; centre-edge feather only",
    }
    for item in manifest["generated"]:
        rel = item["path"]
        path = builder.OUT / rel
        if rel in changes:
            item["changes"] = changes[rel]
            item["sha256"] = builder.sha256(path)
            item["mode"] = Image.open(path).mode
        if rel == "previews/scene-contact-sheet.webp":
            item["changes"] = "render-integration contact sheet; seven scene outputs plus keyed 04+05 split-pair proof"
            item["sha256"] = builder.sha256(path)
            item["size"] = list(Image.open(path).size)

    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    credits_path = builder.OUT / "CREDITS.md"
    credits = credits_path.read_text(encoding="utf-8")
    for rel, text in changes.items():
        pattern = rf"(### `{re.escape(rel)}`.*?- \*\*Transformation:\*\* )[^\n]+"
        credits = re.sub(pattern, r"\1" + text, credits, flags=re.S)
    credits = re.sub(
        r"(### `previews/scene-contact-sheet\.webp`.*?- \*\*Transformation:\*\* )[^\n]+",
        r"\1render-integration contact sheet; seven scene outputs plus keyed 04+05 split-pair proof",
        credits,
        flags=re.S,
    )
    credits_path.write_text(credits, encoding="utf-8")


def main() -> int:
    source = Image.open(builder.SOURCE_DIR / "ngo-mon.jpg").convert("RGB")

    threshold = rebuild_threshold(source)
    left, right = build_pair(source)
    builder.save_webp(threshold, builder.SCENE_DIR / "03-ngo-mon-threshold.webp")
    builder.save_webp(left, builder.SCENE_DIR / "04-imperial-left.webp")
    builder.save_webp(right, builder.SCENE_DIR / "05-imperial-right.webp")

    scene_paths = sorted(builder.SCENE_DIR.glob("*.webp"))
    contact_sheet(scene_paths, left, right)

    pair_bg = Image.new("RGBA", builder.CANVAS, (*BG, 255))
    pair_bg = Image.alpha_composite(pair_bg, left)
    pair_bg = Image.alpha_composite(pair_bg, right)
    pair_path = builder.PREVIEW_DIR / "split-pair-proof.webp"
    builder.save_webp(pair_bg.convert("RGB"), pair_path, quality=86)

    update_metadata()

    print("Refined Imperial layers: aligned split pair + bright-sky alpha key")
    print(f"Proof: {pair_path}")
    return 0


raise SystemExit(main())
