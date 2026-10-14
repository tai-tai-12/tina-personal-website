# V8.12 — Final Portfolio Stabilization

This is the **final full-replacement** source package based on V8.11.

## Changes

1. **Clear active page in header:** Work, Experience, Research, Education or About is indicated with a modest underline and `aria-current="location"`; Case Studies inherit Work and the Aorta research detail inherits Research.
2. **Chinese Research labels:** Numeric evidence labels for the two research cards are bilingual rather than leaving English-only `medical centers`, `tumor classes`, and `CT cases` in the Chinese view.
3. **Chinese AI case summary:** Basic cohort cards and introductory evaluation sentence use understandable Traditional Chinese. Canonical sample sizes, tumor metrics, definitions, and limitations remain unchanged.
4. **Chinese Medical AI case:** Hero metric and image alt text localized.
5. **Education precision:** Graduation-stage representative text clarifies representation during the ceremony; not a commencement speech, individual research award, or elected governance position.
6. **Metadata readability:** Restrained Research publication year and card metadata size corrections, with responsive navigation underline.
7. **Accessibility:** Skip-to-content text uses the page language.
8. **Version hygiene:** Only current `portfolio-v812.css`, `home-v812.css`, `verify_v812.py` and V8.12 release docs remain; all original PDF resume and public research artifacts are preserved.

## Explicitly unchanged

- Home content/order, three Work graphics, Product Manager priority, compact Test Manager experience, all case-study evidence and outcomes, publications, awards, original research photos and CT results, five selected certification groups, and Resume.
- No new photos, decorative badges, fake product captures, parallax, animated counters, or inferred business outcomes.

## Post-deploy freeze checklist

- Confirm GitHub Actions Hugo build and page deployment succeed.
- Confirm source marker `portfolio-version: 8.12`.
- Check English & 中文 home, Work, all three detailed cases, Research / Aorta, Experience, Education, About.
- Check phone widths 360–390px and desktop 1440px; light/dark; menu, language, navigation active state; Resume; publication PDFs; external credential sources; alt text and focus.
- Archive ZIP and avoid further changes unless correcting factual errors, broken links, job-search updates or security/accessibility issues.
