# V8.3 QA Report — Source, Responsive Layout, Privacy

## Automated checks performed in preparation environment

- **Source validation:** `python3 scripts/verify_v83.py` — **178/178 passed**.
- **JavaScript:** `node --check static/js/site.js` — passed.
- **CSS syntax:** parsed with `tinycss2` — passed.
- **SVG syntax:** validation workflow parsed as XML — passed.
- **Resume integrity:** SHA-256 comparison with uploaded October 13 general PM resume — exact match.
- **Assets:** local references within Hugo layouts, Markdown shortcodes, and new SVG verified by source checks.
- **Privacy:** raw transcripts, licenses, scores, testing data, and the non-scanned Future Tech photo were not copied into public assets.
- **Lightbox:** Chromium script click test confirmed a figure click opens the `<dialog>` and Close button closes it.
- **Languages:** preserved English and Traditional Chinese content tree, all major sections and project detail pages.

## Visual/layout testing actually performed

Source-template browser previews with actual V8.3 CSS and local referenced images were rendered using Chromium/Playwright. Screens were captured at:

- EN Home: **1440 / 768 / 390px**; EN Experience, Education, Research, About, Thoracic Aorta: **1440 / 390px**.
- 繁中 Home: **1440 / 768 / 390px**; 繁中 Experience, Education, Research, About, Thoracic Aorta: **1440 / 390px**.
- EN homepage and Education in **Dark Mode 1440px**.
- Home numeric evidence rows checked for fixed same-row placement; **no 2+1 wrap**.
- Document horizontal overflow tested on 26 source-template browser variants; **none detected**.
- Images intentionally lazy-loaded in actual website; preview script forces loading to include off-screen images in screenshots.

**Important:** These previews render actual layout source and real local assets, but substitute simple Hugo values to isolate CSS and HTML. They are not the exact output of Hugo and should not be treated as pixel-perfect production screenshots. Additional Work detail pages and final translated Markdown composition need Hugo output review.

## Outstanding deployment gates

1. GitHub Actions `Validate V8.3 design...` success.
2. Full Hugo build success. This environment could not install Hugo due unavailable DNS/network to Go proxy and release host.
3. Review all **EN and zh** routes at **1440, 768, 390, 360px** after live deployment, including Work and case details.
4. Confirm no overlapping headings, Date/Year cropping, or clipping on Chrome/Safari.
5. Check both theme modes, mobile navigation, anchors, Resume, official credentials, and original research figure enlargement.
6. Verify `<meta name="portfolio-version" content="8.3">` and `portfolio-v83.css?v=8.3.0` on live pages. Hard-refresh when validating to avoid older cached CSS.

## Core evidence disclaimer

The FP comparison uses the **same retrospective independent cohort** at two cascade stages. It is not a prospective clinical outcome, not a directly measured time saving, and not a claim that sensitivity improved. Structured Validation graphic is explicitly illustrative, not an original customer product screenshot.
