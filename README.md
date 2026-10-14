# Tina Tai — Personal Portfolio V8.9 (Full Replacement)

This ZIP is the **entire bilingual Hugo project**, not a patch. The ZIP root contains `hugo.toml`, `.github/`, `content/`, `layouts/`, `static/`, `scripts/`, and `themes/`. It is safe to replace the website source tree while **keeping your local `.git/` repository metadata**.

## Full replacement deployment

1. Back up your existing website folder. Extract the ZIP to a new folder.
2. Copy **all files including `.github/`** into the repository root; replace prior website source files (not `.git/`).
3. Ensure no older `portfolio-v88.css` or `home-v88.css` persists after the replacement.
4. `python3 scripts/verify_v89.py` (source/data/security checks).
5. Commit and push to `main`; the included `.github/workflows/hugo.yaml` validates sources, builds Hugo, and deploys GitHub Pages.
6. Verify the published HTML contains `<meta name="portfolio-version" content="8.9">` and the current `portfolio-v89.css?v=8.9.0` plus `home-v89.css?v=8.9.0`.
7. Check Work → Running Client-Facing Validation Operations, Home, Experience, and English / Traditional Chinese views on desktop and mobile. Confirm the original X-ray testing figures load.

Local build, if Hugo is installed:

```bash
python3 scripts/verify_v89.py
hugo build --gc --minify
hugo server
```

If using `rsync` for a clean replacement, **never delete the `.git/` directory**. Example:

```bash
rsync -av --delete --exclude='.git/' /path/to/unpacked-v89/ /path/to/your/local/repo/
cd /path/to/your/local/repo
python3 scripts/verify_v89.py
git add -A && git commit -m "Deploy V8.9 accurate X-ray validation case" && git push origin main
```

See `V8_9_RELEASE_NOTES.md` and `V8_9_QA.md`.
