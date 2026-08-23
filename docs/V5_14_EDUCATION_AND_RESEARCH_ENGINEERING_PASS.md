# V5.14 — Education Curation & Research Engineering Pass

## Why this pass exists
This pass addresses four issues:
1. page-context labels repeated the H1 titles,
2. the NYCU seal had too much white padding and looked smaller than the CMU mark,
3. the Education page underrepresented honors and credentials,
4. substantial technical/research engineering work was not visible anywhere on the portfolio.

## 1. Page context labels
Context labels are now complementary rather than repetitive:
- Experience → CAREER PATH
- Education & Credentials → ACADEMIC BACKGROUND
- Research & Recognition → SELECTED RESEARCH
- Selected Work → PORTFOLIO
- About → PROFILE

Individual project pages still use their project category labels.

## 2. NYCU seal crop
`static/images/education/nycu-seal.png` was tightly cropped around the emblem, removing most of the white canvas around the original asset.
CMU and NYCU seals now share the same display dimensions.

## 3. Honors & credentials curation
The previous single-license panel is now a curated `HONORS & CREDENTIALS` panel with three groups:

### Professional license
- Licensed Medical Radiation Technologist — Taiwan Ministry of Health and Welfare, 2024

### Selected honors
- Outstanding Thesis Award — NYCU, 2026
- Outstanding Oral Presentation — IEEE AMLDS, 2026
- Honor Student Award — NYCU, 2024
- Certificate of Excellence — NTU Hospital clinical internship

### Selected technical credentials
- Data Science & Smart Instrumentation — NYCU, 2026
- CS50's Introduction to AI with Python — Harvard / CS50, 2025
- Data Science Fundamentals with Python & SQL — IBM, 2025
- Fundamentals of Visualization with Tableau — UC Davis, 2026

The site intentionally does not list every IBM / Google certificate. The full inventory belongs on LinkedIn; the personal site should remain curated.

## 4. Research Engineering section
A new Research Engineering section exposes supporting technical work that previously stayed invisible behind the final model outputs:
- 3D vascular reconstruction & segmentation
- ANTs registration and spatial preprocessing
- ground-truth consensus workflows
- dataset standardization and hospital-format conversion
- radiomics / segmentation / classification experiments

These are framed as technical capabilities and supporting workflows, not as five new flagship portfolio projects.

## 5. Clinical AI case-study update
The Clinical AI case study now includes a `Research engineering behind the model` section, explaining that the final cascade was supported by registration, consensus-data management, data-conversion utilities, and alternative modeling experiments.

## Design principle
The website should show enough technical depth to distinguish Tina from a generic PM/analytics profile without turning the portfolio into a source-code directory or certificate archive.
