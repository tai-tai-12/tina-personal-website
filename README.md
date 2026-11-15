# Tina Tai Personal Website — V8.16.1 (Work Page Print & Copy Polish)

**Complete Hugo/GitHub Pages source replacement.** All website files are at the ZIP root, including `.github/`. This is a narrowly scoped patch on V8.16 — no research metrics, Resume, FairPay case screenshots, layout hierarchy, or project navigation were changed.

## Changes

1. **Work intro, both languages:** English and Traditional Chinese now describe three core case studies *plus* an independent AI product build.
2. **Print page breaks:** Print-only CSS keeps each Work project row and its CTA together as far as the page size allows, avoids orphaned section headings, and reduces print-only padding.
3. **Print link contrast:** Case Study / Explore product build controls print as dark text with visible dark borders, even when background graphics are disabled.
4. **Unchanged screen experience:** Desktop, mobile, dark mode and hover/focus layout use the same V8.16 design. New versioned CSS filenames and cache-busting query strings prevent mixed deployments.

## Deploy (full replacement)

1. Back up V8.16. In a local Git checkout retain `.git/`.
2. Delete old website source files, then copy **every item from the ZIP root**, including `.github/`, into the repository root (not into a nested folder).
3. Optional source checks: `python3 scripts/verify_v8161.py` and `node --check static/js/site.js`.
4. Commit/push to `main`, verify `build` and `deploy` are green in GitHub Actions.
5. Verify the online page source includes `portfolio-version` **8.16.1** and stylesheet **portfolio-v8161.css**. Inspect EN/ZH Work, both Case Studies and print preview (enable or disable background graphics to compare).

## Validation boundary

V8.16.1 source checks and local browser print-preview checks do not substitute for the **official GitHub Actions Hugo build/deploy**, which must be green before accepting the release.
