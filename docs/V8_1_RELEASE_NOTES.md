# V8.1 Release Notes · Content & Provenance

## 1. Explicit user instruction: no Future Tech Award photograph

The source file `Material/Awards_Certificate/IMG_9931.JPG`, as well as the preview/source copy `future_award_source.jpg`, **is not included** in `static/`, content, or the deployment archive. V8.1 keeps the existing typographic project-recognition panel and adds two official external links, based on page language:

- EN: https://www.futuretech.org.tw/futuretech/index.php?action=product_detail&prod_no=P0008700008523&web_lang=en-us
- 繁中: https://www.futuretech.org.tw/futuretech/index.php?action=product_detail&prod_no=P0008700008523&web_lang=zh-tw

NYCU-led product/team recognition is explicitly distinguished from Tina's personal contribution. The official product profile describes DICOM/PACS, tumor detection, segmentation, five-class classification, brain-region localization, volume measurement, physician confirmation and LLM-assisted draft reporting. It **does not** establish which named individual implemented each platform subsystem. V8.1 therefore labels this as `Team platform capability` separately from `My contribution`.

## 2. Clinical AI — thesis metrics (not MIDL short-paper metrics)

Primary source: `Material/Paper/Tai_Thesis_Final_20260706.pdf`, English abstract, Chapter 3 ground-truth inter-rater agreement and Table 5.14.

- Retrospective two-center **264** MRI test examinations; **132 positive / 132 negative**; **226** reference lesions.
- Stage 0: **1,007 false positives**, **3.81 FP/scan**, **84.96% lesion-wise sensitivity**, **16.01% precision**.
- Final cascade: **55 false positives**, **0.21 FP/scan**, **80.97% lesion-wise sensitivity**, **76.89% precision**, **90.16% five-class accuracy on retained true positives**.
- False-positive candidate count reduction **94.54%**; sensitivity change **−3.99 percentage points**. True-positive retention **192** Stage-0 → **183** final = nine extra deleted true positives.
- Expert labels before consensus: Fleiss' κ **0.9416** tumor type, **0.9514** intra-/extra-axial label; mean segmentation Dice **0.8864**. These describe annotation agreement, not AI model performance.
- Secondary input-config comparison: T1C-only **73.89% sensitivity**, **0.09 FP/scan**, **88.62% retained-TP five-class accuracy** versus primary T1C+T2 **80.97%**, **0.21**, **90.16%**. The retained lesion subsets differ; typing metrics are conditional.

MIDL 2026 short paper is a distinct **249-exam** held-out cohort with 90.13% sensitivity, 0.41 FP/scan, 89.55% retained-TP typing accuracy; it must not be presented as the same cohort. Official MIDL program: https://2026.midl.io/scientific-program

The page now says explicitly that neither project proves prospective reader-time savings, reduction of clinical alert fatigue, improved patient outcomes, autonomous diagnosis or regulatory clearance.

## 3. NSTC source figures and support

Primary source: `Material/Paper/1122813CA49031E_merge.pdf` (44-page NSTC original study report).

- Figure 9 from PDF page 16 (multiplanar annotation/3D model) → `static/images/research/thoracic-aorta-multiplanar-annotation-v81.webp`.
- Figure 29 from PDF page 31 (ground truth and segmentation variant comparisons) → `static/images/research/thoracic-aorta-3d-results-v81.webp`.
- Images were tightly cropped from the original research figures, visually reviewed, and checked for obvious personal/patient identifiers. They are research illustrations, not medical product screenshots. No private original report is embedded in the deployment archive.
- 8-month undergraduate research support (2023–2024) and international conference travel support (AMLDS 2026) are stated as NSTC *grants/support*, not personal awards. Official grant paperwork remains private.

## 4. Credentials and publication links

- Google Ads Search credential record: https://www.credential.net/81142a9a-5143-4e81-97be-9354d8667e3e
- Google Ads Measurement credential record: https://www.credential.net/f2b46cae-5532-4190-80f1-9da00bf7dd7d
- IBM Relational Database Administrator Professional Certificate verification URL (printed on supplied PDF): https://www.coursera.org/verify/professional-cert/TEEVL5E2DS84
- Harvard CS50 AI: https://cs50.harvard.edu/ai/ (course information only; the original certificate does not provide a user-specific public verification URL)
- MIDL official program: https://2026.midl.io/scientific-program (search paper S-64 / Shih-Ting Tai)

User-private certificates, transcripts, educational identifiers, license scans and other raw material are not included. The URL destination of a credential verification page might require the destination site's scripts/sign-in depending on browser and provider.

## 5. Content scope and quality

- 11 EN pages + 11 ZH pages (same routes).
- V8.0 PDF Resume retained byte-for-byte (already updated to the supplied October 13 canonical version).
- Removed 22 images that had no direct references anywhere in deployed source code/templates/styles; original V7/V8 release documentation remains.
- Added `static/css/v81-evidence.css` and updated asset cache-busting to `?v=8.1.0`.
- GitHub Pages workflow runs V8.1 source verifier immediately before the Hugo build.
