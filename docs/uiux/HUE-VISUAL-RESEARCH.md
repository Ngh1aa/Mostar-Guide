# HUẾ — Visual Research

Status: RESEARCH / ART DIRECTION ONLY — no implementation in this phase.

Target repository: `Ngh1aa/Mostar-Guide`

## 1. Research objective

Transform the current Mostar-derived destination identity into an original Huế cultural experience while preserving only reusable interaction engineering. The research must prevent a superficial "rename Mostar → Huế" result.

## 2. Verified project baseline

The current implementation is a static HTML/CSS/JS prototype with:

- cinematic homepage in `index.html` / `styles.css` / `script.js`;
- 3700px scroll choreography;
- layered scene composition driven by CSS custom properties;
- `clamp`, `smoothstep`, `lerp`, `segmentInOut` motion helpers;
- 3-set infinite slider with `normalizeSightSlider()`;
- separate editorial `routes.html` page;
- GitHub Pages + Vercel-compatible static deployment.

Current destination-specific identity that must be replaced later:

- Mostar / Bosnia and Herzegovina naming;
- Stari Most, Neretva, Kujundžiluk, Koski Mehmed Pasha Mosque, Kajtaz House, War Photo Exhibition;
- all seven existing remote scene PNGs;
- all three existing remote pin-icon PNGs;
- Mostar routes, copy, metadata and editorial framing.

## 3. Huế factual grounding

Primary source: UNESCO Complex of Hué Monuments — https://whc.unesco.org/en/list/678

Verified facts used to shape the design direction:

- Huế became the capital of unified Viet Nam in 1802 under the Nguyễn dynasty and remained the political, cultural and religious centre until 1945.
- The Perfume River runs through the Capital City, Imperial City, Forbidden Purple City and Inner City and is part of the site's defining natural setting.
- The plan of the capital responds to physical landscape and geomantic principles.
- UNESCO explicitly describes relationships with the Five Cardinal Points, Five Elements and Five Colours: yellow, white, blue, black and red.
- Important components extend beyond the Citadel to Thiên Mụ Pagoda and the Nguyễn royal tombs along/upstream from the Perfume River.

Design consequence: Huế should not be framed as one iconic object. The stronger native narrative is **river + axis + threshold + landscape + ritual + living city**.

## 4. Narrative direction

### Chosen concept

**HUẾ — Between River & Citadel**

Narrative spine:

`Mist / river atmosphere → threshold / Ngọ Môn → imperial order → river connection → outer monuments / living city`

The Perfume River is the continuity device. The Citadel is the threshold device. Royal tombs and Thiên Mụ expand the world beyond the walls. Đông Ba prevents the experience from becoming a frozen royal-history museum.

### Three style adjectives

- POETIC
- IMPERIAL
- ATMOSPHERIC

### Anti-concepts

Do not design:

- a generic tourism-board landing page;
- "Mostar with Vietnamese landmarks";
- Hội An lantern / mustard / nostalgia clichés;
- generic beige-serif luxury travel UI;
- black-neon AI portfolio styling;
- a heritage site that treats every section as identical rounded cards.

## 5. Visual vocabulary from Huế

### Architecture

- long horizontal fortified walls;
- monumental gates and layered roofs;
- axial courtyards;
- dark lacquer / painted timber;
- yellow/orange glazed roof tiles;
- grey stone and brick bases;
- ceramic / glass mosaic detail at Khải Định.

### Landscape

- broad river surface rather than narrow dramatic canyon;
- low horizon and long reflections;
- garden / pine / lotus / courtyard greenery;
- mist, overcast light and warm late-day light both fit the city better than perpetual bright-blue travel imagery.

### Composition

Prefer:

- long panoramic crops;
- architectural symmetry broken by one asymmetric editorial layer;
- framed thresholds / gateways;
- river-line motifs;
- large negative space;
- occasional macro-detail crops of roof, mosaic or timber to interrupt landscape scale.

Avoid repeating the current Mostar silhouette formula on every phase.

## 6. Proposed visual system

### Signature motif — `THE RIVER LINE`

A thin continuous line derived from the Sông Hương / Perfume River becomes a recurring navigation and transition motif:

- timeline indicator;
- route map line;
- section divider;
- hover underline;
- small animated path through the sights slider.

It should be geometric/editorial, not a literal map trace unless source data is later verified.

### Secondary motif — `IMPERIAL THRESHOLD`

Use gate/door/courtyard framing as a compositional device:

