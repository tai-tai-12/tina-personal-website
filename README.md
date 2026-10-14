# Tina Tai Personal Website — V8.1

**Release:** October 2026 · **Project:** Bilingual Hugo portfolio · **Positioning:** Product Management first, AI/ML & Analytics second, Healthcare as a differentiator.

V8.1 refines V8.0 using primary-source research evidence, public project listings and credential records. **Do not deploy the private `Material(4).zip` or original certificates.** This archive contains the complete Hugo source, theme, public-selected research artifacts, images, current Resume, GitHub Pages workflow and release checks.

## What's new / V8.1 更新

- **2026 Future Tech Award:** official public team/project page links in English and Traditional Chinese. **The original award photo was intentionally excluded at the user's request.** The existing understated FT typographic block remains, not an official medal graphic.
- **Medical AI Product:** accessible five-stage DICOM/PACS → lesion analysis → physician confirmation → LLM-assisted draft reporting → clinical review schematic, with explicit separation of **team capabilities** and **Tina's actual contributions**. The figure is illustrative, not a system UI screenshot.
- **Clinical AI:** two-dimension trade-off visualization for the same 264-case retrospective cohort; 1,007 → 55 false-positive candidates (−94.54%) alongside 84.96% → 80.97% lesion-wise sensitivity (−3.99 percentage points). Precision 16.01% → 76.89% is also reported.
- **Research methodology:** pre-consensus agreement (Fleiss' κ and Dice), T1C-only secondary analysis with exact denominators, and clear distinction from the separately published MIDL 249-exam cohort. No prospective clinical gains or regulatory clearance are claimed.
- **Actual research figures:** two de-identified research illustrations (Figure 9 / Figure 29) from the original NSTC thoracic-aorta research report. They are labeled as research figures, not synthetic illustrations or deployed product screenshots.
- **Research support:** separate, compact NSTC undergraduate research grant and international conference travel support; not framed as competition awards.
- **References:** official MIDL 2026 program; public FUTEX DeepBT A+ profiles (language appropriate); credential verification for Google Ads Search, Google Ads Measurement and IBM DBA. Harvard CS50 links to the **official course description**, not an invented personal verification record.
- **Release quality:** V8.1 CSS, English/Traditional Chinese consistency, orphan image pruning, GitHub Pages workflow source validation and a reproducible QA script.

All major V8.0 additions—October 13 General PM Resume, current CMU coursework, NYCU coursework corrections, 1,040-hour internship and selected credentials—remain preserved.

## Deployment / GitHub Pages 部署

1. Extract the ZIP. Copy **the contents** of the root `tina-personal-website-v8-1/` into the existing `tina-personal-website` repository, including hidden `.github/`.
2. Commit and push to `main`. Your existing Pages configuration must have **Source: GitHub Actions**.
3. `.github/workflows/hugo.yaml` first runs `python3 scripts/verify_v81.py`, then installs Hugo 0.164.0, builds the site and deploys it.
4. Check the deployed EN and 繁體中文 product/research case studies and open the public Resume link. Hard-refresh for the `?v=8.1.0` CSS cache revision.
5. Before sharing widely, visually QA at least one desktop and one phone viewport and verify that external credential links are publicly accessible without account sign-in.

### Local validation

```bash
python3 scripts/verify_v81.py
hugo version                # Hugo 0.164.0 recommended for deployment parity
hugo --gc --minify --baseURL "https://tai-tai-12.github.io/tina-personal-website/"
hugo server -D
```

**Build status in authoring environment:** source and asset checks are completed; the machine used to prepare this archive had no Hugo executable and cannot fetch one through its network. Final Hugo build and actual browser screenshot validation must therefore run on GitHub Actions or locally. Do not treat the source check as an equivalent to a successful Hugo build.

## Directory guide

- `content/en/`, `content/zh/`: paired 11-page content sets
- `layouts/`: Hugo templates
- `static/css/v81-evidence.css`: incremental evidence & mobile design
- `static/images/research/thoracic-aorta-*-v81.webp`: cropped source figures
- `static/resume/Shih-Ting_Tai_Resume.pdf`: supplied October 13 Resume (unchanged)
- `static/research/publications/`: selected existing public research PDFs
- `scripts/verify_v81.py`: offline checks, also run in deployment workflow
- `docs/V8_1_RELEASE_NOTES.md`: claim-level documentation and source links
- `docs/V8_1_QA.md`: checks performed, what remains

## Editorial policies

Preserve evidence scope and fair attribution. Research performance ≠ completed prospective clinical validation; software feature description ≠ personal implementation of every subsystem; project/team recognition ≠ an individually conferred award. Never expose raw medical test screenshots, research identifiers, student/transcript details, license scans or private credential documents.
