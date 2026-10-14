# Tina Tai Personal Website — V8.13.2 (Build-Fixed Final)

**Complete replacement** of the Hugo source tree for GitHub Pages. Base: the previously deployed V8.13. This is not an overlay over the failed V8.13.1.

## What was fixed
1. Resolved a **Hugo Go-template rendering scope error** in `layouts/work/single.html`. Inside `with .Params.snapshot`, the language check must use `$.Lang`, not `.Lang`. The failed package introduced this difference.
2. Preserved Research area card metric containment (fixed three-column grid, responsive single-column metrics on small screens).
3. Preserved final Traditional Chinese localization corrections for Research, Case Study takeaway headings, and accessible labels.
4. Kept all original publication, resume, award, testing attribution, multilingual routes and existing project assets.

## Safely replacing the repository
1. Back up your current website. If working locally with Git, **do not delete `.git/`**.
2. Remove existing tracked site files and copy all files from this ZIP directly to the repository root, including hidden `.github/`.
3. Check the repository root has `hugo.toml`, `content/`, `layouts/`, `static/`, `themes/`, `scripts/`, `.github/`.
4. Push to `main` and wait for `hugo.yaml` build and deploy jobs to both succeed.
5. Verify page source contains `<meta name="portfolio-version" content="8.13.2">`; verify `portfolio-v8132.css` and `home-v8132.css` load.
6. Verify `/research/` in EN and `/zh/research/` in Traditional Chinese, plus at least one case-study page.

## Local/source checks

```bash
python3 scripts/verify_v8132.py
hugo build --gc --minify
```

The source validator and stylesheet checks pass locally. **A real Hugo build is required on GitHub Actions:** the authoring container does not have Hugo, so the deploy job's success has to be checked after upload.
