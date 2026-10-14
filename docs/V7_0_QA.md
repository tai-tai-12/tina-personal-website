# V7.0 QA

Automated package checks completed before ZIP creation:

- `hugo.toml`: TOML parse passed.
- Markdown files: 22 checked; YAML front matter passed.
- Local static references: 51 checked; 0 missing.
- Work case navigation: EN + ZH case pages keep matching `navItems` and H2 counts.
- CSS: brace counts passed for all stylesheets.
- Hugo templates: basic `{{` / `}}` delimiter counts passed.
- V7 version marker present in `head.html`.
- V7 stylesheet loaded last with `?v=7.0.0` cache busting.
- Brain Tumor research preview: 1200×750.
- Thoracic Aorta research preview: 1200×750.
- Latest resume file matches `Shih-Ting_Tai_Resume_pm.pdf` supplied for the V6/V7 content pass.

Environment note: Hugo is not installed in the execution environment, so a native `hugo build` could not be run locally. The existing GitHub Actions deployment workflow and Hugo project structure are preserved.
