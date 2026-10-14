# Tina Tai Personal Website · V8.4

**Evidence-first Work visuals · Unified credentials · English / 繁體中文**

This ZIP contains the **full Hugo source project** for the existing GitHub Pages site (`tai-tai-12/tina-personal-website`), not only the files changed in V8.4.

## V8.4 changes

- **Work + Home:** All three case-study thumbnails now use the same reusable, bilingual HTML/CSS visual component (shared panel colors, title hierarchy, evidence/flow representation, outcome rail and source/context footer). A photographic thumbnail no longer appears alongside two unrelated infographic styles.
- **Product case:** Four-stage diagram summarizes physician discovery, workflow testing, trade-off decisions and release readiness, with the supported ~67% processing-time improvement and user/site counts.
- **Clinical AI case:** FP candidate reduction uses the same 264-case retrospective cohort, with `1,007 → 55`, `−94.54%` and the accompanying sensitivity decrease (`84.96% → 80.97%`). These are research measures, **not prospective outcomes**.
- **Structured Validation case:** Four-stage Scope → Test → Resolve → Deliver schematic; clearly labeled as a schematic, not a customer application screenshot.
- **Education:** The three credential categories now have matching headings, item typography and metadata styles. The professional license no longer uses an oversized heading.
- **Selected Certifications:** Five groups only, each with **public person-specific certificate verification** rather than unrelated course-information pages: CS50 AI, Google Ads Search & Measurement, IBM Data Science Fundamentals with Python & SQL, IBM Relational Database Administrator, UC Davis Tableau. `Data Science & Smart Instrumentation` remains out of this public curated list. Full credentials need not be listed on the site.
- **Responsive refinement:** No clipped visuals or broken `1,007` metric at tested phone widths; four-stage visuals use a two-by-two layout on mobile. Existing research pages, experience, resume and official Future Tech attribution were preserved.

## Deployment to the existing repository

1. Unzip the package and copy **the contents** of `tina-personal-website-v8-4/` to the root of the existing GitHub repository, including the hidden `.github/` folder.
2. Remove obsolete files no longer present in the package (notably previously used public versioned stylesheets, if any). Keep `.github/workflows/hugo.yaml` from this package.
3. Commit and push to `main`. GitHub Actions runs `scripts/verify_v84.py`, builds the site using Hugo and deploys it to GitHub Pages.
4. Confirm both `Build` and `Deploy` succeed. View Source should show `<meta name="portfolio-version" content="8.4">` and `portfolio-v84.css?v=8.4.0`.
5. Hard refresh, then check the English and 繁體中文 Work, Education and Home pages on desktop and mobile; spot-check other pages, Dark Mode, case links and PDF download.

### Optional local commands

```bash
python3 scripts/verify_v84.py
hugo server --disableFastRender
# or: hugo --gc --minify
```

Hugo version used by GitHub Actions: **0.164.0**.

## File map

- `layouts/partials/work-evidence-visual-v84.html` — shared evidence graphics for all three cases; translated for EN/zh.
- `layouts/work/list.html` and `layouts/index.html` — reuse the same partial.
- `layouts/education/single.html` — three-column credentials and person-specific verification links.
- `static/css/portfolio-v84.css` — one public CSS file, with V8.4 responsive component rules.
- `static/resume/Shih-Ting_Tai_Resume.pdf` — original October 13 general PM resume.
- `scripts/verify_v84.py`, `.github/workflows/hugo.yaml` — pre-build verification.
- `docs/V8_4_RELEASE_NOTES.md`, `docs/V8_4_QA.md` — scope, verification evidence and testing limitations.

## Privacy / attribution

No raw transcripts, private license scan, exam score reports, original certificates, customer clinical data or non-scanned Future Tech Award photograph have been added to `static/`. DeepBT A+ recognition remains **team/project recognition**, not an individual award.

## QA limitations

V8.4 templates, HTML/CSS responsive layouts and JavaScript were checked offline; the environment could not run the actual Hugo executable. The **real Hugo build and post-deployment browser review are still required**. Preview HTML used for local browser testing reproduces affected template structures; it is not a Hugo-produced `public/` output.
