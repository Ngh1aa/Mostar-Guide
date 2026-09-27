# Phase State — Huế Transformation

## Current phase

`PRODUCTION ASSET PREPARATION / VISUAL APPROVAL GATE`

Branch: `research/hue-visual-system`

No production `index.html`, `styles.css`, `script.js`, `routes.html`, `routes.css`, or `routes.js` has been changed in this phase.

## Current direction

Project transformation:

`Mostar-derived cinematic prototype → original Huế cultural experience`

Working concept:

**HUẾ — Between River & Citadel**

Style adjectives:

- POETIC
- IMPERIAL
- ATMOSPHERIC

Signature system:

- River Line
- Imperial Threshold
- panoramic architectural composition
- restrained five-colour-derived palette

## Requirement ledger

| Requirement | State | Owner phase | Verification |
|---|---|---|---|
| Audit current destination-specific identity | DONE_VERIFIED | research | source inspection |
| Establish Huế factual narrative basis | DONE_VERIFIED | research | UNESCO / authoritative research |
| Define visual direction | DONE_VERIFIED | research | art-direction contract |
| Replace current Mostar asset plan | DONE_VERIFIED | research | replacement matrix |
| Verify source licenses for primary candidates | DONE_VERIFIED | research | Wikimedia Commons file pages |
| Download/store production media locally | DONE_VERIFIED | asset production | `assets/hue/source/` + manifest hashes |
| Produce seven optimized scene derivatives | DONE_VERIFIED | asset production | 7 × 1920×1080 WebP outputs + manifest |
| Produce editorial card derivatives | DONE_VERIFIED | asset production | 5 × 960×640 WebP outputs |
| Replace remote raster pins with local authored marker system | DONE_VERIFIED | asset production | 3 local SVG markers |
| Record attribution / transformations | DONE_VERIFIED | asset production | `assets/hue/CREDITS.md` |
| Create visual-review contact sheet | DONE_VERIFIED | asset production | `assets/hue/previews/scene-contact-sheet.webp` |
| Reject old Mostar scene fingerprints from new asset family | DONE_VERIFIED | asset production | CI grep gate + local-only asset tree |
| Verify asset build reproducibility | DONE_VERIFIED | asset production | GitHub Actions `Build Huế Production Assets` run #2 PASS |
| Human visual veto on generated contact sheet | PENDING_FUTURE_PHASE | visual approval | inspect contact sheet / scene crops before UI wiring |
| Verify display-font license/glyph coverage | PENDING_FUTURE_PHASE | implementation | font specimen + license source |
| Implement new Huế content/visual system | PENDING_FUTURE_PHASE | implementation | rendered representative pages |
| Responsive 390/768/1440 visual QA | PENDING_FUTURE_PHASE | QA | browser screenshots |
| Accessibility / Axe / Lighthouse | PENDING_FUTURE_PHASE | QA | CI/browser evidence |
| GitHub Pages production smoke | PENDING_FUTURE_PHASE | release | deployed URL |

## Production asset inventory

```text
assets/hue/
├── CREDITS.md
├── asset-manifest.json
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
├── cards/
│   ├── ngo-mon.webp
│   ├── perfume-river.webp
│   ├── truong-tien.webp
│   ├── khai-dinh.webp
│   └── dong-ba.webp
├── markers/
│   ├── river-node.svg
│   ├── imperial-node.svg
│   └── legacy-node.svg
└── previews/
    └── scene-contact-sheet.webp
```

## Asset-production evidence

Build workflow:

- workflow: `Build Huế Production Assets`
- successful run: `36293848436`
- generated-asset commit: `6cb12cccdca2d30cd6785feb45a4d22b752fa52a`
- source masters are normalized locally to max 2560 px where needed;
- all seven cinematic scene outputs are 1920×1080;
- threshold/split scene families retain alpha for layered choreography;
- `asset-manifest.json` records source IDs, dimensions, transforms and SHA-256 hashes;
- `CREDITS.md` records author/source/license/transformation details;
- generated Huế asset family does not depend on the existing Mostar Figma/CloudFront scene URLs.

## Current blockers

`BLOCKED = 0`

## Unaccounted due-now requirements

`UNACCOUNTED = 0`

## Evidence limitations

- Asset-generation and structural/media contracts are verified, but the seven-scene contact sheet has not yet received the human visual veto required before UI wiring.
- The generated crops/composites have not yet been tested inside the live 3700px cinematic choreography; that belongs to the implementation/rendered gate.
- Final typography is intentionally not locked until Vietnamese glyph and license verification.
- Route durations/geographic itineraries are not finalized and must not be invented.

## Exit result

`ASSET PRODUCTION GATE: PASS`

Reason:

The approved Huế shortlist has been converted into a local, provenance-documented and reproducible production asset family: source masters, seven cinematic scenes, five editorial cards, three original SVG markers, manifest, credits and review contact sheet. The original Mostar production UI remains untouched.

## Next gate

Human visual approval of:

1. `assets/hue/previews/scene-contact-sheet.webp`
2. `assets/hue/scenes/03-ngo-mon-threshold.webp`
3. `assets/hue/scenes/04-imperial-left.webp` + `05-imperial-right.webp`
4. `assets/hue/scenes/06-river-transition.webp`
5. `assets/hue/scenes/07-beyond-walls.webp`

Only after that visual veto should implementation begin on the Huế HTML/CSS/JS transformation.
