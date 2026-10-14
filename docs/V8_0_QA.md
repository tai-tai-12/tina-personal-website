# V8.0 Quality Assurance / 驗證報告

## Completed / 已執行

- English and Traditional Chinese pages: **11 each**, matched by relative path.
- `scripts/verify_v8.py`: **139/139** source, navigation-section, static asset, privacy exclusion, and factual-presence checks passed.
- JavaScript: `node --check static/js/site.js` passed.
- All **7 CSS files** parsed without top-level errors using `tinycss2`.
- Resume PDF: one-page US Letter, visually rendered and inspected; SHA-256 checksum matches the exact user-uploaded October 13 PDF.
- Site's canonical resume URL and GitHub Pages baseURL unchanged.
- Current materials were never copied wholesale into the project; original private evidence remains excluded.

## Not claimed / 尚未聲稱通過

- **Native Hugo compilation:** Hugo executable is not installed in this preparation environment, and the environment cannot reach the upstream Hugo release URL. The package therefore does *not* claim a successful Hugo build here. The existing GitHub Actions build remains configured and should validate Hugo compilation when the repository is pushed.
- **Browser visual regression / responsive screenshots:** No rendered deployment or local Hugo server was available for end-to-end browser screenshots. V8 styles were designed as conservative additions to the already-provided V7 system and CSS syntax was checked, but desktop/mobile live visual QA should occur after GitHub Actions succeeds.
- **External hyperlink live status:** External institution/organization pages were preserved from V7 without network revalidation.

## Post-deployment checklist / 上線後檢查

1. GitHub Actions `Build and deploy` is successful; no missing theme or Hugo template errors.
2. On desktop and mobile: Home, Work index, three case studies, Experience, Education, Research, Thoracic Aorta detail, About; both EN and 中文.
3. Home Work 02 shows 94.5% / 264 / 90.16%; clinical detail labels **1,007 → 55**.
4. Future Tech Award is labeled team/project recognition, not a personal prize.
5. Education shows current CMU courses, correctly attributed NYCU courses, Search + Measurement, IBM DBA.
6. Resume downloads the new one-page PDF: DeepBT award, NTUH 1,040 hours, Search & Measurement, 12,125 development scans, 264 independent exams.
7. Test menu, language switch, dark/light mode, Tab keyboard navigation, Escape-to-close, mobile layout and browser print.
8. Confirm no private Materials, original ID/certificate files, transcripts or test reports are accessible on the public static site.
