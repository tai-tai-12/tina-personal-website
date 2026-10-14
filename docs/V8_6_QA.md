# V8.6 QA & Acceptance

- Run `python3 scripts/verify_v86.py` for bilingual content, links, asset, privacy, and version checks.
- Chromium template checks target 1440, 768, 390, 360 px for English/Traditional Chinese Education and Experience (plus light/dark spot checks).
- **Template previews are not official Hugo output**. Formal Hugo build and full production browser regression remain post-deployment checks.
- Confirm no horizontal overflow, clipped figures, overly narrow impact values, broken logos, unsupported award attribution, or different heading hierarchy across degree/role sections.
- Verify all four experience metrics against the supplied October 13 resume and thesis cohort definitions.
- Confirm latest resume PDF SHA-256 matches the supplied October 13 original.
- Recheck official external URLs manually following deployment; offline inspection does not certify remote links are live.
