# Tina Tai Personal Website — V8.16 (FairPay Evidence-First Work Redesign)

**Complete GitHub Pages/Hugo source replacement.** All required site files are at the ZIP root, including the hidden `.github/` workflow directory. This release is based on V8.15 and preserves the three core case studies, every other public page, research data, publications, and the existing resume.

## Editorial and visual changes in V8.16

- **Evidence-led visual:** FairPay's Work artwork is now **responsive HTML/CSS** rather than a text-dense three-panel SVG. An illustrative synthetic source-check highlights **AI suggestion $50 versus quoted source $500**, visibly marking the difference for human review. This is not a real client payment or the same scenario as the separate PayPal Sandbox draft.
- **Recruiter-facing detail:** The right side now shows three focused contributions: source traceability, human-controlled billing rules, and an inspectable prototype (three actual screens, public demo and documentation).
- **Consistent Work hierarchy:** The three proven core cases remain first; FairPay remains a clearly marked *Independent Product Build* in the same two-column editorial system, with unified hover/focus feedback. Slightly more generous visual widths at desktop help all cases.
- **Legible at narrow widths:** Big typographic amounts and real text that reflows, not small type flattened into an image. Bilingual page content adapts down to 320px, including Dark Mode and reduced motion.
- **New Open Graph previews:** Separate English/Traditional Chinese, **1200 × 628** PNG social thumbnails match the revised proof visual. FairPay's other locally hosted screenshots and detail-page Lightbox remain unchanged.
- **No factual expansion:** Three original product, AI and validation cases, existing research, Education, Experience, Resume, FairPay testing boundary, demo and links are preserved. The recorded 161 checks remain in Testing & Limitations, not mistaken for product uptake.
- **Versioning:** Versioned CSS and build verifier updated; GitHub Actions retains the established Hugo and Pages deployment approach.

## Deployment: full replacement, NOT a patch

1. Back up the current GitHub repository (V8.15) and, if editing a local Git clone, **preserve `.git/`**.
2. Remove the old website source files and copy all content from this ZIP directly into the repository root. **Do not nest the extracted folder**, and include `.github/`.
3. Optional local source check: `python3 scripts/verify_v816.py`.
4. Commit and push to `main`.
5. Check GitHub **Actions → Build and deploy**. Both `build` and `deploy` must succeed.
6. Open the home page, `/work/`, `/zh/work/`, `/work/fairpay-ai/` and `/zh/work/fairpay-ai/` and inspect desktop/mobile, Light/Dark modes, image zoom and links.
7. Verify the page source contains `<meta name="portfolio-version" content="8.16">` and `portfolio-v816.css`.

Do **not** delete the `static/images/projects/fairpay-*-v815.webp` screenshots: the website now serves them locally.

## Key URLs and evidence boundaries

- Project demo: https://www.youtube.com/watch?v=pivk3KyXpEQ
- GitHub source and docs: https://github.com/tai-tai-12/fairpay-ai
- Original public product tour: https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/PRODUCT_TOUR.md
- Validation limitations: https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/VALIDATION.md

FairPay is a local, synthetic-data hackathon prototype, **not** a production service, completed payment transaction, verified settlement, or award claim. `$50/$500` source-check, the blocked invoice scenario and the separate `$400 PayPal Sandbox DRAFT` are distinct examples. The `161` count reports focused checks at a particular local QA checkpoint, not users or live transactions.

## QA coverage and limits

- **328/328** source checks passed, JavaScript syntax valid, CSS parsed without errors, and local Hugo assets referenced by the templates exist.
- **44/44** Playwright/Chromium responsive spot checks passed (English/Traditional Chinese, Light/Dark modes; 320–1440px), checking viewport and inner-card bounds. Work graphic screenshots are retained separately in the conversation, not shipped in the site ZIP.
- FairPay detailed-page image Lightbox was retained from previously tested V8.15; the new work image remains a normal clickable case-study link.
- **Official Hugo build could not run in this isolated container** because the runtime has no Hugo binary and cannot resolve GitHub release downloads. Do not claim the source QA substitutes for the GitHub Actions build/deploy checks.

The release-specific record is `V8_16_QA.md`; do not commit the temporary preview HTML/Python scripts in `/mnt/data` to the repository.
