# HUẾ — Asset Replacement Matrix

Status: RESEARCH / SOURCE APPROVAL. No production asset has been wired into the UI yet.

Goal: replace every Mostar-specific visual asset with Huế-specific, provenance-documented media before implementation.

## 1. Replacement policy

Current remote Mostar scene media and remote pin icons are **REMOVE** candidates, not preserve-contract assets.

Implementation rules for the next phase:

1. Do not hotlink the current Figma/CloudFront Mostar assets.
2. Download approved Huế media into `assets/hue/source/` and create optimized derivatives in `assets/hue/scenes/`.
3. Add `assets/hue/CREDITS.md` with author, source URL, license and transformation note for every third-party source.
4. Prefer Public Domain / CC0 / CC BY sources for heavily transformed cinematic composites.
5. Use CC BY-SA assets only when the derivative/share-alike implications are intentionally accepted and documented.
6. Do not use official tourism/UNESCO photography as production assets unless the specific item license permits reuse. Official pages are research sources, not automatic asset libraries.

## 2. Existing asset families to retire

From `index.html`:

| Current role | Current class / role | Current subject | Decision |
|---|---|---|---|
| atmospheric background | `.sky-img` | Mostar sky/scene | REMOVE |
| rear layer | `.back-four` | Mostar scene layer | REMOVE |
| rear city layer | `.back-bazaar` | bazaar layer | REMOVE |
| split foreground | `.splitframe-left` | Mostar frame | REMOVE |
| split foreground | `.splitframe-right` | Mostar frame | REMOVE |
| hero landmark | `.bridge-img` | Stari Most | REMOVE |
| transition scene | `.frame-two-img` | Mostar frame two | REMOVE |
| sight markers | `.sight-pin` × 3 URLs | remote pin illustrations | REMOVE |

The motion roles may survive, but the visual media must not.

## 3. Approved source candidates

These are source candidates for the next asset-production phase. Final scene files should be local derivatives, not remote embeds.

### A01 — Ngọ Môn / Imperial threshold

Source:
https://commons.wikimedia.org/wiki/File:Ngo_Mon_Gate_for_entry_to_the_Imperial_Citadel,_Hue_(31654316702).jpg

Author: shankar s.
License: CC BY 2.0
Resolution: 6000 × 4000

Proposed use:
- main architectural threshold;
- isolate/grade into a central cinematic cutout;
- derive architectural left/right frame fragments from the same source only if attribution notes disclose the transformation.

Why selected:
- strong frontal/architectural read;
- high resolution;
- attribution-only license permits adaptation with credit.

### A02 — Perfume River atmosphere

Source:
https://commons.wikimedia.org/wiki/File:Riviere_des_Parfums_Hue.jpg

Author: Lưu Ly
License: Public Domain
Resolution: 1936 × 1288

Proposed use:
- atmospheric river background;
- color/texture source for river/mist grading;
- optional low-detail blur layer.

Why selected:
- public-domain reuse flexibility;
- directly supports river-as-spine concept.

### A03 — Trường Tiền / river crossing

Source:
https://commons.wikimedia.org/wiki/File:Truong_Tien_Bridge.jpg

Author: Lưu Ly
License: Public Domain
Current file: 985 × 658; historical versions include wider source crops.

Proposed use:
- river chapter / connective line;
- bridge should remain secondary to river narrative, not become a new Stari Most replacement hero.

Why selected:
- public-domain;
- reflection and long horizontal geometry suit editorial/panoramic treatment.

### A04 — Khải Định Tomb

Source:
https://commons.wikimedia.org/wiki/File:Khai_Dinh_tomb_Hue_(27767136409).jpg

Author: dronepicr
License: CC BY 2.0
Resolution: 6000 × 4000

Proposed use:
- `Beyond the Walls` scene or sights slider;
- high-detail crop for material contrast against the flatter Citadel/river scenes.

Why selected:
- very high resolution;
- attribution-only license;
- materially different texture and massing from Ngọ Môn.

### A05 — Đông Ba Market / living city

Source:
https://commons.wikimedia.org/wiki/File:Dong_Ba_market,_Thành_phố_Huế,_Vietnam_(Unsplash).jpg

Author: Alice Young
License: CC0 1.0
Resolution: 6037 × 4025

Proposed use:
- living-city card / route editorial image;
- close crop of market material/colour rather than a generic tourism establishing shot.

Why selected:
- CC0;
- keeps the project from becoming only palaces/tombs;
- high resolution.

### A06 — Thiên Mụ Pagoda

Source:
https://commons.wikimedia.org/wiki/File:Thien_Mu_Pagoda.jpg

Author: AJ Oswald
License: CC BY-SA 2.0
Resolution: 1200 × 1600

