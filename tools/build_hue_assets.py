#!/usr/bin/env python3
"""Build local Huế production assets from provenance-documented Wikimedia sources.

This script intentionally does NOT modify application HTML/CSS/JS. It creates only
assets/hue/** plus CREDITS.md and a machine-readable manifest.
"""

from __future__ import annotations

import hashlib
import io
import json
import math
from pathlib import Path
from textwrap import dedent

import requests
from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "hue"
SOURCE_DIR = OUT / "source"
SCENE_DIR = OUT / "scenes"
CARD_DIR = OUT / "cards"
MARKER_DIR = OUT / "markers"
PREVIEW_DIR = OUT / "previews"

CANVAS = (1920, 1080)
CARD = (960, 640)
USER_AGENT = "Mostar-Guide-Hue-Asset-Builder/1.0 (+https://github.com/Ngh1aa/Mostar-Guide)"

SOURCES = {
    "A01": {
        "slug": "ngo-mon",
        "title": "Ngo Mon Gate for entry to the Imperial Citadel, Hue (31654316702).jpg",
        "author": "shankar s.",
        "license": "CC BY 2.0",
        "license_url": "https://creativecommons.org/licenses/by/2.0/",
        "page_url": "https://commons.wikimedia.org/wiki/File:Ngo_Mon_Gate_for_entry_to_the_Imperial_Citadel,_Hue_(31654316702).jpg",
        "download_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Ngo_Mon_Gate_for_entry_to_the_Imperial_Citadel%2C_Hue_%2831654316702%29.jpg/2560px-Ngo_Mon_Gate_for_entry_to_the_Imperial_Citadel%2C_Hue_%2831654316702%29.jpg",
        "role": "Imperial threshold / Ngọ Môn architecture",
    },
    "A02": {
        "slug": "perfume-river",
        "title": "Riviere des Parfums Hue.jpg",
        "author": "Lưu Ly",
        "license": "Public Domain",
        "license_url": "https://commons.wikimedia.org/wiki/File:Riviere_des_Parfums_Hue.jpg",
        "page_url": "https://commons.wikimedia.org/wiki/File:Riviere_des_Parfums_Hue.jpg",
        "download_url": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Riviere_des_Parfums_Hue.jpg",
        "role": "Perfume River atmosphere / depth base",
    },
    "A03": {
        "slug": "truong-tien",
        "title": "Truong Tien bridge.jpg",
        "author": "Margrethe Store",
        "license": "CC BY 2.0",
        "license_url": "https://creativecommons.org/licenses/by/2.0/",
        "page_url": "https://commons.wikimedia.org/wiki/File:Truong_Tien_bridge.jpg",
        "download_url": "https://upload.wikimedia.org/wikipedia/commons/7/77/Truong_Tien_bridge.jpg",
        "role": "River crossing / transition geometry",
        "note": "Higher-resolution CC BY source selected over the lower-resolution Public Domain candidate for production quality.",
    },
    "A04": {
        "slug": "khai-dinh",
        "title": "Khai Dinh tomb Hue (27767136409).jpg",
        "author": "dronepicr",
        "license": "CC BY 2.0",
        "license_url": "https://creativecommons.org/licenses/by/2.0/",
        "page_url": "https://commons.wikimedia.org/wiki/File:Khai_Dinh_tomb_Hue_(27767136409).jpg",
        "download_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Khai_Dinh_tomb_Hue_%2827767136409%29.jpg/2560px-Khai_Dinh_tomb_Hue_%2827767136409%29.jpg",
        "role": "Beyond the Walls / royal landscape texture",
    },
    "A05": {
        "slug": "dong-ba",
        "title": "Dong Ba market, Thành phố Huế, Vietnam (Unsplash).jpg",
        "author": "Alice Young",
        "license": "CC0 1.0",
        "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
        "page_url": "https://commons.wikimedia.org/wiki/File:Dong_Ba_market,_Th%C3%A0nh_ph%E1%BB%91_Hu%E1%BA%BF,_Vietnam_(Unsplash).jpg",
        "download_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Dong_Ba_market%2C_Th%C3%A0nh_ph%E1%BB%91_Hu%E1%BA%BF%2C_Vietnam_%28Unsplash%29.jpg/2560px-Dong_Ba_market%2C_Th%C3%A0nh_ph%E1%BB%91_Hu%E1%BA%BF%2C_Vietnam_%28Unsplash%29.jpg",
        "role": "Living city / market colour and texture",
    },
}


