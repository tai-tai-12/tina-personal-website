# V8.4 QA · Evidence Visual and Credential Directory

## Executed checks

- `python3 scripts/verify_v84.py`: **174 / 174** source checks passed before final re-run. Tests include English and 繁體中文 content, research numbers, official team recognition, reused cards, all six personal credential URLs, asset references, privacy boundaries, CSS single entry point, and latest Resume hash.
- CSS parsed using `tinycss2`, JavaScript parsed using Node.js `node --check`: no syntax errors.
- Chromium / Playwright on template-composed **Home, Work, Education (EN and 繁中)** at **1440, 768, 390, and 360 px**: **24 variants**, no document horizontal overflow, no `.evidence-visual-v84` element overflow/cropping, and consistent credential item font sizes within each viewport.
- A first browser pass discovered clipping at small heights and a wrapping `1,007`. The actual CSS was corrected; the final browser pass detected neither problem.
- Tested source document vs `static/resume/Shih-Ting_Tai_Resume.pdf` with SHA-256: identical.
- No source research metrics, raw credentials or identifying clinical artifacts were knowingly altered or made public.

## Verification URLs

Each URL was extracted from an uploaded original credential PDF/JSON; actual public endpoint reachability was **not** tested (network disabled):

1. Harvard CS50 AI: `https://cs50.harvard.edu/certificates/1d4e0491-7302-4f56-84c1-fffb139622ae`
2. Google Ads Search: `https://www.credential.net/81142a9a-5143-4e81-97be-9354d8667e3e`
3. Google Ads Measurement: `https://www.credential.net/f2b46cae-5532-4190-80f1-9da00bf7dd7d`
4. IBM Data Science Fundamentals Specialization: `https://www.coursera.org/verify/specialization/FJCM0NEN2YEI`
5. IBM DBA Professional Certificate: `https://www.coursera.org/verify/professional-cert/TEEVL5E2DS84`
6. UC Davis Tableau: `https://www.coursera.org/verify/FSKBD3NK1OJD`

## Release gates still required

- Hugo 0.164.0 **production build** through GitHub Actions (not available locally).
- Open live English and Chinese Home, Work and Education at 1440 / 390 / 360 px; verify style, text, dark mode and links. Confirm all case-study and research detail routes still work.
- Confirm public credential verification endpoint reachability before relying on links for recruiting applications.
- Confirm the deployed source marker and version query string both say 8.4, with no cached 8.3 CSS.

**Disclaimer**: The browser checks used local HTML rendered from the changed template structure with the actual V8.4 stylesheet. They are not full production screenshots and do not substitute for Hugo rendering or a final live-site Visual QA.
