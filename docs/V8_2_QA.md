# V8.2 QA — Performed Checks vs. Outstanding Gates

## Passed in authoring environment

- `python3 scripts/verify_v82.py` — **155 / 155 static source checks**.
- One active public stylesheet `static/css/portfolio-v82.css` (8 old source styles preserved separately in `docs/legacy-styles/`).
- CSS parsed with `tinycss2` with no top-level syntax errors.
- `node --check static/js/site.js` — JavaScript syntax valid.
- English and Chinese source pages, case-study anchored headings, original research figures and key outcome figures present.
- Award photo explicitly excluded; original private credentials / transcripts not published.
- 10/13 PM Resume SHA-256 matches the source upload when mounted.
- Key Hugo layout templates have balanced `{{` / `}}` delimiters.
- ZIP integrity verified after packaging.

## NOT passed / unavailable in this environment

- **Hugo binary build**: Hugo was not installed, the environment could not download a release binary.
- **Real browser screenshot / pixel visual regression**: browser navigation to file / localhost was blocked by runtime policy. CSS and markup were inspected, but rendered screens were not available for visual sign-off.
- **Deployed production check**: requires user's repository deployment and GitHub Actions run.

Do not treat source validation as a substitute for a clean Hugo build and post-deployment browser QA.

## Manual post-deployment checklist

1. Confirm GitHub Actions `Build and deploy` passes validation and Hugo build.
2. Check EN home at desktop 1440px: Hero typography balanced, three Work cards with bounded artwork, experience timeline two columns, 4 research/education/about parts visually aligned.
3. Check Research at desktop: publications appear after research overview, with year badges readable. MIDL and AMLDS photos should not dominate reading order.
4. Check Experience: DeepBT award module is **vertical** and has no fragmented flex text; it attributes recognition to the NYCU team.
5. Check Work detail: 3-stage physician-centered workflow readable; clinical chart integrates 1,007 → 55 FP with sensitivity 84.96 → 80.97%; research/aorta figures contain visible labeling without cropping.
6. Repeat critical pages in zh language. Verify Traditional Chinese wrapping and punctuation.
7. Check laptop 1024px, tablet 768px, phone 390px and 360px for sideways scroll, excessive headings, dark mode contrast, visible metadata and all links.
8. Verify PDF Resume, scientific papers, official award and credential links; test accessibility focus / keyboard and language switch.

