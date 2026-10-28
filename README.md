# Tina Tai Personal Website — V8.13.4 Publication Link Refinement

This ZIP is a **full replacement** of the V8.13.3 Hugo / GitHub Pages source. All files are at the ZIP root (not nested inside an extra folder).

## What changed
- Research: MIDL `Paper` links directly to [OpenReview](https://openreview.net/forum?id=OIjw0dFD3r); its real poster is linked as `Poster`.
- Research: AMLDS `Paper` links to [the individual IEEE Xplore article](https://ieeexplore.ieee.org/document/11723832), not the proceedings index.
- No extra `Official Program` / `Proceedings` link: these duplicate the core publication navigation for a recruiting portfolio. Add them later only to substantiate something unique, such as a presentation schedule or an award notice.
- Clinical AI / Medical AI supporting research links now reference the individual paper pages, in both languages.
- Original PDFs, poster, photos and research metrics remain unchanged. No case-study design, resume, or imagery changes.

## Full replacement deployment
1. Back up V8.13.3. Preserve `.git/` if replacing files in a locally cloned repository.
2. Extract this ZIP and copy **all** contents to the repository root, including hidden `.github/`; remove old website source/CSS/scripts so versions do not overlap.
3. `python3 scripts/verify_v8134.py` — must pass.
4. Commit and push to `main`.
5. Confirm GitHub Actions `build` **and** `deploy` succeeded.
6. Verify `<meta name="portfolio-version" content="8.13.4">` and check `/research/` and `/zh/research/` and the links in both case studies.

## Publication sources
- MIDL 2026 article: https://openreview.net/forum?id=OIjw0dFD3r
- AMLDS 2026 article: https://ieeexplore.ieee.org/document/11723832
- Direct links are provided by the user; an AMLDS DOI was **not** asserted or guessed.

## Verification scope
The source verifier runs before Hugo in GitHub Actions. Final Hugo rendering and GitHub Pages delivery must be confirmed by the Actions run and production URL after deployment.
