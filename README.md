# Tina Tai Personal Website — V8.0

**Release date:** October 2026  
**Focus:** PM-first portfolio, source-grounded updates, bilingual consistency, readable evidence, deployable Hugo source.

## What's new / 本版重點

| Area | V8.0 changes |
|---|---|
| Resume / 履歷 | Replaced public Resume PDF with the supplied **October 13, 2026 General PM Resume**, at the existing URL (`/resume/Shih-Ting_Tai_Resume.pdf`). |
| Product / 產品 | Recognizes **DeepBT A+ · 2026 Future Tech Award** as an NYCU-led *project/team* award, not an individually won award; adds attribution in the case study, Work preview and Experience. |
| Model evaluation / AI 評估 | Introduces outcome-first **94.5% reduction in false-positive candidates (1,007 → 55)** on **264 independent MRI cases**, clarifying that this is not a change in sensitivity. Keeps denominator-aware 80.97% sensitivity and 90.16% retained-TP classification accuracy. |
| NTUH / 臨床實習 | Shows **1,040 hours / 26 weeks**, 3 clinical rotation areas, and the existing Certificate of Excellence. |
| CMU / 卡內基美隆 | Adds selected *current Fall 2026 courses* and distinguishes them from completed courses; clarifies MSBA Student Ambassador 2026–27. |
| NYCU / 陽明交通大學 | Reassigns MRI, deep-learning and medical-device-regulation coursework to the B.S.; limits master's listed courses to graduate coursework. |
| Certifications / 專業證書 | Adds **Google Ads Search & Measurement** and **IBM Relational Database Administrator Professional Certificate** to the selected training inventory without publishing all certificates. |
| Thoracic aorta / 胸主動脈 | Adds **eight-month NSTC-funded** duration and **3D U-Net**. |
| Usability / 介面 | Adds restrained editorial award panel, accessible evaluation bars, mobile CSS, keyboard skip link, reduced-motion compatibility, more resilient theme/menu interactions and `V8.0` asset cache versions. |
| Privacy / 隱私 | No original transcript, license scan, test score, degree, ID or raw Material archive is included. |

This is the complete **Hugo source repository**, not a pre-rendered HTML export. The original GitHub Pages Actions workflow and published URL structure are preserved.

## Deploy / 部署至 GitHub Pages

1. Unzip the distribution. Work from the `tina-personal-website-v8/` folder, which contains `hugo.toml` and `.github/workflows/hugo.yaml`.
2. Copy the contents of that folder (including hidden `.github`) into the existing `tina-personal-website` repository, preserving GitHub repository settings.
3. Commit and push changes to `main`. The existing GitHub Actions workflow will install Hugo, build and deploy the site.
4. In repository Settings → Pages, confirm that the source is **GitHub Actions**.
5. After successful workflow completion, check the English and Chinese pages and open the public Resume button to confirm the PDF has updated. If cached, hard-refresh.

**Local checks (Hugo installed):**

```bash
python3 scripts/verify_v8.py
hugo server -D
# open http://localhost:1313/tina-personal-website/

hugo --gc --minify --baseURL "https://tai-tai-12.github.io/tina-personal-website/"
```

The automated Actions workflow currently uses Hugo **0.164.0**. If using a different local Hugo version, prefer this version for parity with GitHub Pages. Do not place the private `Material` archive in `static/` or commit any original transcript/certificate documents.

## Structure

- `content/en`, `content/zh`: paired content pages and case studies
- `layouts/`: page templates and shared components
- `static/css/v8-refresh.css`: V8 style refinements, loaded after V7 styles
- `static/resume/Shih-Ting_Tai_Resume.pdf`: canonical downloadable resume
- `static/research/publications/`: existing selected public research artifacts
- `scripts/verify_v8.py`: reproducible offline source/asset checks
- `docs/V8_0_RELEASE_NOTES.md`: change rationale and evidence decisions
- `docs/V8_0_QA.md`: source validation results and known limits

## Editorial principles / 內容原則

- Prioritize product judgment and measurable outcomes ahead of technical jargon.
- State denominators and cohort scopes for AI metrics; never conflate sensitivity, precision, classification accuracy or false-positive reduction.
- Attribute awards accurately: team/project recognitions are not personal awards.
- Show only selected credentials on the public site. Keep private evidence in a separate vault.
- Preserve English / Traditional Chinese parity while writing natural copy for each audience.
