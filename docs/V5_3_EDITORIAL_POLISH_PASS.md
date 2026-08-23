# V5.3 — Editorial Polish Pass

## Why this pass
V5.2 established the right content architecture and visual system, but the homepage still carried too much supporting detail and Research images were being forced into matching tall containers. V5.3 is a reduction-and-rhythm pass rather than a redesign.

## Homepage changes
- Project 01 now shows two proof points only: **2 medical centers** and **TFDA submission**.
- Project 01 visual is a four-step teaser: Clinical data → AI analysis → Lesion review → Physician decision.
- Project 02 homepage visual keeps the 3-stage cascade and only the two key cohort scopes: **12.1K development MRI exams** and **264 independent test exams**. Detailed performance remains on the case-study page.
- Project 03 visual removes the extra proof-label footer.
- All Selected Work visuals use a consistent 16:10 desktop rhythm.
- Research is now a compact editorial strip rather than two oversized portrait cards.
- The homepage Research heading now explains the value of research directly instead of telling the reader how to interpret it.
- About imagery is slightly smaller so Selected Work remains the dominant visual section.

## Research page changes
- MIDL retains a portrait-led layout.
- AMLDS presentation keeps its native landscape character.
- AMLDS award uses the landscape award photo rather than a certificate-only image.
- Full publication titles stay in the typography-first publication list; featured cards use shorter descriptive titles.
- Research themes are condensed into one Focus line.

## Data-scope wording
- Development cohort: **12,125 MRI examinations / 23,341 annotated lesions**.
- Independent clinical test cohort: **264 MRI examinations / 226 annotated lesions**.
- Homepage wording avoids presenting the development-cohort size as an independent validation size.

## Image quality
The latest user-provided source files were re-encoded at high WebP quality while preserving source resolution:
- `midl-poster.webp` — 1152 × 2048
- `amlds-talk.webp` — 2048 × 1365
- `amlds-award.webp` — 2048 × 1152

## Deployment
Replace the contents of the existing local `tina-personal-website` repository with this package (do not delete `.git`), commit, push, and wait for the existing GitHub Pages Action to complete.
