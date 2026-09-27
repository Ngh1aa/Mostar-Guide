#!/usr/bin/env python3
"""Stable CI entrypoint for Huế asset production.

This wrapper owns production-source overrides and the visual-veto refinements.
It intentionally leaves the shipped application HTML/CSS/JS untouched until the
asset gate is visually approved.
"""

from pathlib import Path
import json
import math

from PIL import Image, ImageDraw, ImageFilter

import build_hue_assets as builder

# ---------------------------------------------------------------------------
# Production source overrides
# ---------------------------------------------------------------------------

builder.SOURCES["A01"].update(
    {
        "slug": "ngo-mon",
        "title": "The grand entrance complex to the Imperial Citadel (31801617815).jpg",
        "author": "shankar s.",
        "license": "CC BY 2.0",
        "license_url": "https://creativecommons.org/licenses/by/2.0/",
        "page_url": "https://commons.wikimedia.org/wiki/File:The_grand_entrance_complex_to_the_Imperial_Citadel_(31801617815).jpg",
        "download_url": (
            "https://upload.wikimedia.org/wikipedia/commons/6/6a/"
            "The_grand_entrance_complex_to_the_Imperial_Citadel_%2831801617815%29.jpg"
        ),
        "role": "Imperial Threshold / frontal Ngọ Môn grand-entrance composition",
        "note": "Selected after visual veto because the earlier close gate crop did not read strongly enough as the project signature.",
    }
)

builder.SOURCES["A03"].update(
    {
        "slug": "truong-tien",
        "title": "Truong Tien Bridge.jpg",
        "author": "Lưu Ly",
        "license": "Public Domain",
        "license_url": "https://commons.wikimedia.org/wiki/File:Truong_Tien_Bridge.jpg",
        "page_url": "https://commons.wikimedia.org/wiki/File:Truong_Tien_Bridge.jpg",
        "download_url": "https://upload.wikimedia.org/wikipedia/commons/1/13/Truong_Tien_Bridge.jpg",
        "role": "River crossing / reflection / horizontal connective geometry",
        "note": "Selected for a full-frame river transition rather than a ghosted bridge composite.",
    }
)

builder.SOURCES["A04"]["download_url"] = (
    "https://upload.wikimedia.org/wikipedia/commons/5/5e/"
    "Khai_Dinh_tomb_Hue_%2827767136409%29.jpg"
)
builder.SOURCES["A05"]["download_url"] = (
    "https://upload.wikimedia.org/wikipedia/commons/0/05/"
    "Dong_Ba_market%2C_Th%C3%A0nh_ph%E1%BB%91_Hu%E1%BA%BF%2C_Vietnam_%28Unsplash%29.jpg"
)


# ---------------------------------------------------------------------------
# Visual-veto v4 compositions
# ---------------------------------------------------------------------------

DARK = (10, 17, 16, 255)
GOLD = (211, 177, 101, 150)
IVORY = (239, 231, 211, 220)


def feathered_rect_mask(size: tuple[int, int], inset: int = 18, blur: int = 12) -> Image.Image:
    """A restrained rectangular feather; avoids the tunnel/vignette look."""
    w, h = size
    mask = Image.new("L", size, 0)
    d = ImageDraw.Draw(mask)
    d.rectangle((inset, inset, w - inset, h - inset), fill=255)
    return mask.filter(ImageFilter.GaussianBlur(blur))


def one_edge_mask(size: tuple[int, int], edge: str, feather: int = 72) -> Image.Image:
    """Opaque panel with only its inner split edge feathered."""
    w, h = size
    mask = Image.new("L", size, 255)
    px = mask.load()
    if edge == "right":
        for x in range(max(0, w - feather), w):
            alpha = round(255 * (w - 1 - x) / max(1, feather - 1))
            for y in range(h):
                px[x, y] = max(0, min(255, alpha))
    else:
        for x in range(0, min(feather, w)):
            alpha = round(255 * x / max(1, feather - 1))
            for y in range(h):
                px[x, y] = max(0, min(255, alpha))
    return mask.filter(ImageFilter.GaussianBlur(5))


