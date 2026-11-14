# V8.16 — FairPay Evidence-First Work Redesign

Based on the **V8.15 full replacement ZIP**, not a partial patch.

## Changes

1. Rebuilt the FairPay Work overview as a source-evidence comparison. Large `$50 ≠ $500` values and accessible text are sized by CSS and reflow on mobile.
2. Improved the right-hand hierarchy with a project title, 3 concrete capabilities and one prototype-scope note.
3. Kept the 3 core cases first, with consistent editorial row proportions and hover/focus rules.
4. Added local EN/繁中 1200 × 628 PNG Open Graph images to use for direct FairPay case-study links.
5. Preserved prior FairPay case details, **three genuine screenshots**, click-to-enlarge behavior, 161-check context, synthetic-data and Sandbox boundaries.
6. Updated source version label to `8.16`, CSS assets, cache query, JS cache key, and Actions source verifier.

## Deliberate nonchanges

- No new nav or extra top-level Projects page.
- No modification to 3 core case facts, dates, awards, Research, Education, Experience, About or Resume.
- V8.15 diagram assets kept as existing detail-hero and historical compatibility files; they are **no longer used in the Work overview card**.
- No false production payments, client adoption or awards added to the project.

## Deployment

Replace the entire site source in GitHub with the contents of the ZIP root, **including `.github/`**. Preserve local `.git/` when using an existing clone. Push to `main`, verify GitHub Actions build and deploy, then test `/work/`, `/zh/work/` and the FairPay case in both languages.

## QA limitation

This release passed source-level and browser preview checks. A true Hugo build requires GitHub Actions because Hugo is unavailable in the local container.
