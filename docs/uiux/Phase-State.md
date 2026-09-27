# Phase State — Huế Transformation

## Current phase

`IMPLEMENTATION COMPLETE / PR QA`

Branch: `feat/hue-between-river-citadel`

Pull request: `#5`

The Huế transformation is implemented on the feature branch. `main` is still unchanged until the implementation PR is approved and merged.

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

## Preserve / change result

### Preserved exactly

The cinematic engine remains byte-identical:

- `script.js` blob SHA: `ac4a26e4e98bb56fffe3ac7213b2951f12560543`
- `clamp()`
- `smoothstep()`
- `lerp()`
- `segmentInOut()`
- CSS-variable-driven rendering
- requestAnimationFrame scheduling
- reduced-motion branch
- three-set infinite slider cloning
- `jumpSightSlider()` / `normalizeSightSlider()`

### Replaced / transformed

- all user-facing Mostar / Bosnia identity;
- all seven remote Mostar scene images;
- all three remote raster pin images;
- homepage metadata and copy;
- story anchors and navigation labels;
- sights content;
- route content;
- favicon / visual identity;
- Huế-specific layer treatment and card styling;
- rendered QA contract and stale-identity checks.

Scene-specific visual motion is retuned through Huế CSS/layer geometry instead of rewriting the preserved engine.

## Requirement ledger

| Requirement | State | Verification |
|---|---|---|
| Huế factual / visual research | DONE_VERIFIED | research docs + authoritative source record |
| Huế art-direction contract | DONE_VERIFIED | `HUE-ART-DIRECTION-CONTRACT.md` |
| Production media local + provenance documented | DONE_VERIFIED | `assets/hue/` + `CREDITS.md` + manifest |
| Seven cinematic scene derivatives | DONE_VERIFIED | asset inventory / visual-veto artifact |
| Human visual veto on scene family | DONE_VERIFIED | V5 contact-sheet + split-pair proof |
| Replace Mostar identity on homepage | DONE_VERIFIED | branch source + QA stale-identity gate |
| Replace Mostar identity on Routes | DONE_VERIFIED | branch source + QA stale-identity gate |
| Replace remote scene/pin media | DONE_VERIFIED | local Huế media + CI grep gate |
| Preserve cinematic engine | DONE_VERIFIED | exact `script.js` blob check |
| Retune choreography for Huế media | DONE_VERIFIED | `hue-choreography.css` + rendered checkpoints |
| Preserve 3× infinite slider architecture | DONE_VERIFIED | rendered smoke: 15 cloned cards + control movement |
| Rename story anchors | DONE_VERIFIED | `#citadel` / `#river` + `shared/nav.js` |
| Routes remain isolated from cinematic engine | DONE_VERIFIED | rendered smoke confirms no `script.js` on routes page |
| Desktop rendered choreography | DONE_VERIFIED | branch QA run `36298304486` |
| Mobile 390px overflow smoke | DONE_VERIFIED | branch QA run `36298304486` |
| Accessibility gate | DONE_VERIFIED | Lighthouse Home `1.00`, Routes `1.00` |
| Pull-request QA on final head | PENDING_CURRENT_PHASE | PR #5 workflow |
| Production GitHub Pages smoke | PENDING_FUTURE_PHASE | after merge / deploy |

## Implemented production surfaces

### Homepage

- identity: `HUẾ — Between River & Citadel`;
- chapters: Intro → Citadel → River → Places;
- local scene family under `assets/hue/scenes/`;
- local editorial card imagery under `assets/hue/cards/`;
- local SVG markers under `assets/hue/markers/`;
- Huế-specific visual overrides in `hue.css`;
- scene tuning in `hue-choreography.css`.

### Routes

- three Huế thematic routes;
- 4 / 5 / 3 stop structure retained for stable QA geometry;
- no invented route duration claims;
- local Huế markers;
- route-specific visual language in `hue-routes.css`;
- routes page remains independent of `script.js`.

## Latest rendered evidence

Branch QA run:

- run: `36298304486`
- result: `PASS`
- JavaScript syntax: PASS
- preserved engine blob: PASS
- Huế production asset contract: PASS
- stale Mostar identity gate: PASS
- Chromium choreography smoke: PASS
- infinite slider interaction: PASS
- 390px responsive overflow smoke: PASS
- Lighthouse Accessibility: Home `1.00`
- Lighthouse Accessibility: Routes `1.00`
- artifact: `hue-uiux-qa-evidence`

Representative evidence includes:

- `home-intro.png`
- `home-citadel.png`
- `home-river.png`
- `home-places.png`
- `routes-desktop.png`
- `mobile-index.png`
- `mobile-routes.png`

## Current blockers

`BLOCKED = 0`

## Unaccounted due-now requirements

`UNACCOUNTED = 0`

## Current evidence limitations

- The implementation has not yet been production-smoked on the public GitHub Pages URL because `main` has not been merged.
- The repository slug remains `Mostar-Guide`; this is an infrastructure name, not user-facing destination identity.
- `script.js` retains legacy internal variable/class vocabulary because byte preservation is intentional; user-facing semantics are Huế-specific.

## Current result

`IMPLEMENTATION CANDIDATE: PASS ON FEATURE BRANCH`

Reason:

The implementation replaces destination identity, content and media while keeping the verified animation engine intact. Rendered browser evidence passes current functional, responsive and accessibility gates.

## Next gate

1. PR #5 final-head QA must complete successfully.
2. Human review of the PR implementation candidate.
3. Merge only after approval.
4. Run GitHub Pages deployment and production smoke on the public URL after merge.