def scene_river_v4(img: Image.Image) -> Image.Image:
    """Quieter river opener with more spatial depth and less grey blur."""
    base = builder.cover(img, builder.CANVAS, focus=(0.47, 0.48))
    base = builder.grade(
        base,
        saturation=0.78,
        contrast=0.96,
        brightness=0.96,
        tint=(16, 48, 46, 22),
    )
    mist = Image.new("RGBA", builder.CANVAS, (0, 0, 0, 0))
    md = ImageDraw.Draw(mist)
    md.rectangle((0, 0, 1920, 250), fill=(232, 229, 209, 24))
    mist = mist.filter(ImageFilter.GaussianBlur(70))
    base = Image.alpha_composite(base, mist)
    return Image.alpha_composite(
        base,
        builder.vertical_gradient(builder.CANVAS, (7, 18, 17, 0), (7, 18, 17, 84)),
    )


def scene_citadel_v4(img: Image.Image) -> Image.Image:
    """Readable establishing image; keep stone and roof detail alive."""
    base = builder.cover(img, builder.CANVAS, focus=(0.50, 0.57))
    base = builder.grade(
        base,
        saturation=0.84,
        contrast=0.99,
        brightness=0.90,
        tint=(68, 30, 23, 12),
    )
    return Image.alpha_composite(
        base,
        builder.vertical_gradient(builder.CANVAS, (10, 15, 14, 18), (7, 13, 12, 92)),
    )


def scene_threshold_v4(img: Image.Image) -> Image.Image:
    """Architectural threshold as an inset portal, not a black tunnel vignette."""
    panel_size = (1600, 900)
    panel = builder.cover(img, panel_size, focus=(0.50, 0.60))
    panel = builder.grade(
        panel,
        saturation=0.92,
        contrast=1.04,
        brightness=0.98,
        tint=(76, 28, 20, 10),
    )
    panel.putalpha(feathered_rect_mask(panel_size, inset=14, blur=10))

    canvas = Image.new("RGBA", builder.CANVAS, (0, 0, 0, 0))
    canvas.alpha_composite(panel, (160, 90))

    frame = Image.new("RGBA", builder.CANVAS, (0, 0, 0, 0))
    fd = ImageDraw.Draw(frame)
    fd.line((170, 82, 1750, 82), fill=(211, 177, 101, 76), width=1)
    fd.line((170, 998, 1750, 998), fill=(239, 231, 211, 48), width=1)
    return Image.alpha_composite(canvas, frame)


def scene_split_v4(img: Image.Image, side: str) -> Image.Image:
    """Complementary architectural doors with clean geometry and modest overlap."""
    panel_size = (1040, 1080)
    focus = (0.32, 0.60) if side == "left" else (0.68, 0.60)
    panel = builder.cover(img, panel_size, focus=focus)
    panel = builder.grade(
        panel,
        saturation=0.88,
        contrast=1.02,
        brightness=0.94,
        tint=(64, 27, 20, 10),
    )
    panel.putalpha(one_edge_mask(panel_size, "right" if side == "left" else "left", feather=76))

    canvas = Image.new("RGBA", builder.CANVAS, (0, 0, 0, 0))
    x = 0 if side == "left" else 880
    canvas.alpha_composite(panel, (x, 0))
    return canvas


def scene_river_transition_v4(bridge: Image.Image) -> Image.Image:
    """Use Trường Tiền as one coherent full-frame scene; no pasted photo band."""
    base = builder.cover(bridge, builder.CANVAS, focus=(0.50, 0.54))
    base = builder.grade(
        base,
        saturation=0.60,
        contrast=0.98,
        brightness=0.86,
        tint=(17, 53, 51, 26),
    )
    base = Image.alpha_composite(
        base,
        builder.vertical_gradient(builder.CANVAS, (7, 17, 16, 8), (6, 14, 13, 118)),
    )

    river_line = Image.new("RGBA", builder.CANVAS, (0, 0, 0, 0))
    ld = ImageDraw.Draw(river_line)
    points = [(90, 820), (490, 798), (930, 772), (1370, 742), (1830, 726)]
    ld.line(points, fill=GOLD, width=2)
    for x, y in (points[1], points[2], points[3]):
        ld.ellipse((x - 4, y - 4, x + 4, y + 4), fill=IVORY)
    return Image.alpha_composite(base, river_line)


