# Personal Website V5.2 — Visual Consistency Pass

## What changed

### 1. Selected Work now uses one visual system
All three homepage projects use the same visual grammar: warm-white surface, light blue grid, deep/electric blue, 1.5px outline icons, consistent spacing, and comparable visual height.

- Project 01: Product Translation — PACS → AI → Evidence → Deployment
- Project 02: Lesion-Wise AI Cascade — Stage 0 → Stage 1 → Stage 2, with cohort and final-thesis evaluation signals
- Project 03: Structured Decision System — Evidence → Decision → Action

The large raster infographic is no longer used as the homepage thumbnail. Full case-study diagrams are now SVG so they remain crisp on Retina/4K displays.

### 2. Data-scope wording was corrected
Homepage credibility signal:
- `12K+ MRI Exams`
- `Development cohort · 2 centers`

Project 02 explicitly distinguishes:
- 12,125 development MRI examinations / 23,341 annotated tumor lesions
- 264 independent clinical test examinations / 226 annotated lesions
- 2 medical centers

Headline final-thesis independent-test metrics:
- 80.97% lesion-wise sensitivity
- 0.21 FP/scan
- 76.89% precision
- 90.16% retained-lesion five-class accuracy

This avoids implying that 10K+ cases were the independent test set.

### 3. Project 01 and Project 02 have different jobs
Project 01 is now product/clinical-translation first:
- 2 medical centers
- TFDA submission
- PACS-connected workflow
- stakeholder / validation / product execution

Project 02 is technical/evaluation first and carries the final-thesis cohort metrics.

### 4. Research page was redesigned
The Research page now has:
1. Featured MIDL research card
2. Featured AMLDS oral-presentation card
3. Dedicated Outstanding Oral Presentation recognition block
4. Editorial publication list
5. Compact research-theme tags

### 5. High-resolution research photos
Re-exported from the new source images at higher quality:
- `static/images/research/midl-poster.webp`
- `static/images/research/amlds-talk.webp`
- `static/images/research/amlds-award.webp`

## Updating the live site
Copy the contents of this V5.2 folder into the existing `tina-personal-website` local repository, replace same-name files, then:

1. Commit: `Apply V5.2 visual consistency pass`
2. Push origin
3. Wait for GitHub Actions → Build and deploy ✅
4. Hard refresh the live site (`Cmd + Shift + R` on Chrome for Mac)

No GitHub Pages or custom-domain settings need to be changed.
