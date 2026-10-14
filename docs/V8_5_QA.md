# V8.5 QA checklist

## Verified offline
- Source assertions: URL assets, cross-page content, existing case proofs, personal credentials, image/privacy exclusions, head/base cache busts.
- Targeted bilingual responsive previews: About, Education and Research on Chromium at 1440, 768, 390, and 360px widths; no horizontal overflow or clipped key heading text detected.
- Original AMLDS and NYCU award images visually tested in recognition cards with identical 4:3 media geometry.
- Resume byte comparison against the user's Oct 13 PDF when the file is present.

## Still required in production
- `hugo build` success via `.github/workflows/hugo.yaml` (not run in this local environment).
- Browse the real GitHub Pages HTML (meta `portfolio-version=8.5`) and inspect About, Education and Research in EN/zh, 1440px/390px and Dark Mode.
- Verify external institutional/certificate links in the deployed environment.
- Audit accessibility with keyboard focus, alt text, responsive menu, and reduced-motion settings.

## Attribution
- Graduation ceremony: onstage representative of graduating Institute of Biophotonics students; no speaking or elected office implied.
- Future Tech Award: NYCU project/team award. Its excluded event photo is not in the public assets.
- The Student Ambassador role is a selection, not invented tenure accomplishments.
