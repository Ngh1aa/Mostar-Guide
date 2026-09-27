# HUẾ — Production Asset Credits

These local assets were prepared for the independent portfolio concept **HUẾ — Between River & Citadel**.
They are not official Huế tourism or heritage-centre assets.

## Source policy

- Wikimedia Commons file pages are the provenance source of truth.
- CC BY assets retain attribution and a license link below.
- Public Domain / CC0 assets are still credited for portfolio transparency.
- Local source masters are normalized/resized derivatives, not untouched originals.
- No Mostar Figma/CloudFront scene media is used in these Huế production assets.

## Source assets

### A01 — The grand entrance complex to the Imperial Citadel (31801617815).jpg

- **Local source master:** `source/ngo-mon.jpg`
- **Author:** shankar s.
- **Source:** https://commons.wikimedia.org/wiki/File:The_grand_entrance_complex_to_the_Imperial_Citadel_(31801617815).jpg
- **License:** CC BY 2.0
- **License URL:** https://creativecommons.org/licenses/by/2.0/
- **Role:** Imperial Threshold / frontal Ngọ Môn grand-entrance composition
- **Changes to local master:** downloaded from Wikimedia, EXIF-orientation normalized, resized to max 2560 px if needed, re-encoded as optimized progressive JPEG, metadata stripped.
- **Selection note:** Selected after visual veto because the earlier close gate crop did not read strongly enough as the project signature.

### A02 — Riviere des Parfums Hue.jpg

- **Local source master:** `source/perfume-river.jpg`
- **Author:** Lưu Ly
- **Source:** https://commons.wikimedia.org/wiki/File:Riviere_des_Parfums_Hue.jpg
- **License:** Public Domain
- **License URL:** https://commons.wikimedia.org/wiki/File:Riviere_des_Parfums_Hue.jpg
- **Role:** Perfume River atmosphere / depth base
- **Changes to local master:** downloaded from Wikimedia, EXIF-orientation normalized, resized to max 2560 px if needed, re-encoded as optimized progressive JPEG, metadata stripped.

### A03 — Truong Tien Bridge.jpg

- **Local source master:** `source/truong-tien.jpg`
- **Author:** Lưu Ly
- **Source:** https://commons.wikimedia.org/wiki/File:Truong_Tien_Bridge.jpg
- **License:** Public Domain
- **License URL:** https://commons.wikimedia.org/wiki/File:Truong_Tien_Bridge.jpg
- **Role:** River crossing / reflection / horizontal connective geometry
- **Changes to local master:** downloaded from Wikimedia, EXIF-orientation normalized, resized to max 2560 px if needed, re-encoded as optimized progressive JPEG, metadata stripped.
- **Selection note:** Selected for a full-frame river transition rather than a ghosted bridge composite.

### A04 — Khai Dinh tomb Hue (27767136409).jpg

- **Local source master:** `source/khai-dinh.jpg`
- **Author:** dronepicr
- **Source:** https://commons.wikimedia.org/wiki/File:Khai_Dinh_tomb_Hue_(27767136409).jpg
- **License:** CC BY 2.0
- **License URL:** https://creativecommons.org/licenses/by/2.0/
- **Role:** Beyond the Walls / royal landscape texture
- **Changes to local master:** downloaded from Wikimedia, EXIF-orientation normalized, resized to max 2560 px if needed, re-encoded as optimized progressive JPEG, metadata stripped.

### A05 — Dong Ba market, Thành phố Huế, Vietnam (Unsplash).jpg

- **Local source master:** `source/dong-ba.jpg`
- **Author:** Alice Young
- **Source:** https://commons.wikimedia.org/wiki/File:Dong_Ba_market,_Th%C3%A0nh_ph%E1%BB%91_Hu%E1%BA%BF,_Vietnam_(Unsplash).jpg
- **License:** CC0 1.0
- **License URL:** https://creativecommons.org/publicdomain/zero/1.0/
- **Role:** Living city / market colour and texture
- **Changes to local master:** downloaded from Wikimedia, EXIF-orientation normalized, resized to max 2560 px if needed, re-encoded as optimized progressive JPEG, metadata stripped.

