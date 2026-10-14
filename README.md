# Tina Tai Personal Website — V8.12 Final Release

Full replacement Hugo source package for GitHub Pages. **Not an incremental patch.**

## Replace your existing repository

1. Back up the previous GitHub repository content. If using a local Git checkout, do not delete `.git/`.
2. Remove previous website source files from the repository (except `.git/` when applicable).
3. Copy **all extracted files and directories from the ZIP root** into the repository root, including hidden `.github/`.
4. Confirm the root contains `hugo.toml`, `layouts/`, `content/`, `static/`, `scripts/`, `themes/`, and `.github/`.
5. Commit and push to `main`; GitHub Actions runs a V8.12 source check and Hugo build before deployment.
6. In View Page Source, confirm `<meta name="portfolio-version" content="8.12">` and that CSS loads `portfolio-v812.css` / `home-v812.css`.
7. Open EN and 繁體中文 Home, Work, Experience, Research, Education, About, and case studies at desktop and mobile sizes. Verify Resume and links.

## Release approach

This is a final stabilization release, not a content expansion. The Product Manager-first positioning, selected cases, publication evidence, and case metrics are unchanged. Read `V8_12_RELEASE_NOTES.md` and `V8_12_QA.md` for scope and test limitations.

## Build locally (optional)

```bash
python3 scripts/verify_v812.py
hugo build --gc --minify
```

Requires Hugo (version pinned in `.github/workflows/hugo.yaml`).

## Content guardrails

- The Future Tech Award is **NYCU team/project recognition**, not an individual award; the excluded non-scanned photo is not shipped.
- Consortium-linked third-party testing (8 devices, 5 client organizations, 10+ reports) remains one scope of work. Professor introductions led to client follow-up, not independent prospecting or closing deals.
- The small-animal CT MATLAB work is separate. TAF accreditation refers to a laboratory and defined test items, not the individual.
- Clinical AI performance refers to retrospective research data. False-positive reduction must be accompanied by the lesion-wise sensitivity trade-off.
- Original academic transcripts, individual medical license scan, internal FHIR/patient records, and private Material ZIP are not distributed.
