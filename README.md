# Tina Tai Personal Website — V8.16.2

Complete Hugo / GitHub Pages **Full Replacement** source ZIP; files are placed at ZIP root, including `.github/`.

## Scope of changes

- DeepBT A+ 2026 dual-award text on Home, Experience, and Medical AI Product Case Study, in English and Traditional Chinese.
- Parallel equal-weight recognition cards for the 2026 Future Tech Award and **23rd National Innovation Award — Academic Research category (第23屆國家新創獎－學研新創獎)**.
- The official winning entry name is preserved verbatim: 「醫療 AI 工作流整合平台實現從腦瘤影像分析到報告生成的智慧輔助」.
- Future Tech Award keeps its existing official project link. National Innovation Award has **no linked official award page** until the specific 2026 award entry page is publicly available; old-year award links are not substituted.
- Both are explicitly team/project recognition; neither is represented as an individual award. No new award photo is introduced.
- Website Resume PDF updated *only* in the AITEWAN Product Validation & Recognition bullet. It remains one page. Existing skills, other experience entries, links and document sections are retained.
- V8.16.1 Work, FairPay, research evidence and layouts remain otherwise unchanged. Independent, versioned CSS files prevent stale browser styles.

## Deploy — full replacement

1. Back up current V8.16.1 project. If using a local Git checkout, retain `.git/`.
2. Remove old website source files and copy **all files from this ZIP root** into repository root, including hidden `.github/`.
3. Optional: run `python3 scripts/verify_v8162.py` and `node --check static/js/site.js`.
4. Commit and push to `main`. Confirm both GitHub Actions `build` and `deploy` succeed.
5. Check source metadata for `portfolio-version = 8.16.2`; verify EN/ZH Home, Experience, Medical AI Product Case Study and the Resume PDF.

## Evidence boundary

2026 National Innovation Award category and the exact official project title are taken from the award-notification text supplied by the site owner. The official public project-level URL is not yet included; this does not imply the award is unconfirmed. The English award category rendering is a descriptive translation, not asserted to be the award administrator's registered English category title. Formal recipient and award photo must not be inferred to be the website owner individually.

The local environment could not complete a full Hugo build or a Chromium screenshot capture. Passing source checks does not guarantee production deployment. The GitHub Actions build and visual post-deployment check remain required.
