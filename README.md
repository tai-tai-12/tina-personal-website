# Tina Tai Personal Website — V8.15 (Work Consistency & FairPay Readability)

**Complete GitHub Pages/Hugo source replacement.** All required site files are at the ZIP root, including the hidden `.github/` workflow directory. This release is based on V8.14 and preserves the three core case studies, every other public page, research data, publications, and the existing resume.

## Editorial and visual changes

- **Work hierarchy:** Three core cases stay first, followed by a distinct **Independent Product Build** heading for FairPay AI. All four projects now use the same two-column editorial case-row layout, image proportions, CTA styling, and consistent low-motion Hover/Focus interactions. FairPay is not presented as equivalent in maturity to real clinical/product work.
- **No duplicate headline:** Removed the oversized “Applying product judgment beyond healthcare” title, repeated category label, extra boxed-card surface, and large surrounding shadow.
- **FairPay hero:** Replaced mixed-type hero counters (`3 / 161 / Sandbox`) with three qualitative capabilities. The `161 focused checks` remain accurately attributed to a local test run in the Testing & Limitations section.
- **FairPay breadcrumb:** The secondary project uses **Independent product build** instead of the misleading **Selected work / 04** label. The other three retain their original numbered sequence.
- **Three real application screenshots:** Overview, Agreements and Payments screenshots are now **hosted as WebP assets inside this website**, derived from the genuine product screenshot images embedded in the supplied exported FairPay case-study PDF. They are not AI-generated dashboards. Each one has a descriptive caption and an accessible click-to-enlarge `<dialog>` with Escape, close button, backdrop close, and focus restoration. The GitHub repo and video remain linked.
- **Readability:** Simplified repeated caveats, retained the separate `$50 vs $500`, blocking decision, and `$400 Sandbox draft` scenarios; improved small-font decision cards and desktop case navigation; highlighted the current case section.
- **Print:** Hide the focus-only Skip Link when printing a PDF; preserve it for normal keyboard users.
- **Compatibility:** Updated versioned styles, cache keys, and the verifier. The existing GitHub Pages workflow, Hugo version, base URL, and all unchanged case study sources are preserved.

## Deployment: full replacement, NOT a patch

1. Back up the current GitHub repository (V8.14) and, if editing a local Git clone, **preserve `.git/`**.
2. Remove the old website source files and copy all content from this ZIP directly into the repository root. **Do not nest the extracted folder**, and include `.github/`.
3. Optional local source check: `python3 scripts/verify_v815.py`.
4. Commit and push to `main`.
5. Check GitHub **Actions → Build and deploy**. Both `build` and `deploy` must succeed.
6. Open the home page, `/work/`, `/zh/work/`, `/work/fairpay-ai/` and `/zh/work/fairpay-ai/` and inspect desktop/mobile, Light/Dark modes, image zoom and links.
7. Verify the page source contains `<meta name="portfolio-version" content="8.15">` and `portfolio-v815.css`.

Do **not** delete the `static/images/projects/fairpay-*-v815.webp` screenshots: the website now serves them locally.

## Key URLs and evidence boundaries

- Project demo: https://www.youtube.com/watch?v=pivk3KyXpEQ
- GitHub source and docs: https://github.com/tai-tai-12/fairpay-ai
- Original public product tour: https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/PRODUCT_TOUR.md
- Validation limitations: https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/VALIDATION.md

FairPay is a local, synthetic-data hackathon prototype, **not** a production service, completed payment transaction, verified settlement, or award claim. `$50/$500` source-check, the blocked invoice scenario and the separate `$400 PayPal Sandbox DRAFT` are distinct examples. The `161` count reports focused checks at a particular local QA checkpoint, not users or live transactions.

## QA coverage and limits

- **320/320** source regression checks passed, including bilingual content and local screenshot assets.
- **40/40** offline Chromium preview configurations passed for Work/FairPay in English/Traditional Chinese at widths 1440, 1024, 768, 390 and 360 pixels in Light/Dark modes. No horizontal page or measured card overflow; assets loaded. The modal's Escape/Focus restoration was exercised in both languages.
- JavaScript syntax and CSS parser checks passed.
- Offline visual previews use captured HTML structure plus the actual V8.15 CSS/JS and locally embedded screenshots. **They are not a Hugo-generated production build**. This runtime cannot download or execute Hugo; the authoritative deployment/build acceptance is GitHub Actions.

The release-specific QA record is `V8_15_QA.md`. No historic generated browser preview HTML is shipped as a website page.
