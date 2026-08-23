# V5.9 — Information Architecture + Visual Readability Pass

## Why this pass
V5.8 moved the portfolio visuals toward a more scientific / real-world look, but the homepage project images still contained too much small text. Education was also overloaded on the homepage instead of having a proper destination page.

## Main changes

### 1. Project visuals are now image-first and readable
Homepage and `/work/` use dedicated cropped/montage assets:
- `clinical-product-home.webp`
- `clinical-ai-home.webp`
- `structured-validation-home.webp`

The goal is to show recognizable MRI, AI, quantitative-analysis, and review artifacts without asking the user to read a mini research poster inside a card.

### 2. Project 03 is more concrete
Renamed to:
**Building Repeatable Validation & Analytics Workflows**

Its homepage visual now uses a representative quantitative CT / MATLAB analysis workflow rather than a generic diagram. The full case study explicitly explains that this is a representative analytics tool within a broader testing / certification / audit role.

### 3. Added a real Education page
New route:
`/education/`

Navigation now includes **Education**.

The new page includes:
- Carnegie Mellon University — M.S. Business Analytics
- NYCU — M.S. Biophotonics + Outstanding Thesis Award
- NYCU — B.S. Biomedical Imaging & Radiological Sciences + Biomedical Engineering minor
- Licensed Medical Radiation Technologist credential
- Cross-links to Research and related case studies

### 4. Homepage education is now a concise teaser
The previous four-card Background & Education block was removed.
The homepage only shows the two highest-signal degrees plus a link to the dedicated page.

### 5. Case study pages are wider and more editorial
New `layouts/work/single.html` gives case studies:
- a custom category / summary hero
- wider figures for real-world diagrams
- a narrower readable body measure for text
- clearer proof / skill metadata

### 6. Research page rendering is made more robust
Research is converted to a true Hugo section (`_index.md`) and rendered through `layouts/research/list.html` to avoid raw-HTML leakage / incorrect fallback rendering.

### 7. Navigation / page context updated
Education is included in the main navigation and uses its own page-context icon / label.

## Recommended deployment
Replace the contents of the existing GitHub repository with the contents of this package (keep the existing hidden `.git` folder), commit, and push.

Suggested commit message:
`Apply V5.9 architecture and visual readability pass`
