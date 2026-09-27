# HUẾ — Between River & Citadel

An independent cinematic cultural-experience prototype about Huế, Việt Nam. The project follows the Perfume River through imperial thresholds, contemporary city life, and the wider royal landscape while preserving a lightweight vanilla HTML/CSS/JavaScript implementation with no bundler or build step.

The repository slug is currently retained for deployment continuity, but the production product identity is **HUẾ — Between River & Citadel**.

## Project structure

```text
.
├── index.html
├── styles.css                 # preserved cinematic mechanics / base styles
├── hue.css                    # Huế art-direction layer
├── script.js                  # preserved scroll + infinite-slider engine
├── routes.html
├── routes.css                 # base routes structure
├── hue-routes.css             # Huế routes art direction
├── routes.js
├── shared/
│   ├── nav.css
│   ├── nav.js
│   └── footer.css
├── assets/
│   ├── favicon.svg
│   └── hue/
│       ├── CREDITS.md
│       ├── asset-manifest.json
│       ├── source/
│       ├── scenes/
│       ├── cards/
│       ├── markers/
│       └── previews/
├── docs/uiux/
│   ├── HUE-VISUAL-RESEARCH.md
│   ├── HUE-ASSET-REPLACEMENT-MATRIX.md
│   ├── HUE-ART-DIRECTION-CONTRACT.md
│   ├── HUE-IMPLEMENTATION-PLAN.md
│   └── Phase-State.md
├── tools/
│   ├── build_hue_assets.py
│   └── build_hue_assets_ci.py
├── qa/render_smoke.py
├── vercel.json
├── robots.txt
├── sitemap.xml
└── .github/workflows/
    ├── deploy-pages.yml
    ├── build-hue-assets.yml
    └── uiux-factory-qa.yml
```

## Experience concept

Working narrative:

1. **Arrival** — mist, river, geography
2. **Citadel** — Ngọ Môn and the Imperial Threshold
3. **River** — Perfume River as the connective line rather than a single landmark
4. **Beyond the walls** — royal landscape and living city
5. **Routes** — three thematic ways to read Huế

Art direction:

- **Poetic**
- **Imperial**
- **Atmospheric**

Signature devices:

- River Line
- Imperial Threshold
- panoramic architecture
- restrained dark green / ivory / vermilion / aged-gold palette

## Motion-engine contract

The project intentionally separates reusable motion engineering from destination identity.

`script.js` remains the scroll/slider source of truth for:

- `clamp`, `smoothstep`, `lerp`, `segmentInOut`;
- requestAnimationFrame scroll smoothing;
- CSS-variable-driven choreography;
- the existing 560–1620 and 1760–2700 narrative segments;
- sights entrance at 2760–3560;
- controls entrance at 3360–3660;
- the three-set infinite slider and normalization logic;
- `prefers-reduced-motion` bypass.

The Huế transformation changes content, visual assets, art direction, chapter semantics, routes, and presentation without casually rewriting that engine.

## Local media and provenance

Production destination media is local under `assets/hue/` rather than hotlinked from the earlier visual source.

The asset family contains:

- 5 normalized source masters;
- 7 cinematic 1920×1080 scene derivatives;
- 5 editorial card crops;
- 3 original project SVG markers;
- a visual-veto contact sheet;
- SHA-256/provenance manifest;
- full attribution and transformation notes in `assets/hue/CREDITS.md`.

Run the asset builder only when intentionally regenerating approved media:

```bash
python tools/build_hue_assets_ci.py
```

## Typography

The Huế presentation uses **Cormorant Garamond** as the display candidate, loaded from Google Fonts, with system sans-serif UI/body fallbacks. Cormorant Garamond is distributed under the SIL Open Font License 1.1 and includes a Vietnamese subset.

The old display-face declaration remains in the preserved base stylesheet for compatibility but is overridden by the Huế art-direction layers on production surfaces.

## Run locally

Because the site is static:

```bash
npx serve .
```

or:

```bash
python -m http.server 4173
```

Then test both `index.html` and `routes.html`.

## GitHub Pages

1. Merge an approved implementation to `main`.
2. Open **Settings → Pages**.
3. Set **Source** to **GitHub Actions**.
4. `.github/workflows/deploy-pages.yml` deploys the repository root.

All internal page/media references remain relative so the site works under the existing repository subpath.

## Vercel

- Framework preset: **Other**
- Build command: empty
- Output directory: `.`

No client-side router or rewrite layer is required.

## Accessibility and motion

- keyboard-visible skip links;
- semantic chapter and route structures;
- keyboard-operable infinite slider;
- reduced-motion path inherited from the cinematic engine;
- routes reveal transitions disabled under reduced motion;
- rendered QA at mobile and desktop widths;
- Lighthouse Accessibility gate ≥ 90 on both production pages.

## QA contract

Before release:

- verify the preserved `script.js` engine blob;
- verify all required local Huế assets exist;
- reject old remote scene/pin hosts from production UI;
- reject stale destination copy from `index.html` and `routes.html`;
- render checkpoints at Intro, Citadel, River, and Places;
- verify the slider still clones 3 × 5 cards and normalizes cleanly;
- verify 390px mobile has no horizontal overflow;
- verify routes remain isolated from the cinematic engine;
- run Lighthouse Accessibility on both pages;
- inspect uploaded screenshots rather than treating a green build as visual proof;
- smoke-test the real deployed URL after release.

## Source transparency

This project began from an external cinematic-scroll reference used as a technical starting point. The portfolio transformation intentionally replaces the destination identity, imagery, editorial framing, navigation semantics, route content, visual system, and production media with an authored Huế concept while retaining only reusable interaction engineering that continues to serve the experience.

See `docs/uiux/` and `assets/hue/CREDITS.md` for the research, preserve/change boundary, asset provenance, and visual-veto record.
