# V8.13.2 — Fixed GitHub Pages Build

- Restored from V8.13 known-good complete source.
- Added only intended V8.13.1 improvements (Research KPI card containment, Chinese copy, accessibility labels) with the template-scope bug corrected.
- Corrected `{{ if eq .Lang "zh" }}` inside `{{ with .Params.snapshot }}` to `{{ if eq $.Lang "zh" }}`. This is an **identified likely cause**, not a quoted GitHub Actions error: the screenshot only contained exit code 1 and job summary.
- Added a regression check to the deployment validator and versioned cache busting.
- V8.13.2 is a full replacement. It intentionally excludes prior version CSS and old scripts.
