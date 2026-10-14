# Tina Tai Personal Website — V8.2

**Release:** October 2026  
**Theme:** Full Visual Refinement & Design System Consolidation  
**Positioning:** Product Management first; AI/ML & Analytics second; Healthcare as a differentiator.

This is the **complete, bilingual Hugo source project** for an existing GitHub Pages portfolio. V8.2 is a visual refactor of V8.1, not a new site or new claim set. It retains existing routes, the current October 13 general PM resume, primary-source-backed project evidence, links to official recognition, selected research figures, and EN / 繁體中文 content.

## What changed / 這次更新

- **Single stylesheet entry point:** 8 legacy CSS files are concatenated in cascade order into `static/css/portfolio-v82.css`. A clearly identified V8.2 design-system section sets coherent typography, whitespace, figures, metadata, and breakpoints. The 8 originals are preserved for developer reference under `docs/legacy-styles/` and are not published as separate CSS assets. Some historical selectors remain inside the consolidated file for visual and functional compatibility; this is not a full removal of every old selector.
- **Fixed Future Tech recognition layout:** replaced the broken flex-based mixed inline text with a vertical, semantic recognition module (project/team award, not individual). The user-excluded non-scanned award photograph was **not** included.
- **Homepage:** true two-column Experience timeline, dates and labels that can be read at a glance, NTUH internship added, normalized Selected Work figures, matching MIDL/AMLDS mini-cards, more structured About narrative and four concise foundations.
- **Research:** selected publications presented near the top ahead of image-heavy presentation cards, consistent smaller photo crops, readable publication dates and captions, clearer hierarchy for recognition, methods and NSTC support.
- **Experience / Education / Work:** reduced oversized headings, improved body widths and metadata, simplified repeated scope decoration, consistent research/coursework/credential presentation, bounded work-card images.
- **Case studies:** consistent reading measure and headings, accessible three-phase team-product workflow, one integrated clinical FP/sensitivity trade-off presentation (no duplicate FP-only chart), research figures shown without excessive width, more legible diagram labels.
- **Responsive design:** intended adaptations at desktop, 1050px, 760px and 480px, including stacked mobile timeline, single-column case flow and editorial research tiles.
- **Deployment:** `scripts/verify_v82.py` runs in the GitHub Pages workflow before Hugo build; cache version `8.2.0`.

## Deployment / GitHub Pages 部署

1. Unzip this package. Copy **the contents** of `tina-personal-website-v8-2/` into the root of the existing `tina-personal-website` repository. Include hidden `.github/` files. Delete any old V8.1 files in the repository that are absent from V8.2, especially old CSS files under `static/css/`.
2. Commit and push to `main`; Pages Source must remain **GitHub Actions**.
3. The workflow runs `python3 scripts/verify_v82.py`, installs Hugo 0.164.0, compiles the site and deploys `public/`.
4. Confirm green GitHub Actions results, then hard-refresh the published site to pick up `?v=8.2.0`.
5. Perform live visual review at widths **1440, 1024, 768, 390, 360px** in both English and Traditional Chinese, light/dark, and test navigation, section anchors, official links, and Resume download.

### Local development

```bash
python3 scripts/verify_v82.py
hugo version
hugo --gc --minify --baseURL "https://tai-tai-12.github.io/tina-personal-website/"
hugo server -D
```

**Verification limits:** the authoring environment had no Hugo binary and blocked both browser navigation and downloading an executable. We verified static content, asset references, CSS parse, JavaScript syntax, the PDF hash and ZIP integrity; **we did not obtain a successful Hugo build or actual pixel-level desktop/mobile screenshots here**. These remain necessary deployment acceptance gates. See `docs/V8_2_QA.md`.

## Key files

- `layouts/`: customized Hugo templates for all pages
- `content/en/`, `content/zh/`: bilingual case studies and research detail content
- `static/css/portfolio-v82.css`: the only public CSS file
- `docs/legacy-styles/`: archived old CSS source files for traceability
- `static/images/`: selected publicly presentable assets, including genuine research figures
- `static/resume/Shih-Ting_Tai_Resume.pdf`: unchanged October 13 resume
- `static/research/publications/`: public-facing publications/poster PDFs
- `scripts/verify_v82.py`: offline source validation, also runs in Actions
- `docs/V8_2_RELEASE_NOTES.md`: release details and design choices
- `docs/V8_2_QA.md`: test status and remaining visual sign-off

## Evidence and privacy

Do not publish the private `Material(4).zip`, transcripts, degree certificates, raw clinician/FHIR screenshots, professional license originals, or the Future Tech Award non-scanned photograph. Keep research metrics scoped to their evaluated cohort and project awards attributed to the project/team. No clearance, prospective effectiveness or individual implementation of all product features is claimed.
