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
| Create aligned split-pair proof | DONE_VERIFIED | visual approval | `assets/hue/previews/split-pair-proof.webp` |
| Reject old Mostar scene fingerprints from new asset family | DONE_VERIFIED | asset production | CI grep gate + local-only asset tree |
| Verify asset build reproducibility | DONE_VERIFIED | asset production | GitHub Actions asset workflow PASS |
| Human visual veto on generated scene system | DONE_VERIFIED | visual approval | v5 contact-sheet review + split-pair proof |
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
    ├── scene-contact-sheet.webp
    └── split-pair-proof.webp
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
- rebuilt `07-beyond-walls.webp` as a cleaner editorial contrast.

Remaining issue:

- Trường Tiền still read too much like a ghosted double exposure.

### V3 — REOPENED AFTER HUMAN REVIEW

The uploaded contact sheet exposed issues that structural asset QA could not catch:

- `03` still felt like a heavy tunnel vignette rather than an architectural threshold;
- `04` and `05` looked acceptable individually but duplicated the building when combined;
- `06` still read like a photo strip pasted over another photo;
- `07` was cleaner than V1 but the hard diagonal split still felt collage-like.

Decision:

`HUMAN VISUAL VETO = FAIL / REVISE`

### V4 — CONDITIONAL

Changes:

- `01` received clearer river depth and less grey blur;
- `02` retained more stone/roof detail;
- `03` became an inset architectural portal with restrained edge feathering;
- `06` became one coherent full-frame Trường Tiền scene with the River Line signature;
- `07` became an intentional editorial diptych on a dark field rather than a blended diagonal composite.

Remaining issue:

- the first V4 split-pair implementation still duplicated Ngọ Môn because left/right layers used different crops of the same source.

### V5 — PASS

Final split-pair correction:

- `04` and `05` now use one shared, registered full-frame Ngọ Môn crop;
- only the alpha masks differ between the two layers;
- the combined proof reconstructs a single continuous architectural image before the two halves separate in motion;
- `split-pair-proof.webp` is the rendered evidence for this behavior.

Final visual result:

- `01` establishes river / mountain / mist atmosphere without over-processing;
- `02` establishes the imperial architectural mass clearly;
- `03` reads as an intentional threshold/portal rather than a tunnel vignette;
- `04` + `05` reconstruct one coherent scene and are suitable for split-frame choreography;
- `06` reads as a Huế river-crossing scene, not a pasted bridge band and not a Mostar-style singular-bridge identity;
- `07` closes the sequence with a deliberate heritage / living-city editorial contrast.

Decision:

`HUMAN VISUAL VETO = PASS`

## Asset-production evidence

- current asset workflow: `Build Huế Production Assets`;
- final visual-veto asset build: run `36297222747` — PASS;
- final review artifact: `hue-visual-veto`;
- aligned split-pair refinement is part of the reproducible pipeline;
- current generated-asset head after the final build: `b2a47c176ae04ee6f48d033646452459fb976cde`;
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

- The approved assets have not yet been tested inside the live 3700px cinematic choreography; that belongs to the implementation/rendered gate.
- Final typography is intentionally not locked until Vietnamese glyph and license verification.
- Route durations/geographic itineraries are not finalized and must not be invented.

## Exit result

`RESEARCH + ASSET + VISUAL VETO GATE: PASS`

Reason:

The project now has an approved Huế narrative, art-direction contract, local provenance-documented production media, a repeatable asset pipeline, seven visually approved cinematic scenes, a verified single-scene split pair, five editorial cards and three original SVG markers. The original Mostar production UI is still untouched at the moment of approval.

## Next gate

Create a separate Huế implementation branch and wire the approved visual system into production while preserving the reusable scroll/slider engineering contract. Implementation must then pass rendered choreography, responsive, accessibility, stale-Mostar-identity and deployment QA before release.
