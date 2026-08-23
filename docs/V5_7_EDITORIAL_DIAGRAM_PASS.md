# V5.7 — Editorial Diagram Pass

This pass updates the portfolio visuals to address the feedback that the previous icon-based diagrams felt too generic and "AI-template-like."

## What changed

### 1) Rebuilt the three flagship project visuals
The homepage and `/work/` page now use new editorial SVG diagrams with:
- clearer step-by-step structure
- better visual hierarchy
- larger typography
- fewer words on the image itself
- more refined panel composition inspired by scientific workflow posters, but simplified for portfolio use

Updated visuals:
- `static/images/projects/medical-ai-product/clinical-product-workflow.svg`
- `static/images/projects/medical-ai-product/three-stage-ai-cascade.svg`
- `static/images/projects/structured-validation-workflow.svg`

### 2) Replaced inline SVG blocks with image-based editorial diagrams
This improves consistency across:
- homepage selected work section
- `/work/` landing page cards
- case-study pages that already reference the product / clinical AI diagrams

Files updated:
- `layouts/index.html`
- `layouts/work/list.html`

### 3) Improved diagram presentation styling
- project figure cards now display diagram images directly
- corner labels have subtle badge styling
- work-card visuals use proper cover behavior
- image framing is more stable and visually cleaner

File updated:
- `static/css/site.css`

## Design intent
The new diagrams aim to sit between:
- overly abstract startup-style icons
- overly dense academic figures

They should feel:
- professional
- structured
- portfolio-appropriate
- easier to skim
- more visually credible in a healthcare / analytics context

## Notes
- The clinical AI diagram explicitly distinguishes **development scale** from **independent evaluation** to avoid overstating the testing cohort.
- Existing photos, content structure, and navigation were preserved.
