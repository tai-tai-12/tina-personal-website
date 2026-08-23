# Tina Tai — Personal Website V5.1 — Round 1 Visuals (GitHub Pages path fix)

Recruiter-first Hugo portfolio built on the CareerCanvas/Hugo foundation and refined around a quieter, more personal visual system.

## V4 direction

**Beautiful, professional, and recognizably personal — without looking like a template.**

- Product & Analytics | AI × Healthcare
- English primary + Traditional Chinese
- Light default + dark mode
- **Manrope for display + Inter for body/UI + Noto Sans TC**
- **Single chromatic brand color: deep/electric blue**
- Warm ivory used only as a neutral atmosphere, not a second accent color
- Tina Tai. reduced from heavy display weight to Manrope Medium
- Product & Analytics carries stronger professional hierarchy
- Medium professional portrait
- Mixed credibility strip
- Three asymmetric featured case studies
- Experience, Research & Recognition, About
- Writing architecture retained but not surfaced in the main navigation

## Preview

Open:

`preview/index.html`

## Deploy over the existing GitHub Pages site

Read:

`docs/V4_UPDATE.md`

The repository is already configured for GitHub Pages. Replace the site files with this V4 package, commit, and push. GitHub Actions will redeploy automatically.

## Future image replacement

The V3 image replacement plan still applies:

`docs/V3_ASSET_REPLACEMENT_LIST.md`


## GitHub Pages image-path fix

V5.1 removes leading slashes from Hugo asset URLs and uses a `site-img` shortcode in Markdown content so images resolve correctly under the project-site base path `/tina-personal-website/`.