## Generated derivatives

### `scenes/01-river-atmosphere.webp`

- **Source IDs:** A02
- **Transformation:** river crop with increased spatial clarity; restrained mist; cool Huế grade; subtle lower atmospheric density
- **Output:** 1920 × 1080 · RGBA

### `scenes/02-citadel-backdrop.webp`

- **Source IDs:** A01
- **Transformation:** frontal architectural establishing crop; improved stone/roof readability; restrained imperial warmth
- **Output:** 1920 × 1080 · RGBA

### `scenes/03-ngo-mon-threshold.webp`

- **Source IDs:** A01
- **Transformation:** 1600×900 inset architectural portal; narrow edge feather; subtle threshold rules; transparent outer canvas
- **Output:** 1920 × 1080 · RGBA

### `scenes/04-imperial-left.webp`

- **Source IDs:** A01
- **Transformation:** registered left half of one shared Ngọ Môn full-frame crop; centre-edge feather only; reconstructs a single scene with 05 before split motion
- **Output:** 1920 × 1080 · RGBA

### `scenes/05-imperial-right.webp`

- **Source IDs:** A01
- **Transformation:** registered right half of one shared Ngọ Môn full-frame crop; centre-edge feather only; reconstructs a single scene with 04 before split motion
- **Output:** 1920 × 1080 · RGBA

### `scenes/06-river-transition.webp`

- **Source IDs:** A03
- **Transformation:** full-frame Trường Tiền river-crossing scene; unified cool grade; River Line navigation signature; no pasted-photo band
- **Output:** 1920 × 1080 · RGBA

### `scenes/07-beyond-walls.webp`

- **Source IDs:** A04, A05
- **Transformation:** editorial diptych on dark field: Khải Định heritage panel + Đông Ba living-city panel; no diagonal double exposure
- **Output:** 1920 × 1080 · RGBA

### `cards/ngo-mon.webp`

- **Source IDs:** A01
- **Transformation:** 960×640 editorial card crop; unified Huế grade
- **Output:** 960 × 640 · RGB

### `cards/perfume-river.webp`

- **Source IDs:** A02
- **Transformation:** 960×640 editorial card crop; unified Huế grade
- **Output:** 960 × 640 · RGB

### `cards/truong-tien.webp`

- **Source IDs:** A03
- **Transformation:** 960×640 editorial card crop; unified Huế grade
- **Output:** 960 × 640 · RGB

### `cards/khai-dinh.webp`

- **Source IDs:** A04
- **Transformation:** 960×640 editorial card crop; unified Huế grade
- **Output:** 960 × 640 · RGB

### `cards/dong-ba.webp`

- **Source IDs:** A05
- **Transformation:** 960×640 editorial card crop; unified Huế grade
- **Output:** 960 × 640 · RGB

### `markers/imperial-node.svg`

- **Source IDs:** ORIGINAL_PROJECT_GRAPHIC
- **Transformation:** original geometric SVG marker; no third-party raster source
- **Output:** 96 × 96 · SVG

### `markers/legacy-node.svg`

- **Source IDs:** ORIGINAL_PROJECT_GRAPHIC
- **Transformation:** original geometric SVG marker; no third-party raster source
- **Output:** 96 × 96 · SVG

### `markers/river-node.svg`

- **Source IDs:** ORIGINAL_PROJECT_GRAPHIC
- **Transformation:** original geometric SVG marker; no third-party raster source
- **Output:** 96 × 96 · SVG

### `previews/scene-contact-sheet.webp`

- **Source IDs:** DERIVED_SCENES
- **Transformation:** visual-veto contact sheet of seven scene outputs plus aligned 04+05 split-pair preview
- **Output:** 1032 × 1376 · RGB

## Local SVG marker system

`markers/river-node.svg`, `markers/imperial-node.svg`, and `markers/legacy-node.svg` are original project graphics authored for this repository. They use simple geometric forms, a river-line motif, and numeric indexing rather than a generic tourism-map pin.

## License reminder

The repository's own code/content license does not override third-party media licenses. Reusers must follow the licenses above for source-derived media.