def ensure_dirs() -> None:
    for d in (SOURCE_DIR, SCENE_DIR, CARD_DIR, MARKER_DIR, PREVIEW_DIR):
        d.mkdir(parents=True, exist_ok=True)


def download_image(meta: dict) -> Image.Image:
    response = requests.get(meta["download_url"], headers={"User-Agent": USER_AGENT}, timeout=90)
    response.raise_for_status()
    img = Image.open(io.BytesIO(response.content))
    img = ImageOps.exif_transpose(img).convert("RGB")
    # Normalize local masters to keep the repository light while preserving enough detail.
    max_dim = 2560
    if max(img.size) > max_dim:
        ratio = max_dim / max(img.size)
        img = img.resize((round(img.width * ratio), round(img.height * ratio)), Image.Resampling.LANCZOS)
    return img


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def save_jpeg(img: Image.Image, path: Path, quality: int = 90) -> None:
    img.convert("RGB").save(path, "JPEG", quality=quality, optimize=True, progressive=True)


def save_webp(img: Image.Image, path: Path, quality: int = 84) -> None:
    img.save(path, "WEBP", quality=quality, method=6, lossless=False)


def cover(img: Image.Image, size: tuple[int, int], focus=(0.5, 0.5)) -> Image.Image:
    tw, th = size
    scale = max(tw / img.width, th / img.height)
    nw, nh = math.ceil(img.width * scale), math.ceil(img.height * scale)
    resized = img.resize((nw, nh), Image.Resampling.LANCZOS)
    fx, fy = focus
    left = int((nw - tw) * fx)
    top = int((nh - th) * fy)
    left = max(0, min(left, nw - tw))
    top = max(0, min(top, nh - th))
    return resized.crop((left, top, left + tw, top + th))


def grade(img: Image.Image, saturation=0.82, contrast=0.94, brightness=0.94, tint=(27, 56, 51, 28)) -> Image.Image:
    out = ImageEnhance.Color(img.convert("RGB")).enhance(saturation)
    out = ImageEnhance.Contrast(out).enhance(contrast)
    out = ImageEnhance.Brightness(out).enhance(brightness).convert("RGBA")
    overlay = Image.new("RGBA", out.size, tint)
    return Image.alpha_composite(out, overlay)


def vertical_gradient(size: tuple[int, int], top=(8, 19, 18, 0), bottom=(8, 19, 18, 150)) -> Image.Image:
    w, h = size
    gradient = Image.new("RGBA", size)
    px = gradient.load()
    for y in range(h):
        t = y / max(1, h - 1)
        c = tuple(round(top[i] + (bottom[i] - top[i]) * t) for i in range(4))
        for x in range(w):
            px[x, y] = c
    return gradient


def horizontal_alpha_mask(size: tuple[int, int], fade_left=0.0, fade_right=0.0, feather=96) -> Image.Image:
    w, h = size
    mask = Image.new("L", size, 255)
    p = mask.load()
    left_edge = int(w * fade_left)
    right_edge = int(w * (1 - fade_right))
    for x in range(w):
        alpha = 255
        if fade_left and x < left_edge + feather:
            alpha = min(alpha, int(255 * max(0, x - left_edge) / feather))
        if fade_right and x > right_edge - feather:
            alpha = min(alpha, int(255 * max(0, right_edge - x) / feather))
        alpha = max(0, min(255, alpha))
        for y in range(h):
            p[x, y] = alpha
    return mask.filter(ImageFilter.GaussianBlur(18))