def scene_beyond_v4(khai: Image.Image, market: Image.Image) -> Image.Image:
    """Intentional editorial diptych instead of a muddy diagonal double exposure."""
    canvas = Image.new("RGBA", builder.CANVAS, DARK)
    canvas = Image.alpha_composite(
        canvas,
        builder.vertical_gradient(builder.CANVAS, (20, 26, 23, 0), (3, 8, 7, 92)),
    )

    left_size = (1180, 900)
    left = builder.cover(khai, left_size, focus=(0.47, 0.56))
    left = builder.grade(
        left,
        saturation=0.72,
        contrast=1.03,
        brightness=0.88,
        tint=(35, 36, 31, 10),
    )
    canvas.alpha_composite(left, (60, 90))

    right_size = (540, 760)
    right = builder.cover(market, right_size, focus=(0.60, 0.50))
    right = builder.grade(
        right,
        saturation=0.94,
        contrast=1.02,
        brightness=0.90,
        tint=(70, 28, 22, 8),
    )
    canvas.alpha_composite(right, (1320, 170))

    details = Image.new("RGBA", builder.CANVAS, (0, 0, 0, 0))
    dd = ImageDraw.Draw(details)
    dd.line((60, 1014, 1240, 1014), fill=(211, 177, 101, 110), width=2)
    dd.line((1320, 950, 1860, 950), fill=(239, 231, 211, 70), width=1)
    dd.ellipse((1266, 520, 1276, 530), fill=(211, 177, 101, 190))
    return Image.alpha_composite(canvas, details)


