# V5.30 — Portrait Refresh & Final Visual QA

## Why this release

V5.29 remains the production architecture baseline. V5.30 is a restrained follow-up prompted by the new homepage portrait and a final strict visual QA of the live site. It does not introduce new pages, animations, or visual systems.

## Homepage portrait

- Replaces the previous white-background headshot with Tina's newly supplied professional portrait.
- The file is cropped/resized only; facial features, clothing, background, and identity are not generatively altered.
- Uses a 4:5 editorial crop that keeps face, shoulders, crossed arms, and upper torso.
- Removes the decorative dot grid, nodes, lines, and vertical `PRODUCT · ANALYTICS · AI` caption because the new photograph already has sufficient visual depth.
- Retains only a very subtle offset blue plane and restrained shadow.
- Slightly rebalances the desktop hero grid to give the new portrait sufficient presence without overpowering the copy.
- No global palette change: the portrait's navy, cool aqua, and warm neutral background already harmonize with the site's off-white / cobalt system.
- Updates the Open Graph image to the new portrait.

## Work detail QA

- Medical AI Product: consolidates four small responsibility modules into two editorial responsibility domains: `Product & Clinical` and `Validation & Regulatory`.
- Clinical AI: removes repeated `264` from At a Glance / Study Scope where the hero already establishes it; the scope block now emphasizes the 132/132 class balance.
- Clinical AI result metrics receive real text separation between values and labels for copy/paste and accessibility fallbacks.
- Third-Party Testing: removes the repeated 8 / 10+ / 5 / 2 metric grid from the validation section because those metrics already appear in the hero.

## Research QA

- Research Engineering tags use sentence case and explicit separators: `DICOM / NIfTI · Standardization`, `ANTs · Registration`, etc.
- Foundational Research metrics receive explicit separators instead of running together in text extraction.

## Education QA

- Selected Coursework is now a semantic list rather than a series of visual-only spans.
- Desktop uses a restrained two-column list; mobile collapses to one column.

## Footer QA

- Location/opportunity status and email are presented on separate lines for cleaner scanning and robust text extraction.
- Footer remains compact and does not add phone or street address.

## Production markers

- `portfolio-version` updated to `5.30`.
- CSS/JS cache-busting updated to `5.30.0`.
- OG image points to the refreshed portrait.
