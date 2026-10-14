# Tina Tai Portfolio V8.11 — Full Replacement

This archive is a complete bilingual Hugo website, **not an incremental patch**. All paths in the ZIP are relative to the repository root; `.github/` is included. Keep your local `.git/` folder when replacing files via Git.

## Deploy

1. Back up the previous site. Extract this ZIP into an empty directory.
2. Replace all tracked website source files in your Git repository with the extracted contents, including the hidden `.github/` directory. Do not delete `.git/`.
3. Run `python3 scripts/verify_v811.py` (checks source integrity, critical claims, media paths, and version information).
4. Commit and push to `main`. GitHub Actions runs the source verifier and then performs the official Hugo build/deployment.
5. Check source for `<meta name="portfolio-version" content="8.11">` and confirm that `portfolio-v811.css` and `home-v811.css` load with `?v=8.11.0`.
6. Test desktop/mobile and EN/繁中 navigation, case study links, PDF resume, research zoom, light/dark mode and external verification links. Clear browser cache or hard-refresh if old CSS is displayed.

## Scope & factual boundaries

- The main career emphasis is **Product Manager at AITEWAN**. The earlier BIPI testing role is intentionally shorter in Experience; its full evidence remains in the dedicated X-ray case study.
- BIPI: company contacts were initially introduced by the professor; Tina handled follow-up, explained consortium services, coordinated membership and paperwork, received devices and customers, personally performed X-ray tube testing and prepared third-party reports. Do not claim independent cold outreach, signed deals, customer acquisition conversion, or personal TAF accreditation.
- The **8 devices / 5 client organizations / 10+ technical reports** refer to **one** consortium-linked third-party testing workstream. The small-animal CT bone analysis project was separate and adopted by two university laboratories.
- TAF accredits the laboratory for defined methods; it does not accredit each individual or automatically cover every report.
- Brain-tumor AI sensitivity, false positives and five-class results reflect defined retrospective cohorts; avoid presenting them as prospective clinical benefit.
- Resume is unchanged from the supplied October 13 PDF. Do not include personal source material, confidential test records or the excluded Future Tech Award photograph.

## Documentation

- `V8_11_RELEASE_NOTES.md` — what changed in this release
- `V8_11_RECRUITER_AUDIT.md` — page-by-page content and visual audit
- `V8_11_QA.md` — checks completed versus deployment-only checks

This environment did not have the Hugo binary. Browser checks used locally reconstructed templates, not final production Hugo output. The official Hugo build is a required GitHub Actions deployment gate.
