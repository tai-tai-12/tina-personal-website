# Tina Tai Personal Website — V8.13.3 IEEE Publication Update

This is a **full replacement** Hugo / GitHub Pages source package, based on the successfully deployed V8.13.2 release.

## Deployment
1. Back up the previous version. Preserve `.git/` if using local Git.
2. Replace the entire website source in the existing GitHub repository with the contents of this ZIP, including `.github/`.
3. Commit and push to `main`.
4. In GitHub Actions, confirm **build** and **deploy** succeeded.
5. Confirm the site source reports `<meta name="portfolio-version" content="8.13.3">`.
6. Check `/research/`, `/zh/research/` and the two clinical/product case studies. Test IEEE Xplore and PDF links.

## Publication verification
- AMLDS 2026 official proceedings: https://ieeexplore.ieee.org/xpl/conhome/11723344/proceeding
- This is a **conference proceedings URL**, **not** a verified article-specific DOI or document URL. An article-level link may replace it once verified.
- The previously published local AMLDS paper PDF remains available. MIDL references and distinct research cohorts are unchanged.

## Quality checks
Run `python3 scripts/verify_v8133.py` before building. Hugo build runs in the included GitHub Actions workflow.
