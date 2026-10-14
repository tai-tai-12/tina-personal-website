# Tina Tai — Personal Portfolio V8.8

**Full replacement source package** for the existing bilingual Hugo website at `tai-tai-12.github.io/tina-personal-website/`. This archive is **not** a patch and is meant to replace the old repository content, without accumulating old versioned CSS files or scripts.

## Deploy as a clean replacement

1. Extract `Tina_Tai_Personal_Website_V8_8_Full_Replacement.zip`.
2. The ZIP already contains the **repository-root files directly** (`hugo.toml`, `layouts/`, `content/`, `static/`, `.github/`, etc.). Extract these files and folders directly into the repository root; do **not** create an extra `tina-personal-website-v8-8/` layer.
3. Replace the old repository files with these files, **including the hidden `.github/` folder**. Do not delete the `.git/` directory if you use Git locally (it contains your repo history and remote configuration).
4. Verify the root contains `hugo.toml`, `layouts/`, `content/`, `static/`, `themes/`, `scripts/` and `.github/workflows/hugo.yaml`. There must be **no extra enclosing website folder** in the repo root.
5. Commit and push to `main`. GitHub Actions will run `python3 scripts/verify_v88.py`, build with Hugo, then deploy to GitHub Pages.
6. In page source, check `<meta name="portfolio-version" content="8.8">` and that the stylesheets are `portfolio-v88.css?v=8.8.0` and `home-v88.css?v=8.8.0` (home only).
7. Check the built site at Home, Work, Experience, Research, Education, About and the case/research detail pages in English and Traditional Chinese, on both desktop and mobile.

If replacing files using a terminal, an example from the unpacked folder is:

```bash
# Run from outside your local repository; replace placeholders with real paths.
rsync -av --delete --exclude='.git/' /path/to/unpacked-v8.8/ /path/to/your/local/tina-personal-website/
cd /path/to/your/local/tina-personal-website
python3 scripts/verify_v88.py
git add -A
git commit -m "Deploy V8.8 cross-page UX polish"
git push origin main
```

**Note:** Only use `rsync --delete` if you intend to fully replace the repo's working tree and have backed up any independent changes. The `.git/` directory is excluded from deletion, including if it's hidden.

## Local validation

```bash
python3 scripts/verify_v88.py
hugo build --gc --minify
hugo server
```

Local source checks do not replace a successful Hugo build or production browser verification. The GitHub Actions workflow runs both the source check and the actual Hugo build.

See `V8_8_RELEASE_NOTES.md` and `V8_8_QA.md`.
