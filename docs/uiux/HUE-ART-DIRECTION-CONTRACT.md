# HUẾ — Art Direction Contract

Status: DESIGN CONTRACT CANDIDATE — ready for human approval before implementation.

Project concept: **HUẾ — Between River & Citadel**

## 1. Core promise

The transformed project must feel authored for Huế, not adapted from Mostar.

A reviewer should understand the place through:

- river atmosphere;
- imperial threshold;
- axial / landscape order;
- outer monuments;
- living city detail.

The UI should support those ideas rather than compete with them.

## 2. Three adjectives

**POETIC · IMPERIAL · ATMOSPHERIC**

Every visual decision should support at least two of the three.

## 3. Signature design language

### 3.1 River Line

A thin continuous line is the dominant graphic system.

Use cases:

- progress/timeline;
- route line;
- section separator;
- card index connector;
- subtle hover motion.

Do not render it as a literal tourist-map route unless the geometry comes from verified map data.

### 3.2 Imperial Threshold

Architectural gates, walls and framed openings inform composition.

Use:

- hard rectangular framing mixed with open negative space;
- vertical edge reveals;
- architectural datum lines;
- clipped image thresholds.

Avoid:

- generic glass cards;
- universal 24px rounded rectangles;
- floating SaaS-style pill UI across every section.

### 3.3 Material contrast

Alternate:

- mist / water / sky;
- stone / brick / wall;
- lacquer / roof / ceremonial color;
- intricate Khải Định mosaic detail;
- market textures.

This contrast is important so the site does not become one long heritage postcard.

## 4. Color contract

Working tokens:

```css
--hue-ink: #171411;
--hue-ivory: #EEE4D2;
--hue-vermilion: #8F352A;
--hue-gold: #B99143;
--hue-river: #5C7775;
--hue-moss: #50604C;
--hue-mist: #B7C3BE;
```

Hierarchy:

1. broad cinematic fields: river / mist / ink;
2. text/editorial surfaces: ivory / ink;
3. interaction accent: vermilion;
4. ceremonial accent: gold, used sparingly;
5. secondary environmental accent: moss.

Do not use all colors at equal weight.

## 5. Typography contract

### Display

Requirements:

- Vietnamese glyph support;
- editorial / architectural presence;
- stable at very large sizes;
- less fashion-editorial than the current Ogg treatment.

### UI / body

Preferred candidate family:

`Be Vietnam Pro`

Reason:

- designed around Vietnamese text needs;
- clean enough for English UI;
- suitable for compact metadata / labels / routes.

Final display font remains open until glyph, licensing and rendering tests are completed.

Do not ship a font without verified Vietnamese diacritics even if the production copy is English-only at first.

## 6. Image direction

### Hero / cinematic

- panoramic / architectural;
- strong foreground-background separation;
- avoid travel-influencer people shots;
- avoid oversaturated blue sky;
- allow mist / grey sky / warm low sun;
- crops should feel spatial, not decorative.

### Cards / sights

- one subject per image;
- alternating landscape / detail / vertical silhouettes;
- avoid six near-identical monument photos;
- use market/material/detail imagery to keep the system alive.

### Processing

Allowed:

- crop;
- local color grade;
- mask / transparent cutout;
- controlled grain;
- reduced saturation;
- multi-layer editorial composite when license permits.

Avoid:

- fake AI glow;
- gold dust particles;
- generic radial light rays;
- fantasy architecture edits;
- historical-looking sepia filter across everything.

## 7. Homepage composition contract

### Phase 01 — ARRIVAL

Visual:
- Perfume River / mist / broad atmosphere;
- `HUẾ` title with maximum breathing room;
- minimal UI.

Emotion:
- quiet orientation, not immediate information overload.

### Phase 02 — CITADEL

Visual:
- Ngọ Môn emerges as a threshold;
- stronger vermilion/gold presence;
- use symmetry, then break it with one editorial offset.

Motion:
- reveal should feel architectural / opening, not bridge zoom replication.

### Phase 03 — RIVER

Visual:
- wider horizontal geometry;
- Trường Tiền and river reflection may appear as connective forms;
- the river line becomes explicit in navigation/progress.

Motion:
- lateral drift / long-line transition is preferable to a second monumental zoom.

