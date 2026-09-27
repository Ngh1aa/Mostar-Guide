# HUẾ — Between River & Citadel
## Implementation Contract

Status: IMPLEMENTATION

Source phase merged to `main`: research + production assets + visual veto PASS.

## 1. Preserve engineering contract

Preserve the reusable interaction engineering from the existing cinematic prototype unless rendered evidence proves a scene-specific retune is required:

- scroll smoothing / requestAnimationFrame architecture;
- `clamp`, `smoothstep`, `lerp`, `segmentInOut` model;
- CSS-variable-driven choreography;
- reduced-motion bypass;
- infinite sights-slider 3-set clone architecture;
- keyboard activation and slider normalization behavior;
- static/no-build deployment model.

The visual and destination identity are **not** preserved.

## 2. Remove Mostar identity

All user-facing production surfaces must remove stale references to:

- Mostar;
- Bosnia and Herzegovina;
- Stari Most;
- Neretva;
- Kujundžiluk;
- Koski Mehmed Pasha Mosque;
- Kajtaz House;
- War Photo Exhibition;
- Bridge/Bazaar as the primary conceptual navigation;
- remote Mostar Figma/CloudFront scene images;
- remote raster pin images.

## 3. New product identity

Title:

**HUẾ — Between River & Citadel**

Narrative chapters:

1. Arrival
2. Citadel
3. River
4. Legacy / Beyond the Walls
5. Routes

Design signatures:

- River Line;
- Imperial Threshold;
- panoramic architecture;
- poetic / imperial / atmospheric tone.

## 4. Approved local media

Use only approved local derivatives under `assets/hue/` for the new destination visual system.

Scene mapping:

- `.sky-img` → `assets/hue/scenes/01-river-atmosphere.webp`
- rear architectural layer → `02-citadel-backdrop.webp`
- primary landmark / threshold reveal → `03-ngo-mon-threshold.webp`
- split left → `04-imperial-left.webp`
- split right → `05-imperial-right.webp`
- river transition → `06-river-transition.webp`
- late narrative transition → `07-beyond-walls.webp`

Slider/editorial cards use `assets/hue/cards/*`.
Map/timeline markers use `assets/hue/markers/*`.

## 5. Navigation

Homepage navigation should become concept-native rather than a textual replacement of Mostar labels.

Recommended:

- Intro
- Citadel
- River
- Legacy
- Routes

Anchor IDs may be renamed where safe, but timeline navigation in `shared/nav.js` must be updated coherently.

## 6. Content contract

Write concise English editorial copy for Huế.

Do not invent:

- opening hours;
- exact walking times;
- visitor numbers;
- unsupported historical claims.

Use established factual context only. Route page may describe thematic route intent without invented durations until geographic validation is available.

## 7. Typography

Before locking a display font, verify:

- reuse/license suitability;
- Vietnamese glyph support;
- readable fallback behavior.

The existing Ogg setup is not immutable.

## 8. Implementation order

1. identity/copy/metadata;
2. local scene media wiring;
3. scene-specific CSS adaptation;
4. semantic nav/anchor mapping;
5. slider content and local markers/cards;
6. routes page transformation;
7. responsive repair at 390 / 768 / 1440;
8. reduced-motion/accessibility repair;
9. rendered choreography QA;
10. stale-Mostar identity search;
11. deployment smoke.

## 9. Acceptance gates

The implementation is not release-ready until all of the following are verified:

- no unintended user-facing Mostar identity remains;
- no old Mostar remote scene/pin URLs are used by production UI;
- cinematic sequence still progresses cleanly through the existing scroll engine;
- new Huế media does not crop or collide badly at 390 / 768 / 1440;
- slider remains infinite and keyboard-usable;
- reduced-motion path remains functional;
- no project-code console errors;
- no serious/critical Axe violations;
- Lighthouse Accessibility ≥ 90 on homepage and routes;
- GitHub Pages production deploy succeeds.