def soft_window_mask(size: tuple[int, int], margin=(130, 80, 130, 60), blur=70) -> Image.Image:
    w, h = size
    mask = Image.new("L", size, 0)
    d = ImageDraw.Draw(mask)
    l, t, r, b = margin
    d.rounded_rectangle((l, t, w - r, h - b), radius=50, fill=255)
    return mask.filter(ImageFilter.GaussianBlur(blur))


def scene_river(img: Image.Image) -> Image.Image:
    base = cover(img, CANVAS, focus=(0.50, 0.50))
    base = base.filter(ImageFilter.GaussianBlur(2.0))
    base = grade(base, saturation=0.72, contrast=0.86, brightness=0.90, tint=(19, 52, 48, 34))
    mist = Image.new("RGBA", CANVAS, (235, 228, 205, 0))
    md = ImageDraw.Draw(mist)
    md.rectangle((0, 0, 1920, 380), fill=(232, 229, 209, 34))
    mist = mist.filter(ImageFilter.GaussianBlur(80))
    base = Image.alpha_composite(base, mist)
    return Image.alpha_composite(base, vertical_gradient(CANVAS, (7, 18, 17, 0), (7, 18, 17, 95)))


def scene_citadel(img: Image.Image) -> Image.Image:
    base = cover(img, CANVAS, focus=(0.50, 0.58))
    base = grade(base, saturation=0.78, contrast=0.90, brightness=0.80, tint=(77, 27, 20, 18))
    return Image.alpha_composite(base, vertical_gradient(CANVAS, (12, 17, 16, 35), (8, 14, 13, 120)))


def scene_threshold(img: Image.Image) -> Image.Image:
    base = cover(img, CANVAS, focus=(0.50, 0.62))
    base = grade(base, saturation=0.90, contrast=1.06, brightness=0.92, tint=(78, 24, 17, 14))
    alpha = soft_window_mask(CANVAS, margin=(220, 125, 220, 55), blur=60)
    base.putalpha(alpha)
    return base


def scene_split(img: Image.Image, side: str) -> Image.Image:
    full = cover(img, CANVAS, focus=(0.40 if side == "left" else 0.60, 0.62))
    full = grade(full, saturation=0.82, contrast=1.00, brightness=0.86, tint=(57, 24, 20, 14))
    if side == "left":
        mask = horizontal_alpha_mask(CANVAS, fade_left=0.0, fade_right=0.47, feather=260)
        # Remove much of the right half so the two assets can split apart during motion.
        wipe = Image.new("L", CANVAS, 0)
        wd = ImageDraw.Draw(wipe)
        wd.rectangle((0, 0, 1220, 1080), fill=255)
        wipe = wipe.filter(ImageFilter.GaussianBlur(90))
    else:
        mask = horizontal_alpha_mask(CANVAS, fade_left=0.47, fade_right=0.0, feather=260)
        wipe = Image.new("L", CANVAS, 0)
        wd = ImageDraw.Draw(wipe)
        wd.rectangle((700, 0, 1920, 1080), fill=255)
        wipe = wipe.filter(ImageFilter.GaussianBlur(90))
    mask = ImageChops.multiply(mask, wipe)
    full.putalpha(mask)
    return full


def scene_river_transition(river: Image.Image, bridge: Image.Image) -> Image.Image:
    base = scene_river(river)
    br = cover(bridge, CANVAS, focus=(0.48, 0.45))
    br = grade(br, saturation=0.60, contrast=0.90, brightness=0.78, tint=(23, 59, 58, 22))
    alpha = Image.new("L", CANVAS, 0)
    d = ImageDraw.Draw(alpha)
    d.rectangle((0, 315, 1920, 980), fill=198)
    alpha = alpha.filter(ImageFilter.GaussianBlur(115))
    br.putalpha(alpha)
    merged = Image.alpha_composite(base, br)
    river_line = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    ld = ImageDraw.Draw(river_line)
    ld.line((100, 760, 1820, 685), fill=(211, 177, 101, 105), width=3)
    ld.ellipse((940, 700, 962, 722), fill=(239, 228, 201, 210))
    return Image.alpha_composite(merged, river_line)