Proposed use:
- sights slider/card reference;
- avoid heavy derivative composite unless share-alike handling is explicitly accepted.

Why selected:
- vertical silhouette gives a different card rhythm;
- strong recognition at small size.

### A07 — Minh Mạng Tomb

Source:
https://commons.wikimedia.org/wiki/File:Minh_Mang_Tomb,_Hué_(31448961557).jpg

Author: Isabell Schulz
License: CC BY-SA 2.0
Resolution: 5472 × 3648

Proposed use:
- route/editorial card or background reference;
- not preferred for heavily composited hero scene unless share-alike derivative handling is accepted.

### A08 — Additional Ngọ Môn panorama

Source:
https://commons.wikimedia.org/wiki/File:Ngo_Mon.jpg

Author: Lưu Ly
License: CC BY-SA 3.0
Resolution: 8611 × 2840

Proposed use:
- panoramic layout reference;
- optional backup for wide architectural crop.

## 4. Production asset plan

The implementation should create a new local media family rather than preserve the old seven-file mapping mechanically.

Proposed target tree:

```text
assets/
└── hue/
    ├── CREDITS.md
    ├── source/
    │   ├── ngo-mon.jpg
    │   ├── perfume-river.jpg
    │   ├── truong-tien.jpg
    │   ├── khai-dinh.jpg
    │   └── dong-ba.jpg
    ├── scenes/
    │   ├── 01-river-atmosphere.webp
    │   ├── 02-citadel-backdrop.webp
    │   ├── 03-ngo-mon-threshold.webp
    │   ├── 04-imperial-left.webp
    │   ├── 05-imperial-right.webp
    │   ├── 06-river-transition.webp
    │   └── 07-beyond-walls.webp
    └── cards/
        ├── ngo-mon.webp
        ├── thien-mu.webp
        ├── truong-tien.webp
        ├── khai-dinh.webp
        ├── minh-mang.webp
        └── dong-ba.webp
```

The exact seven scene outputs may change after first rendered composition tests. What is fixed is that the Mostar scene assets do not survive the transformation.

## 5. Scene-role mapping

| New scene role | Visual subject | Treatment | Motion role |
|---|---|---|---|
| 01 River atmosphere | Perfume River / mist | broad low-contrast background, desaturated | initial world / depth base |
| 02 Citadel backdrop | walls / roofline / flag-axis context | wide horizontal crop | rear architectural layer |
| 03 Imperial threshold | Ngọ Môn | isolated central architecture | primary threshold reveal |
| 04 Threshold left | Ngọ Môn / wall detail | masked architectural crop | split-frame left |
| 05 Threshold right | complementary gate/courtyard detail | masked crop | split-frame right |
| 06 River transition | Trường Tiền / river reflection | long horizontal band, lower contrast | second narrative transition |
| 07 Beyond walls | Khải Định / tomb texture / garden | editorial macro or layered composite | late transition into sights |

Important: Trường Tiền is a connective element, not the single symbolic hero. This avoids recreating the Mostar "one bridge = city" composition.

## 6. Graphic-marker replacement

Retire the three current remote pin PNGs.

Do not introduce another generic map-pin icon set.

Proposed marker system:

- small geometric `river node` circles;
- one line + index number (`01`, `02`, `03`…);
- optional five-colour micro-accent based on the project palette;
- CSS/SVG authored locally, not remote raster icons.

This makes the slider feel like part of the Huế visual system rather than a tourism map widget.

## 7. Attribution policy

`assets/hue/CREDITS.md` should include, for every production source:

```text
Asset ID
Local derivative filename
Original title
Author
Original source URL
License
License URL
Changes made (crop / color grade / mask / composite / resize)
```

For CC BY material, attribution is mandatory.
For CC BY-SA material, derivative/share-alike obligations must be preserved where applicable.
For Public Domain / CC0 material, credit is still recommended for portfolio transparency even when not legally required.

## 8. Approval state

APPROVED FOR NEXT PHASE:

- A01 Ngọ Môn (CC BY 2.0)
- A02 Perfume River (Public Domain)
- A03 Trường Tiền (Public Domain)
- A04 Khải Định (CC BY 2.0)
- A05 Đông Ba (CC0)

CONDITIONAL / CARD-LEVEL USE:

- A06 Thiên Mụ (CC BY-SA 2.0)
- A07 Minh Mạng (CC BY-SA 2.0)
- A08 Ngọ Môn panorama (CC BY-SA 3.0)

BLOCKED:

- none at research phase.

NEXT PHASE:

- download approved source files;
- create local derivatives and transparent/optimized scene composites;
- create local SVG marker system;
- verify crop/focal quality at 390 / 768 / 1440 before wiring final choreography.