# V8.7 QA / Release gates

## Completed here
- 102/102 source checks via `python3 scripts/verify_v87.py`.
- Bilingual `layouts/index.html` and three case visuals checked for direct links.
- 10 Chromium mock-render viewport checks: EN/ZH × 1440 / 1024 / 768 / 390 / 360 pixels.
- No horizontal overflow, missing rendered images, or missing role/case/degree rows detected in these mock previews.
- Existing Resume SHA-256 matches the uploaded Oct 13 reference PDF.
- Verified source files did not add private credentials, transcripts, or the excluded Future Tech Award photograph.
- New homepage stylesheet is explicitly homepage-scoped.

## Limits
This environment did not have a Hugo executable and could not complete the formal Hugo build. Chromium tests rendered a local approximation of the Hugo homepage; they are **not** screenshots of the production GitHub Pages site. CSS fonts can also differ when Google Fonts are not reachable offline.

## Required deployment verification
1. In GitHub Actions confirm `Validate V8.7 homepage and preserved site content`, `Build`, and `Deploy to GitHub Pages` all succeed.
2. Inspect source of the deployed home page: `<meta name="portfolio-version" content="8.7">` and `home-v87.css?v=8.7.0`.
3. Check the English homepage and `/zh/` homepage on desktop and smartphone.
4. Select `Explore Selected Work`; it should scroll to `#work`.
5. Click each `Read case study` to confirm it enters its own detail page (no extra overview step).
6. Check `All case studies` leads to the existing Work overview.
7. Check all three Education rows appear, including the undergraduate NYCU degree.
8. Confirm Research pictures load on scroll, and test Light/Dark modes and reduced motion.
9. Download Resume and verify correct updated version.
