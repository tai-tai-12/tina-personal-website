# V8.7 — Homepage Editorial Refinement

This deployable Hugo / GitHub Pages site updates **only the homepage** from V8.6. It uses `home-v87.css` exclusively on home pages; all interior pages, credentials, research content, and source assets remain unchanged. See `V8_7_RELEASE_NOTES.md` and `V8_7_QA.md`.

Before pushing: `python3 scripts/verify_v87.py`. On GitHub Pages, Actions runs the V8.7 verification and formal Hugo build.

# Tina Tai Personal Website · V8.6

Complete bilingual Hugo source project for the existing GitHub Pages portfolio. **This is a full deployment archive, not a patch.** It builds on V8.5 and focuses on Education and Experience.

## V8.6 updates

- **Education:** All three degrees use the same sequence: Degree → Focus → Selected Coursework → Campus Highlights. Current CMU coursework is identified as in progress. Campus highlights distinguish student involvement, ceremonial representation, and student leadership without suggesting those roles were equivalent.
- **Experience:** Four professional roles now use a shared visual hierarchy: Organization / Date → Role / Scope → Primary Outcome → Selected Contributions → Optional Recognition → Relevant Links. Product, research, clinical training, and testing operations preserve their different substance and evidence.
- **Recognition:** A shared component presents DeepBT A+ Future Tech Award as a **team/project award** and NTUH Certificate of Excellence as **individual internship recognition**.
- **Preserved:** Home, Work, Research, About, all certificates/verification links, original research and award photographs, bilingual routes, latest Oct 13 Resume, privacy exclusions, dark mode, and GitHub Pages settings.

See `docs/V8_6_RELEASE_NOTES.md` for detailed content and UX decisions, and `docs/V8_6_QA.md` for QA scope and limitations.

## Deployment to GitHub Pages

1. Unzip `Tina_Tai_Personal_Website_V8_6_Deployment.zip` and open `tina-personal-website-v8-6/`.
2. Replace the **repository root contents** of `tai-tai-12/tina-personal-website` with the contents of that folder, **including `.github/`**. Remove obsolete tracked files that are absent from the package, notably `static/css/portfolio-v85.css`.
3. Push to `main`. GitHub Actions runs `python3 scripts/verify_v86.py`, then Hugo build and GitHub Pages deployment.
4. View source on the published site to confirm `<meta name="portfolio-version" content="8.6">`, and the stylesheet `portfolio-v86.css?v=8.6.0`.

## Validation

```bash
python3 scripts/verify_v86.py
hugo build --gc --minify
hugo server -D
```

Hugo 0.164.0 is specified in `.github/workflows/hugo.yaml`. The offline validator and Chromium **template-based** screenshots do not replace the actual Hugo build or deployment-level browser regression. Verify the official build and both languages after deployment.
