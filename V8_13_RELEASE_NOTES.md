# V8.13 — Bilingual Localization & Final Layout Polish

## Improvements

**Traditional Chinese localization**
- Education: Carnegie Mellon University → 卡內基美隆大學; National Yang Ming Chiao Tung University → 國立陽明交通大學. Institute, department, degrees, fields of focus, selected course names and campus highlight labels are localized.
- Award names verified against Material: 書卷獎, 傑出口頭報告獎, 傑出論文獎・第一名; the NTUH letter identifies the award as 放射腫瘤科實習表現優異獎.
- Selected certifications receive reader-friendly Chinese descriptions while certificate verification links and official English page names remain available in the English version.
- Home, Experience, Research, About, navigation utilities and key case-study labels now use Chinese by default on the Traditional Chinese locale. Established names/acronyms (MIDL, AMLDS, CS50, Google Ads, IBM, MRI, CT, AI) remain as needed.

**Visual**
- Home `05 / ABOUT`: align right-hand paragraph with left-hand section heading on desktop. On tablet/phone the two-column layout still collapses to a single natural vertical stack.
- The longer university and award names were checked for wrapping at desktop, tablet and mobile widths. Preserve existing design rather than adding cosmetic icons or animations.

**Unchanged**
- All routes, complete project and research case studies, proof metrics, latest resume PDF, team award attribution, and scoped TAF/client-testing description.
- Original named scientific papers remain in English for exact citation and searchability.

## Validation caveat

Template-based Chromium previews and source-file checks passed. **An actual Hugo build and pixel-level test of the newly deployed pages were not performed in this authoring environment.** The CI workflow remains the final build gate.
