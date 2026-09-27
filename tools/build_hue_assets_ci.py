#!/usr/bin/env python3
"""Stable CI entrypoint for Huế asset production.

This wrapper owns production-source overrides and the visual-veto refinements.
The base builder stays framework-agnostic; this file pins stable Wikimedia
originals, fixes preview compositing for alpha scenes, and applies the approved
Huế editorial composition rules before the UI is wired.
"""

from pathlib import Path
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
        "note": "Selected after visual veto because the previous close gate crop did not read strongly enough as the project signature.",
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
        "note": "Re-selected during visual veto to remove traffic-heavy literal imagery and strengthen the river-as-spine art direction.",
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
# Visual-veto v3 compositions
# ---------------------------------------------------------------------------

def scene_river_transition_v3(river: Image.Image, bridge: Image.Image) -> Image.Image:
    """River chapter with one clean panoramic bridge band; no double exposure."""
    base = builder.cover(river, builder.CANVAS, focus=(0.50, 0.50))
    base = builder.grade(
        base,
        saturation=0.64,
        contrast=0.90,
        brightness=0.78,
        tint=(18, 54, 52, 32),
    )
    base = Image.alpha_composite(
        base,
        builder.vertical_gradient(builder.CANVAS, (6, 14, 13, 14), (6, 14, 13, 126)),
    )

    # Treat Trường Tiền as an editorial panoramic strip rather than a ghosted overlay.
    band_h = 410
    bridge_band = builder.cover(bridge, (1920, band_h), focus=(0.50, 0.52))
    bridge_band = builder.grade(
        bridge_band,
        saturation=0.58,
        contrast=1.02,
        brightness=0.74,
        tint=(20, 50, 48, 20),
    )

    alpha = Image.new("L", (1920, band_h), 232)
    ap = alpha.load()
    feather = 28
    for y in range(band_h):
        edge = min(y, band_h - 1 - y)
        if edge < feather:
            value = round(232 * (edge / feather))
            for x in range(1920):
                ap[x, y] = value
    bridge_band.putalpha(alpha)

    panel = Image.new("RGBA", builder.CANVAS, (0, 0, 0, 0))
    panel.alpha_composite(bridge_band, (0, 315))
    merged = Image.alpha_composite(base, panel)

    # River Line signature sits outside the photo band so it reads as navigation language.
    line = Image.new("RGBA", builder.CANVAS, (0, 0, 0, 0))
    ld = ImageDraw.Draw(line)
    points = [(96, 785), (520, 768), (930, 748), (1360, 724), (1824, 710)]
    ld.line(points, fill=(211, 177, 101, 138), width=2)
    for x, y in (points[1], points[2], points[3]):
        ld.ellipse((x - 5, y - 5, x + 5, y + 5), fill=(239, 228, 201, 205))
    return Image.alpha_composite(merged, line)


def scene_beyond_v2(khai: Image.Image, market: Image.Image) -> Image.Image:
    """Clean editorial contrast: royal landscape vs living city, no muddy overlay."""
    left = builder.cover(khai, builder.CANVAS, focus=(0.46, 0.56))
    right = builder.cover(market, builder.CANVAS, focus=(0.61, 0.50))
    left = builder.grade(
        left,
        saturation=0.68,
        contrast=1.02,
        brightness=0.80,
        tint=(34, 35, 30, 18),
    )
    right = builder.grade(
        right,
        saturation=0.90,
        contrast=1.00,
        brightness=0.78,
        tint=(66, 26, 22, 14),
    )

    mask = Image.new("L", builder.CANVAS, 0)
    md = ImageDraw.Draw(mask)
    md.polygon([(1230, 0), (1920, 0), (1920, 1080), (1040, 1080)], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(5))
    right.putalpha(mask)
    merged = Image.alpha_composite(left, right)

    divider = Image.new("RGBA", builder.CANVAS, (0, 0, 0, 0))
    dd = ImageDraw.Draw(divider)
    dd.line((1230, 0, 1040, 1080), fill=(211, 177, 101, 112), width=2)
    merged = Image.alpha_composite(merged, divider)
    return Image.alpha_composite(
        merged,
        builder.vertical_gradient(builder.CANVAS, (5, 10, 9, 8), (5, 10, 9, 120)),
    )


def contact_sheet_v2(scene_paths: list[Path]) -> None:
    """Composite alpha scenes over the actual dark art-direction surface."""
    tile_w, tile_h = 480, 270
    gap = 24
    cols = 2
    rows = math.ceil(len(scene_paths) / cols)
    bg = (10, 17, 16)
    sheet = Image.new(
        "RGB",
        (cols * tile_w + (cols + 1) * gap, rows * (tile_h + 44) + (rows + 1) * gap),
        bg,
    )
    d = ImageDraw.Draw(sheet)
    f = builder.font(18)

    for i, path in enumerate(scene_paths):
        img = Image.open(path).convert("RGBA")
        dark = Image.new("RGBA", img.size, (*bg, 255))
        rendered = Image.alpha_composite(dark, img).convert("RGB")
        thumb = builder.cover(rendered, (tile_w, tile_h))
        col, row = i % cols, i // cols
        x = gap + col * (tile_w + gap)
        y = gap + row * (tile_h + 44 + gap)
        sheet.paste(thumb, (x, y))
        d.text((x, y + tile_h + 10), path.name, fill=(239, 231, 211), font=f)

    builder.save_webp(sheet, builder.PREVIEW_DIR / "scene-contact-sheet.webp", quality=84)


builder.scene_river_transition = scene_river_transition_v3
builder.scene_beyond = scene_beyond_v2
builder.contact_sheet = contact_sheet_v2

raise SystemExit(builder.main())
