# Mostar Guide

A static, multi-page Mostar prototype built around a pixel-faithful cinematic scroll homepage and a lightweight editorial routes page. The project uses vanilla HTML, CSS, and JavaScript only: no framework, bundler, package install, or build step.

## Project structure

```text
.
├── index.html
├── styles.css
├── script.js
├── routes.html
├── routes.css
├── routes.js
├── shared/
│   ├── nav.css
│   ├── nav.js
│   └── footer.css
├── assets/
│   └── favicon.svg
├── vercel.json
├── robots.txt
├── sitemap.xml
└── .github/workflows/deploy-pages.yml
```

## Cinematic core contract

`index.html`, `styles.css`, and `script.js` preserve the cinematic scroll choreography and remote media contract. Treat the animation engine in `script.js` and the cinematic custom properties/layer rules in `styles.css` as protected core.

Allowed extension points are deliberately separated:

- shared header/navigation styling → `shared/nav.css`
- cinematic anchor navigation (without touching the animation engine) → `shared/nav.js`
- routes page styling/interaction → `routes.css`, `routes.js`
- shared footer → `shared/footer.css`
- deployment, metadata, accessibility, and indexing files → their own scopes

The homepage contains the requested `#bridge` and `#bazaar` anchors, while Routes is a separate `routes.html` destination so the 3700px cinematic scroll sequence is not extended or re-timed.

## Run locally

Because this is a static site, either open `index.html` directly or run a tiny static server from the repository root:

```bash
npx serve .
```

Then open the local URL printed by `serve`. Test both `index.html` and `routes.html`.

## GitHub Pages

1. Push/merge the project to `main`.
2. Open **Settings → Pages** in the repository.
3. Set **Source** to **GitHub Actions**.
4. The included `.github/workflows/deploy-pages.yml` uploads the repository root and deploys it as a static Pages artifact.

All internal asset and page references use relative paths so the site works when published under a repository subpath such as `https://ngh1aa.github.io/Mostar-Guide/`.

## Vercel

1. Import this repository in Vercel.
2. Choose **Framework Preset: Other**.
3. Leave **Build Command** empty.
4. Set **Output Directory** to `.` (repository root).
5. Deploy.

`vercel.json` only enables clean URLs and disables trailing slashes; no client-side router or rewrite is required.

## Accessibility and motion

- The homepage and Routes page both provide a keyboard-visible skip link.
- `#bridge` and `#bazaar` are real semantic section targets.
- Route entries use `article`, `h2`, `dl`, and ordered lists rather than generic div-only markup.
- Existing `prefers-reduced-motion` behavior remains on the cinematic homepage; Routes also disables reveal transitions for reduced-motion users.
- Interactive shared-nav elements have visible keyboard focus states.

## QA checklist

Before release, verify:

- scroll manually from 0 → 3700px on `index.html` and confirm all five cinematic phases scrub cleanly;
- Intro, Bridge, Bazaar, and Routes navigation destinations resolve correctly;
- slider navigation loops continuously across the three cloned card sets;
- `routes.html` runs independently and does not load `script.js` or `styles.css`;
- remote Ogg font, seven scene PNGs, and three sight-pin PNGs return successfully;
- no console errors, horizontal overflow, missing styles, or broken relative links at desktop/tablet/mobile widths;
- reduced-motion behavior removes smoothing/transitions as intended;
- Lighthouse Accessibility target is ≥ 90 on both pages;
- deploy smoke-test the real GitHub Pages/Vercel URL after release rather than treating a successful build as visual proof.

## Design system snapshot

- Ink: `#111411`
- Paper: `#fdf1e1`
- Night: `#0b1110`
- Display type: `Ogg Medium`
- UI/body stack: Inter / Satoshi / system sans-serif
- Direction: cinematic, editorial, warm-historic
