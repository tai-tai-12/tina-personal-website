# V5.18 — Research Visual & Architecture Pass

## Goals
This pass addresses four issues from V5.17:
1. Recognition needed the actual award-receiving photos and smaller, more balanced image treatment.
2. Research Engineering needed stronger visual hierarchy and more recognizable visual cues.
3. The thoracic-aorta CT project was too easy to miss at the bottom of the Research page.
4. Selected Work visuals needed one consistent visual language and the homepage Research cards needed equal sizing.

## Research & Recognition
### Research Areas first
The page now introduces two research areas immediately after the page hero:
- Brain Tumor MRI AI — 2024–2026
- Thoracic Aorta CT Analysis — 2023–2024

This makes the research breadth visible before the user scrolls through conference outputs.

### Featured Research Outputs
MIDL 2026 and IEEE AMLDS 2026 now use equal-size cards and equal image frames.

### Recognition
Two compact award cards now use real photos supplied by Tina:
- Outstanding Oral Presentation — IEEE AMLDS 2026
- Outstanding Thesis Award · First Place — NYCU 2026

The photos are intentionally kept smaller than the research-output photography so Recognition reads as an award section, not a duplicate research gallery.

### Beyond model training
The 2×2 text-heavy grid is replaced by four stacked editorial rows:
- Data Engineering
- Spatial Preprocessing
- Ground-Truth Design
- Model Experimentation

Each row includes a small line illustration, a clear title, a one-sentence explanation, and compact technical tags.

### Thoracic Aorta CT
The project is introduced near the top in Research Areas, then revisited later in a compact detail section with 308 CT scans, Mean AUC 0.95, and Overall DSC 0.782.

## Selected Work visuals
All three portfolio visuals now use the same dark clinical/technical visual language and the same 1500×560 crop:
- Product Translation: AI-assisted MRI review environment
- Clinical AI · ML: lesion-focused MRI analytics dashboard
- Regulated Testing · Operations: measurement and validation laboratory

There are no titles embedded in the images, and no large white poster-like margins.

## Homepage Research
MIDL and AMLDS tiles now use equal columns and equal 4:3 image frames. This resolves the previous imbalance caused by portrait-vs-landscape source images.

## Deployment
Replace the contents of the existing repository with the contents of this V5.18 folder while preserving the repository's `.git` directory, then commit and push.
