# V5.12 — Navigation & Interface Polish

This release focuses on interface hierarchy rather than another visual redesign.

## Navigation
- Separates primary navigation (`Work`, `Experience`, `Education`, `Research`, `About`) from utility controls.
- Turns `Resume` into a compact outlined utility button.
- Replaces the standalone language text link with a segmented `EN / 中文` pill control.
- Aligns dark-mode control with the Resume and language controls.
- Uses a structured mobile menu with a separate utility row.

## Homepage hierarchy
- Shortens the three Selected Work summaries so the visuals and proof points carry more of the page.
- Keeps the Education section as a compact two-row teaser because a dedicated Education page now exists.
- Reduces the visual weight of Experience skill tags.
- Refines section-number markers so they read as editorial navigation cues rather than presentation labels.
- Tightens Hero CTA and utility-link spacing.

## Interface principles
- Content navigation and interface controls should not compete visually.
- Primary actions are stronger; metadata and utility actions are quieter.
- The language selector remains one-click and preserves the equivalent translated page.
- Mobile navigation keeps Resume, language, and theme controls grouped together.

## Files changed
- `layouts/partials/header.html`
- `layouts/index.html`
- `static/css/site.css`
