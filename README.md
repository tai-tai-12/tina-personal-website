# Tina Tai Personal Website — V8.13 Bilingual Localization & Visual QA

**Full-replacement Hugo source for the existing GitHub Pages site**, not an incremental overlay.

## Replace the repository safely

1. Back up the current repository or create a Git tag for V8.12.
2. If editing a local Git checkout, **keep `.git/`**; remove only the tracked site sources/assets from the working tree.
3. Unzip V8.13. The archive opens directly into the website root (no extra parent directory).
4. Copy everything from that root into the repository, including the hidden `.github/` directory.
5. Confirm these top-level items exist: `hugo.toml`, `.github/`, `content/`, `layouts/`, `static/`, `themes/`, `scripts/`.
6. Commit and push to `main`. GitHub Actions checks the source and then builds/deploys with Hugo.
7. Inspect View Page Source for `<meta name="portfolio-version" content="8.13">`. Stylesheets should be `portfolio-v813.css` and `home-v813.css`.
8. Review both English and 繁體中文 Home, Work, Experience, Research, Education and About on desktop and phone. Open each case study, verify Resume/credential links and theme switching.

## V8.13 scope

- Localizes Taiwanese universities, departments, degrees, coursework and awards in Chinese-facing templates while preserving the official English labels on the English site.
- Corrects **Honor Student Award → 書卷獎** with reference to the original NYCU award certificate; corrects the NTUH recognition to **放射腫瘤科實習表現優異獎**, reflecting the originating department.
- Localizes homepage education, experience, conference recognition, selected certification descriptions, supporting metadata, footer and a selection of case-study explanatory labels.
- Aligns the homepage About paragraph to the heading top on desktop; retains stacked flow on mobile.
- Preserves research/technical paper titles in their original English where they are official publication names, plus product/institution acronyms useful for verification.
- Does **not** alter clinical metrics, ownership attribution, original publications, private documentation boundaries or the existing resume file.

## Source checks

```bash
python3 scripts/verify_v813.py
hugo build --gc --minify
```

The first command runs local preflight checks. Hugo is not available in the authoring environment, so the formal Hugo build must be verified by the GitHub Actions workflow and followed by live-site visual checks.

## Key factual boundaries

- Future Tech Award is an NYCU-led team/project recognition, not a personal individual award. The excluded event photograph is not shipped.
- 8 devices, 5 client organizations and 10+ reports describe one ionizing-radiation consortium testing assignment; companies were introduced by the professor, and the user's responsibility was follow-up, membership/agreement coordination, hands-on testing and report delivery.
- The MATLAB small-animal CT work is separate; TAF accreditation applies to the laboratory's defined scopes, not the individual.
- The 94.54% false-positive reduction is retrospective and carries a decrease in sensitivity; do not interpret research metrics as prospective clinical efficacy.
- No raw personal academic records, medical-license scans or clinical identifiers are included.