def scene_beyond(khai: Image.Image, market: Image.Image) -> Image.Image:
    left = cover(khai, CANVAS, focus=(0.48, 0.56))
    right = cover(market, CANVAS, focus=(0.58, 0.52))
    left = grade(left, saturation=0.72, contrast=1.00, brightness=0.80, tint=(40, 38, 31, 20))
    right = grade(right, saturation=0.92, contrast=0.98, brightness=0.72, tint=(74, 27, 20, 18))
    mask = Image.new("L", CANVAS, 0)
    md = ImageDraw.Draw(mask)
    md.polygon([(1010, -100), (1920, -100), (1920, 1180), (790, 1180)], fill=220)
    mask = mask.filter(ImageFilter.GaussianBlur(120))
    right.putalpha(mask)
    merged = Image.alpha_composite(left, right)
    return Image.alpha_composite(merged, vertical_gradient(CANVAS, (5, 10, 9, 20), (5, 10, 9, 135)))


def card_crop(img: Image.Image, focus=(0.5, 0.5)) -> Image.Image:
    out = cover(img, CARD, focus=focus)
    return grade(out, saturation=0.86, contrast=0.98, brightness=0.90, tint=(22, 43, 39, 18)).convert("RGB")


def write_markers() -> None:
    markers = {
        "river-node.svg": ("01", "circle"),
        "imperial-node.svg": ("02", "square"),
        "legacy-node.svg": ("03", "diamond"),
    }
    for filename, (index, shape) in markers.items():
        if shape == "circle":
            glyph = '<circle cx="40" cy="40" r="27" fill="none" stroke="#D3B165" stroke-width="1.5"/><circle cx="40" cy="40" r="4" fill="#D3B165"/>'
        elif shape == "square":
            glyph = '<rect x="17" y="17" width="46" height="46" rx="3" fill="none" stroke="#D3B165" stroke-width="1.5"/><path d="M17 51h46" stroke="#D3B165" stroke-width="1.5"/>'
        else:
            glyph = '<path d="M40 13 67 40 40 67 13 40Z" fill="none" stroke="#D3B165" stroke-width="1.5"/><circle cx="40" cy="40" r="3.5" fill="#D3B165"/>'
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96" role="img" aria-label="Huế route marker {index}">
  <path d="M8 80H88" stroke="#F1E9D6" stroke-opacity=".42"/>
  {glyph}
  <text x="78" y="22" text-anchor="end" fill="#F1E9D6" font-family="Arial, sans-serif" font-size="11" letter-spacing="1">{index}</text>
