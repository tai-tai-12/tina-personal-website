# V8.3 Release Notes — October 2026

## 1. Visual defects resolved

| Earlier issue | Actual implementation in V8.3 |
|---|---|
| Home case metrics wrapped 2+1 | Explicit `metrics-v83` three-column grid, numeric values separated from labels, three-column stability at 1440/768/390px. |
| Tiny years and metadata | Consistent ~14–16px metadata scale, stronger date weight, clearer publication and experience timelines. |
| Homepage Experience not chronological | Reordered NTUH Clinical Intern (2023–24) before NYCU testing (2021–23); dates themselves unchanged. |
| Repeated blue/dark concept images on Work | Clinical AI is now a real comparison using published thesis data; Structured Validation uses a neutral white-background SVG process flow; Product retains clinical workflow image. |
| Excessively narrow Education credentials sidebar | Credential panel moved after full-width academic timeline, with responsive 3/2/1-column group arrangement. |
| Research image/metadata imbalance | Smaller figures, consistent photo limits, constrained content width, readable publication year labels. |
| Homepage About felt incomplete | Added concise, functional Career Journey; retained four foundation skills and narrative. |
| CSS specificity conflict | Public file normalized to a common cascade, removes legacy priority flags, and consolidates V8.3 component rules within one CSS asset; historical selectors retained where needed for stability. |
| Aorta report figures too large and static | Controlled image sizing + keyboard-operable enlargement dialog, with Close/Escape behavior. |
| Need purposeful motion | Subtle link and image hover; existing reveal; reduced-motion support preserved. No carousel, parallax, or unrelated backgrounds. |

## 2. Evidence and professional positioning

- Retained exact research cohort: **264** independent retrospective MRI studies; **1,007 → 55** FP candidates (**94.54%** reduction). Sensitivity **84.96% → 80.97%** is explicitly stated in the evidence visual.
- 90.16% metric remains classified as five-class accuracy *on retained true-positive lesions*, not an all-lesion accuracy or sensitivity metric.
- Team recognition for DeepBT A+ / 2026 Future Tech Award is accurate. **No non-scanned award photograph was used.**
- No new unsupported claims, credentials, or source material introduced.
- Existing URL structure, Hugo front matter, EN/zh routes, official links, and resume preserved.

## 3. Technical changes

- `layouts/index.html`: performance metric grid, clinical evidence visual partial, validation SVG, Experience ordering, Career Journey.
- `layouts/work/list.html`: shared visual assets and metric styling.
- `layouts/research/single.html`: linked, accessible scientific image zoom, `<dialog>`.
- `layouts/partials/clinical-evidence-visual-v83.html`: bilingual source-oriented evidence visualization.
- `static/images/projects/validation-workflow-v83.svg`: purpose-made, fully editable vector schematic.
- `static/js/site.js`: lightbox event handling without dependencies; respects existing theme/menu/reveal.
- `static/css/portfolio-v83.css`: normalized cascade and responsive component rules.
- `layouts/partials/head.html`, `layouts/_default/baseof.html`: 8.3 metadata and asset cache tags.
- `.github/workflows/hugo.yaml`: V8.3 verification script.
- `scripts/verify_v83.py`: source integrity / asset / metrics / privacy checks.

## 4. Honest remaining limitations

Automated template-based Chromium previews are **not equivalent** to a Hugo build of all final pages. A real Hugo build plus published EN/zh desktop/mobile review remains necessary when the ZIP is deployed. Full historical selector removal, if desired, should be a separate, regression-tested code cleanup rather than a risky blind deletion.