def contact_sheet_v4(scene_paths: list[Path]) -> None:
    """Show seven real outputs plus one combined split-pair preview for human veto."""
    tile_w, tile_h = 480, 270
    gap = 24
    bg_rgb = (10, 17, 16)

    entries: list[tuple[str, Image.Image]] = []
    cached: dict[str, Image.Image] = {}
    for path in scene_paths:
        img = Image.open(path).convert("RGBA")
        dark = Image.new("RGBA", img.size, (*bg_rgb, 255))
        rendered = Image.alpha_composite(dark, img).convert("RGB")
        cached[path.name] = img
        entries.append((path.name, rendered))
        if path.name == "05-imperial-right.webp":
            pair_bg = Image.new("RGBA", builder.CANVAS, (*bg_rgb, 255))
            pair_bg = Image.alpha_composite(pair_bg, cached["04-imperial-left.webp"])
            pair_bg = Image.alpha_composite(pair_bg, cached["05-imperial-right.webp"])
            entries.append(("04+05 split-pair preview", pair_bg.convert("RGB")))

    cols = 2
    rows = math.ceil(len(entries) / cols)
    sheet = Image.new(
        "RGB",
        (cols * tile_w + (cols + 1) * gap, rows * (tile_h + 44) + (rows + 1) * gap),
        bg_rgb,
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


def main_v4() -> int:
    builder.ensure_dirs()
    masters: dict[str, Image.Image] = {}
    source_manifest = {}

    for sid, meta in builder.SOURCES.items():
        img = builder.download_image(meta)
        path = builder.SOURCE_DIR / f"{meta['slug']}.jpg"
        builder.save_jpeg(img, path)
        masters[sid] = Image.open(path).convert("RGB")
        source_manifest[sid] = {
            **meta,
            "local_path": str(path.relative_to(builder.ROOT)),
            "pixels": list(masters[sid].size),
            "sha256": builder.sha256(path),
        }

    outputs = [
        ("01-river-atmosphere.webp", scene_river_v4(masters["A02"]), ["A02"], "river crop with increased spatial clarity; restrained mist; cool Huế grade; subtle lower atmospheric density"),
        ("02-citadel-backdrop.webp", scene_citadel_v4(masters["A01"]), ["A01"], "frontal architectural establishing crop; improved stone/roof readability; restrained imperial warmth"),
        ("03-ngo-mon-threshold.webp", scene_threshold_v4(masters["A01"]), ["A01"], "1600×900 inset architectural portal; narrow edge feather; subtle threshold rules; transparent outer canvas"),
        ("04-imperial-left.webp", scene_split_v4(masters["A01"], "left"), ["A01"], "left architectural door crop with one-edge feather for split-frame choreography"),
        ("05-imperial-right.webp", scene_split_v4(masters["A01"], "right"), ["A01"], "right architectural door crop with one-edge feather for split-frame choreography"),
        ("06-river-transition.webp", scene_river_transition_v4(masters["A03"]), ["A03"], "full-frame Trường Tiền river-crossing scene; unified cool grade; River Line navigation signature; no pasted-photo band"),
        ("07-beyond-walls.webp", scene_beyond_v4(masters["A04"], masters["A05"]), ["A04", "A05"], "editorial diptych on dark field: Khải Định heritage panel + Đông Ba living-city panel; no diagonal double exposure"),
    ]

    generated = []
    scene_paths: list[Path] = []
    for filename, img, sources, changes in outputs:
        path = builder.SCENE_DIR / filename
        builder.save_webp(img, path)
        scene_paths.append(path)
        generated.append({
            "path": str(path.relative_to(builder.OUT)),
            "sources": sources,
            "changes": changes,
            "size": list(img.size),
            "mode": img.mode,
            "sha256": builder.sha256(path),
        })

    card_specs = [
        ("ngo-mon.webp", "A01", (0.50, 0.55)),
        ("perfume-river.webp", "A02", (0.50, 0.50)),
        ("truong-tien.webp", "A03", (0.50, 0.52)),
        ("khai-dinh.webp", "A04", (0.50, 0.55)),
        ("dong-ba.webp", "A05", (0.55, 0.52)),
    ]
    for filename, sid, focus in card_specs:
        img = builder.card_crop(masters[sid], focus)
        path = builder.CARD_DIR / filename
        builder.save_webp(img, path, quality=85)
        generated.append({
            "path": str(path.relative_to(builder.OUT)),
            "sources": [sid],
            "changes": "960×640 editorial card crop; unified Huế grade",
            "size": list(img.size),
            "mode": img.mode,
            "sha256": builder.sha256(path),
        })

    builder.write_markers()
    for marker in sorted(builder.MARKER_DIR.glob("*.svg")):
        generated.append({
            "path": str(marker.relative_to(builder.OUT)),
            "sources": ["ORIGINAL_PROJECT_GRAPHIC"],
            "changes": "original geometric SVG marker; no third-party raster source",
            "size": [96, 96],
            "mode": "SVG",
            "sha256": builder.sha256(marker),
        })

    contact_sheet_v4(scene_paths)
    preview = builder.PREVIEW_DIR / "scene-contact-sheet.webp"
    generated.append({
        "path": str(preview.relative_to(builder.OUT)),
        "sources": ["DERIVED_SCENES"],
        "changes": "visual-veto contact sheet of seven scene outputs plus combined split-pair preview",
        "size": list(Image.open(preview).size),
        "mode": "RGB",
        "sha256": builder.sha256(preview),
    })

    builder.write_credits(builder.SOURCES, generated)
    manifest = {
        "project": "HUẾ — Between River & Citadel",
        "source_policy": "Wikimedia Commons provenance; no Mostar scene media",
        "visual_veto_revision": "v4",
        "canvas": list(builder.CANVAS),
        "sources": source_manifest,
        "generated": generated,
    }
    (builder.OUT / "asset-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    scene_files = sorted(builder.SCENE_DIR.glob("*.webp"))
    if len(scene_files) != 7:
        raise SystemExit(f"Expected 7 scene WebPs, found {len(scene_files)}")
    for path in scene_files:
        img = Image.open(path)
        if img.size != builder.CANVAS:
            raise SystemExit(f"Scene has wrong dimensions: {path} {img.size}")
        if path.name in {"03-ngo-mon-threshold.webp", "04-imperial-left.webp", "05-imperial-right.webp"} and "A" not in img.getbands():
            raise SystemExit(f"Expected alpha channel for layered scene: {path}")
    if len(list(builder.MARKER_DIR.glob("*.svg"))) != 3:
        raise SystemExit("Expected 3 local SVG markers")

    total = sum(p.stat().st_size for p in builder.OUT.rglob("*") if p.is_file())
    print(f"Built {len(scene_files)} scenes, {len(card_specs)} cards, 3 SVG markers")
    print(f"Huế asset family total: {total / (1024 * 1024):.2f} MiB")
    print("Visual-veto revision: v4")
    return 0


raise SystemExit(main_v4())
