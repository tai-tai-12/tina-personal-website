# V6.3 — Unified Editorial System & Research Architecture

## Release goal
Establish one coherent visual grammar across Experience, Education, Research, Work, About, and Footer; improve readability and recruiter scanning; and restructure Thoracic Aorta as a secondary but fully credible foundational research project.

## System-level changes
- Added a final V6.3 typography/readability layer with shared page-header, timeline, definition-row, recognition, figure, link, and button rules.
- Kept semantic hierarchy while increasing supporting metadata readability.
- Matched Experience and Education timeline grids more closely.
- Standardized definition/scope rows across product, research, and academic sections.
- Preserved recognition hierarchy: major awards on Research; inline recognition in Experience/Education.
- Standardized homepage project-proof rows and About foundations.
- Refined footer action hierarchy and contact treatment.

## Thoracic Aorta architecture
- Research landing now contains one foundational-research teaser instead of repeating the same Aorta research twice.
- Added `/research/thoracic-aorta/` as a lightweight Research Project Note rather than a fourth Selected Work case.
- Added a website-aligned workflow figure derived from the existing research visual, with oversized slide-title and duplicate metrics removed.
- Dedicated page covers Context, What I Worked On, Workflow, Results, and Why It Mattered.
- Brain Tumor remains the primary research narrative; Aorta remains explicitly foundational.

## Recruiter-scanning improvements
- Homepage PM project proof now includes 5 physicians in addition to speed and center scope.
- Homepage validation preview now includes client scope.
- About homepage pathway is now four parallel foundations with explanatory copy, not an arrow-only timeline.
- Aorta CTA in Experience now goes directly to the dedicated project note.

## Production
- Portfolio marker and cache-busting updated to 6.3.
- Added `v63-unified-editorial.css` as the final authoritative visual layer.
- Updated Hugo language config from deprecated `languageCode/languageName` to `locale/label`.
