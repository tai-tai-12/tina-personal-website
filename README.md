# Tina Tai Personal Website · V8.5

Full Hugo source project for the bilingual existing GitHub Pages portfolio, based on V8.4. This is **not** a partial patch.

## What's updated

- About: complete editorial reorganization around actual personal story, connected experiences, featured student leadership, community work and interests. Home About is reduced to a short preview.
- Education: adds the NYCU graduation-ceremony onstage representative (not a speaker) and Department Student Association President, without recreating the full About list.
- Research: equally proportioned award photos and compact Recognition cards.
- Existing Work cases, evidence visuals, Resume, public research artifacts, certifications, dark mode and language routes are preserved.

## Deployment

1. Unzip this archive and open `tina-personal-website-v8-5/`.
2. Copy all the **contents** of that directory into the root of the GitHub repository `tai-tai-12/tina-personal-website`, including the hidden `.github` directory. Remove repository files that are absent from this clean package, especially `static/css/portfolio-v84.css`.
3. Push to `main`. GitHub Actions first runs `python3 scripts/verify_v85.py`, then builds the Hugo site and deploys it to GitHub Pages.
4. Inspect HTML View Source for `portfolio-version` = `8.5` and `portfolio-v85.css?v=8.5.0`.

For local verification with Python 3:

```bash
python3 scripts/verify_v85.py
```

For a local Hugo production-like build (Hugo 0.164.0 recommended):

```bash
hugo build --gc --minify
hugo server -D
```

The automated source verifier and local Chromium **template** screenshots are distinct from a full Hugo build. The latter must pass through GitHub Actions during deployment. See `docs/V8_5_RELEASE_NOTES.md` and `docs/V8_5_QA.md`.
