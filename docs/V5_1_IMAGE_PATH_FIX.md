# V5.1 image path fix

## What was wrong
The site is deployed as a GitHub Pages **project site**:

`https://tai-tai-12.github.io/tina-personal-website/`

Several V5 image references began with `/images/...`. In Hugo, a leading slash makes the URL host-root relative, so the browser requested:

`https://tai-tai-12.github.io/images/...`

instead of:

`https://tai-tai-12.github.io/tina-personal-website/images/...`

## What changed
- Removed the leading slash from template image paths before `relURL` / `absURL`.
- Changed `profile_image` in `hugo.toml` to a path without a leading slash.
- Added `layouts/shortcodes/site-img.html` for images embedded in Markdown pages.
- Replaced raw `/images/...` references in English and Chinese content with the shortcode.

## Deploy
Copy the contents of this package over the existing local repository, commit, and push.

Suggested commit message:

`Fix image paths for GitHub Pages project site`
