# V5.16 — Research & Experience Architecture Pass

## Goal
Clarify the boundary between research outputs, awards, research engineering, earlier research, regulated third-party testing, and quantitative-imaging work.

## Research page
- Featured Research now contains only MIDL 2026 and IEEE AMLDS 2026 research outputs.
- Outstanding Oral Presentation is moved into a separate Recognition section together with the Outstanding Thesis Award.
- Research Engineering is reframed as **Beyond model training** and focuses on four transferable technical areas:
  - data engineering / hospital-format conversion
  - ANTs-based spatial preprocessing
  - expert-consensus / ground-truth design
  - radiomics, segmentation, classification, and alternative-model experimentation
- Thoracic-aorta CT work is removed from the Research Engineering grid and promoted into a separate **Earlier Research** feature.
- A dedicated thoracic-aorta CT visual is included.

## Experience page
### AITEWAN
Maintains a concise featured product role with related case-study link.

### AIMISAL / Prof. Yu-Te Wu
- Adds the AIMISAL / Prof. Wu lab link.
- Replaces the single brain-tumor-only narrative with three selected research areas:
  - Brain Tumor MRI AI
  - Thoracic Aorta CT
  - Research Engineering across projects

### BIPI / Prof. Jyh-Cheng Chen
- Removes generic `WORKSTREAM 01 / 02` language.
- Uses **Scope of Work** with two clearly distinct areas:
  - Regulated Testing — Third-Party Testing & Consortium Operations
  - Quantitative Imaging — MATLAB Small-Animal CT Analysis
- Keeps the Prof. Chen lab link.

### NTUH
Remains compact to preserve hierarchy.

## Third-Party Testing case study
- Removes the PDF-crop collage as the hero visual.
- Uses a conceptual portfolio illustration of the workflow: **Test → Measure → Document → Review**.
- Explicitly states that the illustration is conceptual and is not a reproduction of a client report or specific testing setup.
- Refocuses the case study on testing, evidence traceability, reporting, consortium operations, and quality-system work.
- Moves MATLAB small-animal CT analysis into a short **Related quantitative imaging work** section rather than treating it as part of the testing-report workflow.

## New visual assets
- `static/images/projects/third-party-testing-workflow.webp`
- `static/images/research/research-engineering.webp`
- `static/images/research/thoracic-aorta-ct.webp`

The source PNG files were converted to high-quality WebP for faster loading.

## Homepage / Work page
- Project 03 now uses the new testing workflow illustration instead of the documentary PDF collage.
- Homepage research-role summary now reflects both brain-tumor MRI and earlier thoracic-aorta CT work.

## Styling
New V5.16 styles add:
- two-card Featured Research layout
- separate Recognition treatment
- centered research-engineering visual + 2×2 technical capability grid
- Earlier Research feature
- differentiated Experience role hierarchy
- Selected Research grid for Prof. Wu / AIMISAL
- Scope of Work grid for Prof. Chen / BIPI