### Phase 04 — BEYOND THE WALLS

Visual:
- shift from monumental space to detailed place fragments;
- Khải Định / Thiên Mụ / tomb / market / garden variety;
- slider becomes an editorial field guide.

### Phase 05 — ROUTES

Visual:
- map/route line language;
- numbered itineraries;
- content density increases intentionally after the cinematic opening.

## 8. Sights/card system

Replace current remote pin visuals with local SVG/CSS markers.

Card DNA:

- square-ish or architectural proportion, not soft pill cards;
- small index / category;
- strong place title;
- 1–2 lines of editorial cue;
- one image crop or material detail;
- river-line connector may pass behind/between cards.

Interaction:

- hover/focus reveals one secondary fact or route cue;
- do not add unnecessary tilt/glow.

## 9. Route page direction

The route page should feel like a printed field guide translated to screen.

Use:

- large route number;
- one dominant route line;
- editorial text columns;
- monument/river thumbnail crops;
- restrained dividers;
- asymmetry without reducing readability.

Avoid:

- three identical SaaS cards in a row;
- generic timeline dots with no relationship to Huế visual system.

## 10. Motion contract

### Preserve mechanics

- smooth interpolation;
- continuous CSS-variable updates;
- `segmentInOut` choreography model;
- reduced-motion behavior;
- slider normalization.

### Redesign choreography

The new animation must not preserve Mostar's visual sequence merely because the numbers are convenient.

Change as necessary:

- transformation amplitude;
- direction;
- scene timing;
- layer ownership;
- blur/saturation behavior;
- semantic names.

Representative visual gate required before full rollout:

- start / ARRIVAL;
- CITADEL peak;
- RIVER transition;
- slider / BEYOND THE WALLS;
- mobile representative state.

## 11. Anti-template gate

FAIL the design if three or more are true:

- cream background + serif + terracotta resembles generic AI luxury branding;
- every block is a rounded card;
- all sections use the same fade-up animation;
- hero is just giant type over one full-bleed photo;
- landmark cards are identical image/title/paragraph templates with no narrative relationship;
- decorative gradients/glows are used to manufacture "cinematic" mood;
- Huế could be swapped for another heritage city without changing the system.

PASS requires at least these project-specific signatures:

- River Line;
- Imperial Threshold composition;
- Huế-derived asset family;
- clearly different choreography between Citadel and River chapters;
- routes connected to the same visual grammar.

## 12. Responsive transformation

### Desktop

- cinematic scale and architectural framing at full strength;
- large title / long-line composition;
- slider can preserve strong lateral motion.

### Tablet

- reduce overlapping layers;
- keep threshold silhouette legible;
- crop rather than uniformly scale every desktop asset.

### Mobile

- do not shrink the desktop scene wholesale;
- choose a different crop/focal plan per phase;
- maintain `HUẾ` title integrity;
- prioritize one architectural subject per scene;
- slider/card interaction remains keyboard/touch friendly;
- minimum touch target 44px.

## 13. Content tone

Voice:

- concise;
- place-aware;
- observational;
- not brochure language;
- not mystical exoticism.

Preferred:

`The river carries the city past walls, pagodas and royal landscapes.`

Avoid:

`Discover the magical timeless beauty of charming Huế.`

All historical claims must be source-backed.

## 14. Design references — synthesis

ADOPT / ADAPT:

- Elektra Virtual Museum: editorial rhythm, museum-like typography/hover discipline;
- Unravel Van Gogh: narrative-first treatment of cultural material;
- Chartogne-Taillet: authored map/navigation language;
- Just Kibbeh: one clear scroll-story focus per phase.

REJECT:

- copying their palettes, typography, layouts or interaction signatures wholesale.

## 15. Implementation entry gate

Implementation may begin only after these are accepted:

- concept: `HUẾ — Between River & Citadel`;
- signature motif: River Line + Imperial Threshold;
- asset shortlist in `HUE-ASSET-REPLACEMENT-MATRIX.md`;
- palette direction;
- homepage chapter structure;
- all Mostar-specific scene media marked for removal.

Current status:

**READY FOR HUMAN VISUAL APPROVAL — NO CODE CHANGED YET.**