# Phase State — Huế Transformation

## Current phase

`VISUAL VETO COMPLETE / READY FOR IMPLEMENTATION`

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
| Verify asset build reproducibility | DONE_VERIFIED | asset production | GitHub Actions asset workflow PASS |
| Human visual veto on generated contact sheet | DONE_VERIFIED | visual approval | v3 contact-sheet review + individual scene review |
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

## Visual-veto record

### V1 — REJECTED

Reasons:

- first Ngọ Môn source was too close/generic to carry the Imperial Threshold signature;
- the contact-sheet preview exposed hidden RGB in alpha scenes as horizontal smear;
- the Trường Tiền scene relied on a traffic-heavy double exposure;
- the Khải Định / Đông Ba composite was too muddy and collage-like.

### V2 — CONDITIONAL

Changes:

- switched Ngọ Môn source to the grand entrance complex;
- fixed alpha-scene preview compositing against the real dark surface;
- re-selected a river-side public-domain Trường Tiền source;
- rebuilt `07-beyond-walls.webp` as a clean diagonal editorial split.

Remaining issue:

- Trường Tiền still read too much like a ghosted double exposure.

### V3 — PASS

Changes:

- rebuilt `06-river-transition.webp` as one clean panoramic bridge band over the river chapter;
- retained the River Line outside the photographic band as a navigation/signature language;
- reviewed the complete seven-scene contact sheet after alpha compositing.

Visual result:

- `01` establishes mist / river / geographic atmosphere;
- `02` establishes the imperial architectural mass;
- `03` is the primary Imperial Threshold reveal;
- `04` + `05` support split-frame choreography without visual artifacts in rendered compositing;
- `06` reads as river-first, bridge-second and no longer recreates the Mostar one-bridge-as-city logic;
- `07` closes the narrative with a deliberate royal-landscape / living-city contrast.

Decision:

`HUMAN VISUAL VETO = PASS`

## Asset-production evidence

- current asset workflow: `Build Huế Production Assets`;
- final visual-veto asset build: run `36294871943` — PASS;
- final review artifact: `hue-visual-veto`;
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

- The new assets have not yet been tested inside the live 3700px cinematic choreography; that belongs to the implementation/rendered gate.
- Final typography is intentionally not locked until Vietnamese glyph and license verification.
- Route durations/geographic itineraries are not finalized and must not be invented.

## Exit result

`RESEARCH + ASSET + VISUAL VETO GATE: PASS`

Reason:

The project now has an approved Huế narrative, art-direction contract, local provenance-documented production media, a repeatable asset pipeline, seven visually approved cinematic scenes, five editorial cards and three original SVG markers. The original Mostar production UI is still untouched at the moment of approval.

## Next gate

Create a separate Huế implementation branch and wire the approved visual system into production while preserving the reusable scroll/slider engineering contract. Implementation must then pass rendered choreography, responsive, accessibility, stale-Mostar-identity and deployment QA before release.
