# V8.13.1 Final Release — Localization + Research Card Overflow Fix

## P0: Research Area metric containment

Root cause: V8.13 `.research-proof-row-v64` inherited `flex-wrap: nowrap` and `width: max-content`; long metric labels exceeded the research card's bounds even though the **page itself** had no horizontal overflow.

Resolution: Scoped CSS to `.research-area-card-v64 .research-proof-row-v64`, using three equal `minmax(0,1fr)` columns, stacked number/label, natural wrap, and small-phone vertical layout. Updated English DSC label to `DSC · segmentation overlap` for clarity without changing the numerical claim.

## Localization

- `PRIMARY RESEARCH` → `主要研究`; `FOUNDATIONAL RESEARCH · NSTC` → `基礎研究 · 國科會` on zh site.
- `Takeaway` → `重點總結` in both zh Product and Clinical AI cases.
- Reworded one zh Clinical AI cohort summary into fluent, unambiguous Mandarin.
- Localized screen-reader labels for research evidence, case context/metrics/navigation, brand home link, and aorta results. Source study images and research citations unchanged.

## Preserved

V8.13 navigation/visual system, Home, Work, Experience, Education, Research, About, case evidence and content, documents, privacy boundaries, latest 10/13 resume, original awards, and GitHub Pages workflow.

## Files changed

- `layouts/research/list.html`, `layouts/research/single.html`, `layouts/work/single.html`, `layouts/partials/header.html`
- `content/zh/work/medical-ai-product.md`, `content/zh/work/clinical-ai-at-scale.md`
- `static/css/portfolio-v8131.css` (new consolidated style), `static/css/home-v8131.css` (renamed with unchanged rules)
- `layouts/partials/head.html`, `layouts/_default/baseof.html`, `.github/workflows/hugo.yaml`, `scripts/verify_v8131.py`
