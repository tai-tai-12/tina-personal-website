# Tina Tai Personal Website — V8.13.1 FINAL

A **complete source replacement** for Hugo / GitHub Pages. The ZIP root is the GitHub repository root; there is no extra parent folder.

## Deployment

1. Back up the current V8.13 website repository. Keep `.git/` if using local Git.
2. Replace all previous website source files with **all** contents of this archive, including hidden `.github/`.
3. Commit and push to `main`.
4. In GitHub → Actions, confirm the **Build and deploy** workflow successfully completes both Build and Deploy.
5. Refresh the live website and confirm the page source contains `<meta name="portfolio-version" content="8.13.1">` and loads `portfolio-v8131.css`, `home-v8131.css`.
6. Visually inspect both Research cards in EN / 繁中 at desktop and mobile widths; confirm no metric text extends beyond a card.

## Quick check

```bash
python3 scripts/verify_v8131.py
```

The GitHub Actions workflow runs this check automatically **before** the official Hugo build.

## Scope

- Prevent overflow in the three Research metrics of each Research Area card. At desktop, metrics use equal columns with stacked value + label; on small phones, a readable vertical list.
- Translate remaining labels and conclusions in Traditional Chinese pages; localize selected accessibility labels.
- Keep **all** Work, Experience, Education, Research, About, three detailed cases, thoracic-aorta study, official sources, newest resume, and existing visual identity intact.
- Keep medical AI performance-cohort distinctions, lab accreditation boundaries, consortium client-contact attribution, and team award attribution unchanged.

## Validation scope

See `V8_13_1_FINAL_QA.md`. Source validation, HTML template previews, and browser containment checks have passed. The formal Hugo build and post-deployment interaction/visual checks remain the GitHub Actions and live-site gates; do not equate the local preview with production pixels.
