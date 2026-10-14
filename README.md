# Tina Tai — Personal Portfolio V8.10 (Full Replacement)

This archive contains **all source files** required for the bilingual Hugo / GitHub Pages website. It is **not** an incremental patch. ZIP entries start at the repository root (`.github/`, `hugo.toml`, `content/`, `layouts/`, `static/`, `scripts/`, `themes/`).

## Replace the website safely

1. Back up your existing repository. Extract this ZIP into an empty folder, not into the old website source directory.
2. Copy **all ZIP contents**, including hidden `.github/`, into the repository root, replacing previous source files. You may remove the old website source tree first, but **never delete local `.git/`**; keep repository metadata, branches and history.
3. If using `rsync`, a safe example is:

```bash
rsync -av --delete --exclude='.git/' /path/to/unpacked-v810/ /path/to/local/repo/
cd /path/to/local/repo
python3 scripts/verify_v810.py
git add -A
git commit -m "Deploy V8.10 bilingual recruiter-clarity update"
git push origin main
```

4. GitHub Actions (`.github/workflows/hugo.yaml`) runs source checks, builds Hugo and deploys GitHub Pages. If Hugo is installed locally, you can also run `hugo build --gc --minify`.
5. Once deployed, view HTML source and confirm `<meta name="portfolio-version" content="8.10">` and CSS `portfolio-v810.css?v=8.10.0` / `home-v810.css?v=8.10.0`.
6. Verify English and Traditional Chinese at Home, Work, Experience, Research, and the three cases. In particular, open the X-ray validation case on desktop and mobile. Test Resume download and project/official links.

## Accuracy guidance

- **Industry follow-up**: the supervising professor generally made initial contact and passed contacts to Tina for follow-up. Tina then explained testing/consortium services, coordinated membership and agreement paperwork/signing logistics, welcomed clients, personally performed X-ray tube testing, and wrote third-party reports. **Do not claim cold prospecting, independently signed contracts, new-customer acquisition, or personally accredited status.**
- **One workstream**: 8 devices, 5 client organizations, and 10+ reports all describe the same consortium-linked third-party testing work.
- **Separate research**: MATLAB small-animal CT quantitative bone analysis used by two university labs is separate from consortium testing.
- **TAF**: the related laboratory holds defined ISO/IEC 17025 accredited testing scopes; this does not imply each assignment, report, or individual held accreditation.
- **Clinical AI**: 264 retrospective test cases; 94.54% fewer false-positive candidates accompanied a lesion sensitivity change from 84.96% to 80.97%. No prospective outcome claims.

Read `V8_10_RELEASE_NOTES.md` and `V8_10_QA.md`. This package includes the latest resume unchanged, all needed images, both languages, the Hugo theme, and deployment workflow. It contains no private certificate scans, client names or Future Tech Award photograph.
