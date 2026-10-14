# Tina Tai — V8.0 Release Notes / 改版說明

**Date:** 2026-10-13  
**Baseline:** User-supplied V7.0 deployment ZIP  
**Sources:** User-supplied Material archive; pasted audit/plan; October 13, 2026 General PM resume PDF.

## Source of truth / 事實基準

- Resume career metrics follow the supplied one-page General PM Resume dated October 13, 2026. The public PDF is an exact binary copy.
- All newly displayed certifications and the Future Tech Award were cross-checked against user-supplied evidence, including the 2026/09/19 award photograph and credential materials.
- Degree-level attribution follows NYCU transcript provenance documented in the supplied audit.
- Personal data in the original certificate, transcript, degree and exam documents is not placed into the published `static/` folder.

## Page-by-page changes / 各頁更新

**Home / 首頁**
- Work 01: stronger distinction between faster throughput and **~67% reduction in processing time** (~120 seconds → ~40 seconds).
- Work 01: restrained DeepBT A+ team award caption below the main evidence rail.
- Work 02: headline proof prioritizes **94.5% fewer false-positive candidates**, **264 independent MRI tests**, **90.16% five-class accuracy**.
- Existing hero portrait and work imagery retained to preserve visual consistency.

**Work / 專案**
- Medical AI Product: added independent team/project recognition callout; clearly labels NYCU-led DeepBT A+ Future Tech Award; maintains TFDA submission **execution**, not approval, and prior Connectathon context.
- Clinical AI: evidence bars contrast **1,007 false-positive candidates at Stage 0** with **55 after the full cascade** for the same 264-case independent cohort. Bars are drawn to scale; both raw values and denominator are visible in text. The comparison does *not* assert improvement in sensitivity.
- Regulated Validation: retains the established independent client/testing story without adding unrelated certificates.

**Experience / 經歷**
- AITEWAN: team recognition as a small contextual statement, not a new personal award.
- NTUH: **26 weeks / 1,040 hours** plus diagnostic imaging, radiation oncology and nuclear medicine. Internship excellence remains a separate credential.
- Reordered the detailed timeline in most-recent-start order to align with the resume.

**Education / 學歷**
- CMU: explicitly *current Fall 2026 coursework* — Machine Learning Fundamentals, Modern Data Management, Programming in R & Python, Statistical Foundations for Business Analytics. No completed-grade claim.
- NYCU M.S.: Machine Learning & Biomedical Applications; Introduction to Photonics Engineering.
- NYCU B.S.: Programming Language, Deep Learning & Biomedical Applications, Principles of Magnetic Resonance Imaging, Medical Device Regulatory Requirements.
- Selected additional training: Google Ads Search & Measurement (2026), IBM Relational Database Administrator Professional Certificate (2025), IBM Data Science Fundamentals, CS50 AI, UC Davis Tableau, NYCU Data Science & Smart Instrumentation.
- The full list of IBM/Coursera course certificates, Gemini Educator, GPA, rank and admissions tests remain outside the public portfolio, intentionally.

**Research / 研究**
- Thoracic-aorta deep-dive: eight-month NSTC funding and 3D U-Net method added; original 308 CT / 0.95 mean AUC / 0.782 DSC metrics unchanged.
- Research awards grid remains for individual thesis/oral recognition; the Future Tech Award is not portrayed as an individual research award.
- MIDL / AMLDS / TSBME publication listings unchanged; no assertion of IEEE indexing made.

**Interface & maintenance / 介面與維護**
- `v8-refresh.css`: editorial award feature, false-positive comparison chart, responsive and high-contrast states, consistent keyboard focus.
- `site.js`: safely handles browsers without persistent localStorage; Escape closes mobile menu; reduced-motion setting respected.
- Site contact email aligned with the newly supplied resume (`tinatai@tepper.cmu.edu`); a bilingual 404 fallback has been added.
- `baseof.html`: a visible-on-focus keyboard skip link and one page-level `<main>` landmark (corrects case-study nested main).
- CSS/JS cache keys and portfolio version set to 8.0; no route or file naming changes affecting existing public links.

## Explicit editorial exclusions / 不上架的資料

GMAT, IELTS, numeric NYCU GPA, class rank, private transcripts, degree certificates, professional-license original, internship original certificate, and the entire Material ZIP are excluded from public downloads. These can remain in a private application evidence bank.
