# V5.5 — Stability & Richness Pass

## Release blockers fixed
1. **Tina Tai. home link** now uses Hugo's current-language home permalink instead of `/`.
2. **Image stability**: shortcode strips accidental leading slashes; missing Project 01/02 SVG assets are included.
3. **Work labels**: generic `CASE STUDY` replaced with `PRODUCT TRANSLATION`, `CLINICAL AI · ML`, and `ANALYTICS · OPERATIONS`.
4. **Research raw HTML**: Research is rendered entirely by `layouts/research/single.html`; Markdown contains front matter only.

## Richness without copying LinkedIn
- Homepage adds a curated Background & Education section.
- Experience page adds context, impact, skills, and related-project links.
- Work landing cards add category, one-line context, proof points, and tags.
- Full certificate/course inventories remain better suited to LinkedIn.

## Visual system
- Same Manrope + Inter + Noto Sans TC typography.
- Same black / warm white / blue palette.
- Section headings remain icon-free; small outline icons are reserved for metadata/credentials.
- Project diagrams are vector SVG so they remain crisp.
- Research photos keep natural portrait/landscape proportions.

## AITEWAN reference boundary
The product visual borrows the *presentation logic* of physician-led clinical integration and short metadata labels from AItewan's public website. It does **not** attribute current company regulatory clearances or post-tenure milestones to Tina.

## Deploy
Copy all files inside this V5.5 folder into the existing GitHub repository folder and replace same-name files. Keep `.git`. Commit and push.
