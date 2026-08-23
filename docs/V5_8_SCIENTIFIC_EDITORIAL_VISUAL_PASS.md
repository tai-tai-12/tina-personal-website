# V5.8 — Scientific Editorial Visual Pass

## Why this pass exists
The prior SVG illustrations were too abstract and looked assembled from generic geometric shapes. This pass moves the project visuals toward a more concrete scientific-editorial language: realistic imaging screens, recognizable workflow objects, and simplified BioRender-like clarity without turning the portfolio into a research poster.

## Major changes

### 1. Crop the visual to the actual workflow
The homepage no longer shows a full infographic with an internal title, summary panel, and repeated metrics. The project image is now only the workflow strip itself.

### 2. Use semantically real visuals for Product and Clinical AI
Project 01 now uses a cropped clinical product workflow with:
- PACS case list
- case search / AI status
- MRI viewer
- lesion overlay
- lesion analysis
- report summary
- physician review

Project 02 now uses a cropped lesion-wise AI cascade with:
- T1C / T2 MRI input
- 3D candidate generation
- candidate-centered patches
- false-positive filter
- retained-lesion tumor typing

The crop keeps the scientific illustration quality while removing the large internal title and bottom metric strip.

### 3. Rebuild Project 03 with real-world workflow objects
The Project 03 visual now uses recognizable testing / analysis / documentation / audit objects instead of abstract diamonds and generic blocks.

### 4. Reduce duplicated text in the image
The page copy remains the source of project narrative and proof points. The image only explains the workflow visually.

### 5. More horizontal figure treatment
Project images are now shallow editorial banners instead of large slide-like infographics. This reduces the amount of dead space and keeps Selected Work focused on the written case-study story.

## Files changed
- `layouts/index.html`
- `layouts/work/list.html`
- `content/en/work/*.md`
- `content/zh/work/*.md`
- `static/css/site.css`
- new / updated assets under `static/images/projects/`

## Design rule going forward
Use photographs for personal / research evidence, and use scientific-editorial illustrations for project mechanisms. Avoid generic SaaS-style geometric diagrams for medical / technical work.
