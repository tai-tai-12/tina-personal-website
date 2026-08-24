# V5.17 — Full-Site QA & Readability Pass

This release is based on the complete V5.16 package and incorporates live-site QA plus the latest Experience, Research, Education, About, and Work feedback.

## Release blockers / consistency fixes

- Keeps the V5.16 Prof. Yu-Te Wu / AIMISAL lab link in the Experience page.
- Keeps the V5.16 separation between research outputs and recognition.
- Removes the Education `HOW IT CONNECTS` strip, which repeated the site narrative and looked visually simplistic.
- Crops the Third-Party Testing visual to the four core workflow panels only; removes the large infographic title/footer from portfolio cards.
- Standardizes all three Work visuals to the same wide aspect ratio and visual frame.

## Research

### Featured Research
- Two equal desktop cards: MIDL 2026 and IEEE AMLDS 2026.
- Media containers now center each photo correctly.
- MIDL and AMLDS remain research outputs only.

### Recognition
- Outstanding Oral Presentation is presented as an award, not as a third research output.
- Outstanding Thesis Award appears as a second recognition row.
- This avoids the appearance that AMLDS is duplicated.

### Research Engineering
- Removed the oversized generated infographic from the page flow.
- Replaced it with a readable 2×2 icon-led matrix:
  - Data engineering
  - Spatial preprocessing
  - Ground-truth design
  - Model experimentation

### Earlier Research
- Thoracic-aorta CT remains an independent earlier research project, rather than a supporting subtask of the brain-tumor model.

## Experience

### AIMISAL / Prof. Yu-Te Wu
- Preserves the explicit `Prof. Yu-Te Wu / AIMISAL ↗` lab link.
- Preserves the three-area structure: Brain Tumor MRI AI, Thoracic Aorta CT, and Research Engineering.

### BIPI / Prof. Jyh-Cheng Chen
- Uses `SCOPE OF WORK`, with descriptive labels rather than `WORKSTREAM 01 / 02`.
- Keeps third-party testing and MATLAB quantitative CT as distinct responsibilities.

### National Taiwan University Hospital
- Expanded the compact entry without giving it the same visual weight as the two featured research roles.
- Adds the three clinical rotation areas:
  - Diagnostic Imaging
  - Radiation Oncology
  - Nuclear Medicine
- Surfaces Certificate of Excellence as a distinct recognition item.

## Education

- Removes `HOW IT CONNECTS` entirely.
- Rationale: the same imaging → AI → product → analytics story already appears in the homepage, About page, and Education introduction, so the bridge repeated information without adding recruiter value.

## About

### Capabilities
- Replaces dense dot-separated skill paragraphs with four 2×2 icon-led capability cards.
- Each capability now uses three readable sub-points instead of a long keyword string.
- Adds a concise cross-functional note covering collaboration across hospital, academic, and startup environments.

### Leadership & Community
- Replaces the vague `Beyond Work` section with a more recruiter-relevant `Leadership & Community` section.
- Selected items:
  - Department Student Association · President
  - National High School Medical Camp
  - University & Department Basketball Team Manager
  - Lions Club
- Earlier sign-language, dance, Rotary, animal-welfare, and personal interests remain a short closing note rather than becoming a long activity inventory.

## Work visual consistency

- Third-party testing visual is cropped to the four core panels: Test → Measure → Document → Review.
- The large infographic heading and footer are removed from the portfolio-card asset.
- All three project images now use the same 1500×560 display ratio, border treatment, radius, and image fitting.
- Product and Clinical AI visuals remain domain-specific, but framing is intentionally unified rather than forcing identical illustration styles.

## Deployment

Use this as a complete replacement package. Copy all files inside the V5.17 directory into the existing repository and replace same-name files. Do not delete `.git`.

Suggested commit:

`Apply V5.17 full-site QA and readability pass`
