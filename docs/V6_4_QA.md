# V6.4 QA

- 22 Markdown content files parsed with 0 front-matter errors.
- 47 local image references checked with 0 missing assets.
- All CSS files have balanced braces.
- All Hugo layout files have balanced template delimiters.
- Portfolio version marker and cache-busting version updated to 6.4.
- V6.4 stylesheet loads after V6.3, making it the final visual authority.
- Homepage Selected Work uses one proof-row component and no dot separators between pill items.
- Research landing contains two parallel Research cards, each with the same image/meta/title/description/proof/CTA structure.
- Brain Tumor and Thoracic Aorta preview assets are both 1200 × 750 (16:10).
- Thoracic Aorta landing preview, detail hero, and technical workflow use different assets and visual roles.
- No missing image references after the image-system changes.

Hugo is not installed in this execution environment, so the package was validated structurally rather than through a local `hugo build`. The GitHub Actions workflow remains included for the deployment build.
