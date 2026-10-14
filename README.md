# Tina Tai Personal Website — V8.3

**Full Visual Refinement · Responsive Stability · Evidence-Led Portfolio**  
Updated October 2026. Hugo source project prepared for the existing GitHub Pages site: `tai-tai-12/tina-personal-website`.

## What's new in V8.3

- Fixed homepage evidence metrics by replacing fragile inline/flex label fragments with a **three-column metrics grid**, including 390px layouts. The 94.5% / 264 / 90.16% values no longer break into a two-plus-one row.
- Corrected homepage Experience ordering: AITEWAN → NYCU AI Lab → NTU Hospital clinical internship → NYCU Testing Lab; preserves exact dates and keeps overlapping employment clear.
- Distinguished the three portfolio project visuals: clinical-product image, **source-backed** FP comparison (1,007 → 55 with sensitivity trade-off), and accessible vector validation workflow. The validation graphic is a *process schematic*, not an actual product screenshot.
- Rebalanced Education: degree timeline occupies a readable full-width section; license, honors, and training now appear as **full-width credential cards**, not a squeezed sidebar.
- Added a minimal **Medical Imaging → AI Research → Product Management → Business Analytics** career-journey module to the homepage About section.
- Standardized years, publication metadata, case titles, images, spacing, mobile breakpoints and figure captions across pages.
- Added enlarge-on-click for two **original research report figures** on the thoracic-aorta detail page. No identifying patient data or confidential client images were introduced.
- Preserved the correct Future Tech Award attribution as **NYCU-led team/project recognition**. As requested, the non-scanned award photograph was not added to the site.
- Normalized most legacy CSS priority flags, from ~2,097 `!important` occurrences in the previous combined file to **zero active overrides** in the V8.3 public CSS; introduced explicit typography, evidence-visual, timeline, credential, research-figure, and motion rules. Some legacy selectors remain in the consolidated file for compatibility; this is *not* a total redesign or complete elimination of historical selector definitions.
- Added `portfolio-version=8.3` and `?v=8.3.0` cache tags for CSS and JS.
- Updated source validation and GitHub Actions from `verify_v82.py` to `scripts/verify_v83.py`.

All existing routes and bilingual Hugo content remain intact. The downloaded resume is exactly the October 13 general PM resume.

## Deployment to GitHub Pages

1. Extract the ZIP. Copy the **contents** of the `tina-personal-website-v8-3/` folder into the root of the existing `tina-personal-website` repository, including hidden `.github/`.
2. Remove files that are no longer in this package, particularly `static/css/portfolio-v82.css` and prior unversioned CSS files. Keep the current `.github/workflows/hugo.yaml` from this package.
3. Push changes to `main`, or run the `Build and deploy` GitHub Actions workflow.
4. Confirm `Validate V8.3...`, `Build`, and `Deploy to GitHub Pages` succeed. The workflow installs Hugo and generates `public/`.
5. Hard-refresh (or use a fresh/incognito browser tab) and confirm **View Source → `<meta name="portfolio-version" content="8.3">`** and `portfolio-v83.css?v=8.3.0`.
6. Validate EN and 中文 home, Work, Experience, Education, Research, About, and all detail pages at mobile and desktop breakpoints. Test Dark Mode and figure enlarge/close.

### Local build

Hugo 0.164.0 is used in the GitHub Actions workflow. If Hugo is available locally:

```sh
python3 scripts/verify_v83.py
hugo server --disableFastRender
# or
hugo --gc --minify
```

**Testing limitation:** The preparation environment had Playwright/Chromium but could not reach the Hugo download host. Therefore the actual Hugo static build was *not* executed here. Browser QA used locally composed versions of the source templates (not a real `public/` build); the full Hugo compile remains a required deployment gate. See `docs/V8_3_QA.md`.

## Project structure

- `layouts/`: Hugo templates for home, Work, Experience, Education, Research, About, and detail pages.
- `layouts/partials/clinical-evidence-visual-v83.html`: shared evidence diagram on home and Work.
- `static/css/portfolio-v83.css`: sole public CSS entry point, normalized and refined design system.
- `static/images/projects/validation-workflow-v83.svg`: accessible process schematic.
- `static/js/site.js`: theme, menu, scroll reveal, and figure enlargement.
- `content/en/` and `content/zh/`: full English and Traditional Chinese content.
- `static/resume/Shih-Ting_Tai_Resume.pdf`: current General PM resume.
- `scripts/verify_v83.py`: source checks, run automatically by GitHub Actions.
- `docs/V8_3_RELEASE_NOTES.md` / `docs/V8_3_QA.md`: change details and test evidence.

### Privacy and evidence policy

Original transcripts, raw credentials, private identifiers, and the non-scanned Future Tech Award photo are **not** in publicly served assets. The validation visual depicts a generalized work process; it is not an actual customer interface. Research figures are from original source material and are described as research, not as prospective clinical validation or commercial deployment evidence.
