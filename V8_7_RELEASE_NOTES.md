# V8.7 — Homepage Editorial Refinement

## Scope
Homepage only. All existing Work, Experience, Education, Research, About and individual case-study routes and content remain unchanged from V8.6. The new `static/css/home-v87.css` is loaded only on home pages, avoiding cross-page changes.

## Navigation decision
- Keep the top-level `Work` overview and three existing case-study pages. A new top-level `Projects` page would duplicate the existing Work destination.
- Hero `Explore Selected Work` scrolls to the three case studies on the homepage.
- Each homepage case has a clickable evidence visual, title, and visible `Read case study` link pointing directly to the detailed case (one click).
- `All case studies` opens the original Work overview for people who prefer comparing projects.

## Homepage changes
1. Hero: clearer headline, more consistent spacing, balanced portrait, concise CMU/AI positioning and two calls to action.
2. Selected Work: three consistent image-left/copy-right editorial case rows, original evidence visuals, direct case links, role context, compact metrics, accurate team-level Future Tech attribution.
3. Experience: four compact professional roles in a consistent timeline. Links go to full Experience; no duplicate long bullets.
4. Research: two first-author conference highlights with authentic presentation imagery and smaller, consistent images.
5. Education: three academic degrees including NYCU B.S. and Biomedical Engineering minor, preserving CMU/NYCU chronology.
6. About: one clear personal thesis, not a second career timeline. Clear About and Email links.

## Files modified
- `layouts/index.html` — rebuilt homepage layout and bilingual copy.
- `layouts/partials/head.html` — v8.7 marker and homepage-only CSS.
- `layouts/_default/baseof.html` — v8.7 data marker and script cache-busting.
- `.github/workflows/hugo.yaml` — V8.7 source verification before Hugo build.

## Files added
- `static/css/home-v87.css` — scoped, responsive homepage design rules.
- `scripts/verify_v87.py` — bilingual source and asset checks.
- `V8_7_RELEASE_NOTES.md`, `V8_7_QA.md`.

## Preserved
- Latest provided general PM resume (Oct 13 PDF).
- V8.6 Education and Experience information architecture.
- Bilingual research evidence and all official verification links.
- Future Tech Award is project/team recognition; the excluded non-scanned award photograph is not published.
- Existing sitemap URLs and GitHub Pages directory structure.
