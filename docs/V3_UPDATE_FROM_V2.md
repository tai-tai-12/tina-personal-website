# Update the live site from V2 to V3

Your GitHub Pages deployment is already working, so V3 does **not** need a new repository or a new Pages setup.

## Recommended update path

1. Download and unzip the V3 deployment package.
2. Open your existing local repository for `tina-personal-website-v2` (or clone it from GitHub if needed).
3. Back up the current repository folder once.
4. Copy the V3 files into the repository and replace files with the same names.
5. Keep your existing `.git` folder. Do **not** delete or replace it.
6. Review the changed files in GitHub Desktop.
7. Commit with a message such as `Upgrade homepage to V3`.
8. Push to `main`.
9. GitHub Actions will automatically rebuild and redeploy the site.
10. Open the Actions tab and confirm `Build and deploy` is green.

## Files that matter most for the V3 refinement

- `layouts/index.html` — redesigned homepage structure
- `static/css/site.css` — V3 visual system and responsive layout
- `preview/index.html` — browser-openable local preview
- `docs/V3_ASSET_REPLACEMENT_LIST.md` — future real-image replacement plan

All existing case-study pages, bilingual content, resume, header/footer, theme toggle, and GitHub Pages workflow are preserved from V2.