</svg>'''
        (MARKER_DIR / filename).write_text(svg, encoding="utf-8")


def font(size: int):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        p = Path(candidate)
        if p.exists():
            return ImageFont.truetype(str(p), size=size)
    return ImageFont.load_default()


def contact_sheet(scene_paths: list[Path]) -> None:
    tile_w, tile_h = 480, 270
    gap = 24
    cols = 2
    rows = math.ceil(len(scene_paths) / cols)
    sheet = Image.new("RGB", (cols * tile_w + (cols + 1) * gap, rows * (tile_h + 44) + (rows + 1) * gap), (10, 17, 16))
    d = ImageDraw.Draw(sheet)
    f = font(18)
    for i, path in enumerate(scene_paths):
        img = Image.open(path).convert("RGB")
        thumb = cover(img, (tile_w, tile_h))
        col, row = i % cols, i // cols
        x = gap + col * (tile_w + gap)
        y = gap + row * (tile_h + 44 + gap)
        sheet.paste(thumb, (x, y))
        d.text((x, y + tile_h + 10), path.name, fill=(239, 231, 211), font=f)
    save_webp(sheet, PREVIEW_DIR / "scene-contact-sheet.webp", quality=82)


def write_credits(source_records: dict, generated: list[dict]) -> None:
    lines = [
        "# HUẾ — Production Asset Credits",
        "",
        "These local assets were prepared for the independent portfolio concept **HUẾ — Between River & Citadel**.",
        "They are not official Huế tourism or heritage-centre assets.",
        "",
        "## Source policy",
        "",
        "- Wikimedia Commons file pages are the provenance source of truth.",
        "- CC BY assets retain attribution and a license link below.",
        "- Public Domain / CC0 assets are still credited for portfolio transparency.",
        "- Local source masters are normalized/resized derivatives, not untouched originals.",
        "- No Mostar Figma/CloudFront scene media is used in these Huế production assets.",
        "",
        "## Source assets",
        "",
    ]
    for sid, meta in source_records.items():
        local = f"source/{meta['slug']}.jpg"
        lines += [
            f"### {sid} — {meta['title']}",
            "",
            f"- **Local source master:** `{local}`",
            f"- **Author:** {meta['author']}",
            f"- **Source:** {meta['page_url']}",
            f"- **License:** {meta['license']}",
            f"- **License URL:** {meta['license_url']}",
            f"- **Role:** {meta['role']}",
            "- **Changes to local master:** downloaded from Wikimedia, EXIF-orientation normalized, resized to max 2560 px if needed, re-encoded as optimized progressive JPEG, metadata stripped.",
        ]
        if meta.get("note"):
            lines.append(f"- **Selection note:** {meta['note']}")
        lines.append("")

    lines += ["## Generated derivatives", ""]
    for item in generated:
        lines += [
            f"### `{item['path']}`",
            "",
            f"- **Source IDs:** {', '.join(item['sources'])}",
            f"- **Transformation:** {item['changes']}",
            f"- **Output:** {item['size'][0]} × {item['size'][1]} · {item['mode']}",
            "",
        ]

    lines += [
        "## Local SVG marker system",
        "",
        "`markers/river-node.svg`, `markers/imperial-node.svg`, and `markers/legacy-node.svg` are original project graphics authored for this repository. They use simple geometric forms, a river-line motif, and numeric indexing rather than a generic tourism-map pin.",
        "",
        "## License reminder",
        "",
        "The repository's own code/content license does not override third-party media licenses. Reusers must follow the licenses above for source-derived media.",
        "",
    ]
    (OUT / "CREDITS.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ensure_dirs()
    masters: dict[str, Image.Image] = {}
    source_manifest = {}

    for sid, meta in SOURCES.items():
        img = download_image(meta)
        path = SOURCE_DIR / f"{meta['slug']}.jpg"
        save_jpeg(img, path)
        masters[sid] = Image.open(path).convert("RGB")
        source_manifest[sid] = {
            **meta,
            "local_path": str(path.relative_to(ROOT)),
            "pixels": list(masters[sid].size),
            "sha256": sha256(path),
        }

    outputs = [
        ("01-river-atmosphere.webp", scene_river(masters["A02"]), ["A02"], "cover crop; low-contrast river grade; subtle blur/mist; dark lower gradient"),
        ("02-citadel-backdrop.webp", scene_citadel(masters["A01"]), ["A01"], "wide architectural crop; subdued imperial grade; top/bottom atmospheric density"),
        ("03-ngo-mon-threshold.webp", scene_threshold(masters["A01"]), ["A01"], "central architectural crop; warm grade; soft alpha window for layered threshold reveal"),
        ("04-imperial-left.webp", scene_split(masters["A01"], "left"), ["A01"], "left architectural crop; translucent feather mask for split-frame choreography"),
        ("05-imperial-right.webp", scene_split(masters["A01"], "right"), ["A01"], "right architectural crop; translucent feather mask for split-frame choreography"),
        ("06-river-transition.webp", scene_river_transition(masters["A02"], masters["A03"]), ["A02", "A03"], "Perfume River base + Trường Tiền bridge crossfade band; river-line accent; unified cool grade"),
        ("07-beyond-walls.webp", scene_beyond(masters["A04"], masters["A05"]), ["A04", "A05"], "Khải Định + Đông Ba diagonal soft composite; heritage/living-city contrast; dark cinematic grade"),
    ]

    generated = []
    scene_paths = []
    for filename, img, sources, changes in outputs:
        path = SCENE_DIR / filename
        save_webp(img, path)
        scene_paths.append(path)
        generated.append({
            "path": str(path.relative_to(OUT)),
            "sources": sources,
            "changes": changes,
            "size": list(img.size),
            "mode": img.mode,
            "sha256": sha256(path),
        })

    card_specs = [
        ("ngo-mon.webp", "A01", (0.50, 0.55)),
        ("perfume-river.webp", "A02", (0.50, 0.50)),
        ("truong-tien.webp", "A03", (0.48, 0.45)),
        ("khai-dinh.webp", "A04", (0.50, 0.55)),
        ("dong-ba.webp", "A05", (0.55, 0.52)),
    ]
    for filename, sid, focus in card_specs:
        img = card_crop(masters[sid], focus)
        path = CARD_DIR / filename
        save_webp(img, path, quality=85)
        generated.append({
            "path": str(path.relative_to(OUT)),
            "sources": [sid],
            "changes": "960×640 editorial card crop; unified Huế grade",
            "size": list(img.size),
            "mode": img.mode,
            "sha256": sha256(path),
        })

    write_markers()
    for marker in sorted(MARKER_DIR.glob("*.svg")):
        generated.append({
            "path": str(marker.relative_to(OUT)),
            "sources": ["ORIGINAL_PROJECT_GRAPHIC"],
            "changes": "original geometric SVG marker; no third-party raster source",
            "size": [96, 96],
            "mode": "SVG",
            "sha256": sha256(marker),
        })

    contact_sheet(scene_paths)
    preview = PREVIEW_DIR / "scene-contact-sheet.webp"
    generated.append({
        "path": str(preview.relative_to(OUT)),
        "sources": ["DERIVED_SCENES"],
        "changes": "visual-review contact sheet of all seven generated scene outputs",
        "size": list(Image.open(preview).size),
        "mode": "RGB",
        "sha256": sha256(preview),
    })

    write_credits(SOURCES, generated)

    manifest = {
        "project": "HUẾ — Between River & Citadel",
        "source_policy": "Wikimedia Commons provenance; no Mostar scene media",
        "canvas": list(CANVAS),
        "sources": source_manifest,
        "generated": generated,
    }
    (OUT / "asset-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Binary acceptance checks.
    required = [SCENE_DIR / f"0{i}-" for i in range(1, 8)]
    scene_files = sorted(SCENE_DIR.glob("*.webp"))
    if len(scene_files) != 7:
        raise SystemExit(f"Expected 7 scene WebPs, found {len(scene_files)}")
    for path in scene_files:
        img = Image.open(path)
        if img.size != CANVAS:
            raise SystemExit(f"Scene has wrong dimensions: {path} {img.size}")
        if path.name in {"03-ngo-mon-threshold.webp", "04-imperial-left.webp", "05-imperial-right.webp"} and "A" not in img.getbands():
            raise SystemExit(f"Expected alpha channel for layered scene: {path}")
    if len(list(MARKER_DIR.glob("*.svg"))) != 3:
        raise SystemExit("Expected 3 local SVG markers")

    total = sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
    print(f"Built {len(scene_files)} scenes, {len(card_specs)} cards, 3 SVG markers")
    print(f"Huế asset family total: {total / (1024 * 1024):.2f} MiB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