- hero elements enter through vertical frame edges;
- section titles can sit on/under a thin architectural datum line;
- card crops may use gate-like top/bottom masks rather than generic rounded corners.

## 7. Palette direction

The final numerical palette is PROPOSED, not historical fact. It is informed by Huế architecture/landscape plus UNESCO's documented Five Colours concept.

Proposed working tokens:

- `--hue-ink`: `#171411` — lacquer / night neutral
- `--hue-ivory`: `#EEE4D2` — warm paper / stone
- `--hue-vermilion`: `#8F352A` — imperial red accent
- `--hue-gold`: `#B99143` — muted roof / ceremonial yellow
- `--hue-river`: `#5C7775` — desaturated blue-green river tone
- `--hue-moss`: `#50604C` — garden / weathered green
- `--hue-mist`: `#B7C3BE` — atmospheric light neutral

Rules:

- vermilion is the primary active accent, not scattered decoration;
- gold is secondary and restrained;
- river/mist should dominate broad cinematic surfaces;
- ivory is used for editorial text/panels, not as an all-purpose beige background.

## 8. Typography direction

The current Ogg Medium display treatment is not protected.

Requirements for the replacement type system:

- full Vietnamese diacritic coverage;
- strong large editorial display presence;
- readable English body copy;
- no "fashion serif + generic sans" default pairing without a clear reason.

Working direction for implementation research:

- display: a Vietnamese-capable serif with moderate contrast and less fashion-editorial personality than Ogg;
- UI/body: `Be Vietnam Pro` or another Vietnamese-first sans candidate;
- headings should feel architectural and measured rather than romantic/script-like.

Final font files must be checked for license and glyph coverage before implementation.

## 9. Interaction / website references

These are interaction references, not templates to clone.

### Elektra Virtual Museum — Awwwards
https://www.awwwards.com/inspiration/exhibition-page

ADAPT:
- editorial scroll rhythm;
- typography-led museum framing;
- hover as information reveal rather than decoration.

REJECT:
- importing its exact monochrome identity.

### Unravel Van Gogh — Awwwards
https://www.awwwards.com/sites/unravel-van-gogh

ADAPT:
- story-first sequencing;
- image / narrative integration;
- letting source material dominate rather than UI chrome.

### Chartogne-Taillet map experience — Awwwards
https://www.awwwards.com/inspiration/chartogn-taillet-dive-through-the-wines-plots

ADAPT:
- map/route aesthetic as an authored navigation layer;
- moving between place and story without turning the experience into a normal card grid.

### Just Kibbeh — Awwwards
https://www.awwwards.com/sites/just-kibbeh

ADAPT:
- immersive scroll storytelling;
- one narrative focus per phase.

REJECT:
- copying food/ecommerce visual language.

## 10. Proposed homepage chapters

Replace the current `Intro / Bridge / Bazaar / Sights` mental model with:

1. **ARRIVAL** — river atmosphere / orientation
2. **CITADEL** — Ngọ Môn as threshold, not merely hero landmark
3. **RIVER** — Perfume River / Trường Tiền / movement through city
4. **BEYOND THE WALLS** — Thiên Mụ / royal tombs / Đông Ba / living Huế
5. **ROUTES** — editorial itineraries grounded in real geography

Exact route durations are PENDING RESEARCH and must not be invented.

## 11. Motion direction

Keep the strongest technical ideas from the existing engine but change the visual choreography.

Preserve as reusable mechanics:

- smooth scroll interpolation;
- CSS-variable-driven rendering;
- `segmentInOut` timing model;
- reduced-motion branch;
- infinite slider normalization;
- requestAnimationFrame scheduling.

Change later during implementation:

- asset-specific translation distances;
- scale ranges;
- scene opacity timing;
- background saturation/blur logic;
- semantic variable/class names where worthwhile;
- nav anchor names and timeline offsets after the new chapter timing is proven.

## 12. Phase-1 decision

**ART DIRECTION: ADOPTED FOR IMPLEMENTATION CANDIDATE**

Chosen direction:

`Between River & Citadel`

Visual signature:

`river line + imperial threshold + panoramic architecture + restrained five-colour-derived palette`

Current-phase blockers:

- none for art-direction research.

Future-phase requirements:

- download/store replacement media locally;
- add asset attribution/provenance file;
- prototype scene composites/crops;
- verify font licensing/glyph coverage;
- rendered visual gate before full rollout;
- implementation QA and deployment smoke.