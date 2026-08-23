# Round 1 Visual Integration

This version integrates the first real visual layer into the live portfolio.

## Added assets

- `static/images/profile/tina-headshot.jpg` — Hero portrait
- `static/images/projects/medical-ai-product/clinical-product-workflow.webp` — Homepage Project 01 visual + case study
- `static/images/projects/medical-ai-product/three-stage-ai-cascade.webp` — Project 01 technical visual
- `static/images/research/midl-poster.webp` — Research / MIDL evidence
- `static/images/research/amlds-talk.webp` — Research / AMLDS evidence
- `static/images/about/thesis-presentation.webp` — About / Journey image

## Homepage placement

- Hero: professional headshot remains primary identity image.
- Project 01: clinical product workflow replaces the generic abstract graphic.
- Research: MIDL and AMLDS photos replace template-like illustration tiles.
- About: thesis presentation image adds a human / academic bridge above the career journey.
- Hero contact links: LinkedIn and Email now use a consistent outline icon language.

## Project 01 detail page

The case study now contains:

1. Clinical product workflow visual.
2. Three-stage lesion-wise cascade visual.
3. Four published research metrics.
4. MIDL evidence photo.
5. Product / clinical workflow narrative.

## Updating later

To replace an image without changing code, keep the same filename and replace the file in `static/images/...`.

Examples:

- New headshot → replace `static/images/profile/tina-headshot.jpg`
- Better MIDL photo → replace `static/images/research/midl-poster.webp`

Commit and push; GitHub Actions will redeploy automatically.
