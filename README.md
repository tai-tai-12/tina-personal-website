# Tina Tai Personal Website — V8.14 (FairPay AI Independent Product)

This ZIP is a **complete replacement** for V8.13.4. Files live directly at the ZIP root; do not upload the ZIP itself as a site file or nest its contents inside another folder.

## What changed

- **Work** retains its original **three featured case studies** in the existing order. A distinct **Independent Build · AI Product** section now introduces **FairPay AI — Evidence-Led Billing** below them.
- Added an English and Traditional Chinese FairPay AI project page at `/work/fairpay-ai/` and `/zh/work/fairpay-ai/`.
- The case covers the billing problem, three product design decisions, real product screens hosted in the [public FairPay GitHub repository](https://github.com/tai-tai-12/fairpay-ai), a three-minute demo, the reported focused QA run, and explicit prototype limitations.
- Added a **self-contained, bilingual illustrative workflow SVG + PNG** for the Work thumbnail and share preview. No AI-generated fake product screenshots were created. Real product screenshots are included **by public repository URL** (not duplicated inside this ZIP); these will load while the original public repository remains available. Links to the original screenshots and product tour are also provided.
- Updated the version marker, stylesheet names, Open Graph image for FairPay, and the CI verification script.
- No changes to the homepage's three featured cases, Experience, Education, Research, About, resume, existing cases, research metrics, or official publication links.

## Deploy by full replacement

1. Back up the existing V8.13.4 repository state. If using a local Git clone, **preserve `.git/`**.
2. Remove the old website source files in the repository (leave `.git/` untouched); copy **every file/folder from this ZIP** to the repository root, including the hidden `.github/` directory.
3. Run `python3 scripts/verify_v814.py` locally if Python 3 is installed.
4. Commit and push all changed files to `main`.
5. Confirm GitHub Actions **Build and deploy** has green `build` and `deploy` jobs. The workflow runs the verifier before the Hugo build.
6. Verify page source contains `<meta name="portfolio-version" content="8.14">`.
7. Open `/work/` and `/zh/work/`; follow the FairPay card to `/work/fairpay-ai/` and `/zh/work/fairpay-ai/`. Confirm three product images, demo, GitHub, and docs links work.

## FairPay links

- [Three-minute video](https://www.youtube.com/watch?v=pivk3KyXpEQ)
- [Source and README](https://github.com/tai-tai-12/fairpay-ai)
- [Actual product screenshots](https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/PRODUCT_TOUR.md)
- [Validation scope and known limitations](https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/VALIDATION.md)

**Scope:** FairPay AI is a local, synthetic-data hackathon prototype. It does not process real payments, validate bank settlement, provide a hosted merchant platform, or claim production adoption. The $50/$500, blocked-invoice, and separate $400 PayPal Sandbox draft examples are distinct scenarios.

## Verification limits

The included verifier checks source files, links, Hugo template text, CSS parseability, translation assets, and preserved case-study evidence. Offline Chromium previews covered the new Work section and case layouts in English/Traditional Chinese at four common widths. The previews use local placeholder illustrations in place of the externally hosted original FairPay screenshots only for offline layout checks. **They are not Hugo renders.** Hugo itself is unavailable in this container; the production GitHub Actions build and public-page QA are required for final verification.
