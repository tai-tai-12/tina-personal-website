# V6.5 QA

## Source/package checks
- Markdown content files parsed: 22
- YAML front-matter errors: 0
- Hugo layout files checked for balanced template delimiters: 17 / 17 passed
- CSS files checked for balanced braces: 6 / 6 passed
- Local `images/...` references checked: 36 / 36 resolved
- Static paths referenced through `relURL` / `absURL`: 0 missing
- Portfolio version marker: 6.5
- CSS / JS cache-bust version: 6.5.0

## V6.5 visual-system checks
- Work / Experience / Education / Research / About share the same top-level page-header grammar.
- Research now receives the same divider treatment as the other top-level pages.
- Research page eyebrow changed to `RESEARCH PROFILE` / `研究概覽`.
- Research section headings are visually subordinate to the page title.
- Evidence UI no longer uses pill-like button styling on landing cards; Work, Research, and the featured AITEWAN role use the same evidence-rail grammar.
- LinkedIn and Resume use equal footer action styling.
- Email remains visible text, clickable through `mailto:`, with regular weight.
- Education hero-to-content spacing is tighter.

## Research image checks
- Brain tumor preview: 1200 × 750
- Thoracic aorta V6.5 preview: 1200 × 750
- Both Research preview cards therefore use an identical 16:10 image system.
- Aorta preview uses one dominant 3D reconstruction plus supporting CT views instead of the V6.4 three-panel infographic-like composition.
- Aorta landing copy states ownership, NSTC context, workflow breadth, and cohort size without requiring a click.

## Known build limitation
The current execution environment does not contain the Hugo binary, so a native `hugo build` could not be run locally. GitHub Actions configuration remains included for the production build. Source-level template, front-matter, CSS, and static-reference checks all passed.
