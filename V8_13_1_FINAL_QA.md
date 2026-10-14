# V8.13.1 Final QA

## Sources and content

- `python3 scripts/verify_v8131.py`: version, bilingual content, all case/evaluation numbers, lab-consortium attribution, public image references, official links, resume hash and excluded sensitive materials.
- CSS parsed with `tinycss2`, JS syntax validated separately.
- No older stylesheet/verifier in the replacement source.

## Browser visual verification (local template preview, not official Hugo output)

- English/Traditional-Chinese Home, Work and Research: desktop/tablet/mobile width sweep at **1440, 768, 390, 360px** = 24 checks.
- Research-card **containment**: English/Traditional-Chinese × 10 viewport widths (320, 360, 390, 560, 768, 1024, 1200, 1440, 1784, 1920px) × Light/Dark modes = **40 checks**. Specifically tested each metric's bounding box and internal scroll-width against its **parent card**, not merely the page's horizontal scroll width. All passed.
- Additional case-page browser previews using source-rendered templates are run to verify no major regression; they do not substitute for the official Hugo output.

## Required production acceptance

1. GitHub Actions V8.13.1 source validation success.
2. GitHub Actions Hugo build and GitHub Pages deploy success.
3. On the real website: confirm version marker, research cards at 1784px and 390px, English / Chinese page-switching and navigation, card click-throughs, resume PDF, dark theme, and figure zoom interactions.
4. Verify external official institution/certificate links manually or in a supported link checker.

There was **no live-site pixel-perfect QA** in this execution environment. Do not characterize local Chromium reconstruction as live production proof.
