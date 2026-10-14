# V8.11 Full-Site Recruiter & Visual Audit

Baseline: latest user-supplied **V8.10 full replacement** source (verified against the repository version marker). Target: PM / APM / AI Product / Technical Product Operations / Product Analytics recruiting. The checks below refer to content and layout templates. Not all production pages were directly opened in a live browser.

| Page | Content assessment | Design & interaction assessment | V8.11 action |
|---|---|---|---|
| Home | Clear Product Manager-first identity, 3 strong cases, 4 jobs and 3 degrees. No need for more accomplishments. | Balanced portrait, evidence-based case imagery, concise timelines. | Retain; no new icons or moving elements. |
| Work | Three distinct but visually coordinated evidence panels. Titles and metrics offer direct case entry. | Strong consistent card proportions; miniature labels inside diagrams should remain supplementary, never the only carrier of information. | Retain visual system. |
| Medical AI Product case | Best recruiter proof of user discovery, trade-offs and release/TFDA decisions. The ~67% latency improvement is clear. | Full case content is inherently long; the small desktop side navigation hampered scanning. | Increase case TOC readability; preserve substantiation and team attribution. |
| Clinical AI case | Strong evaluation trade-off: FP 1,007 → 55, sensitivity 84.96% → 80.97% in the 264-case retrospective cohort; five-class accuracy is for retained true-positive lesions only. | Technical evidence is appropriate after a plain-language introduction; diagrams and detailed metrics must retain cohort labels. | Increase TOC readability; do not simplify technical statistics into unsupported clinical claims. |
| Structured Validation case | Faculty introductions → Tina's follow-up, agreements, hands-on X-ray tube testing, third-party reports and membership outreach are one consortium-linked responsibility. CT MATLAB research is independent. | V8.9 original X-ray SVGs correct the prior microscopy mismatch. Distinguish conceptual visuals from real equipment photos. | Preserve case breadth, improve TOC; Experience preview links to it. |
| Experience | The PM lead role deserves more attention than the earlier BIPI entry. Early testing entry was disproportionately long and repeated its case study. | Common role → metric → contribution layout works; repetition was the main defect. | **Shortened BIPI** into two contributions, compact scope and one CT note. PM detail remains untouched. |
| Education | Reverse-chronological CMU + NYCU master's + NYCU bachelor's, correct coursework status and campus highlights. | Shared degree structure and compact credentials are appropriate. | Retain. No extra certificate icons or oversized cards. |
| Research & Recognition | First-author MIDL/AMLDS/TSBME, authentic conference and award photos, NSTC support. | Images have consistent crop; conference metadata needs to remain legible. | Minor metadata readability adjustment only. |
| Thoracic Aorta research | 308 CT studies with relevant AUC/DSC, original images, limitations. | Zoomable authentic figures support technical credibility. | Preserve. Case figure captions slightly more readable. |
| About | Clear transition from clinical imaging to AI, PM and analytics, plus evidence of student leadership. | Portrait plus restrained timeline and experiences serve the goal; no extra motion required. | Retain story and layout. |

## Cross-page design rules

- Maintain Product Manager-first prioritization: not every experience deserves the same number of words or visual prominence.
- Core quantitative work metrics must carry a clear label, denominator/cohort when applicable, and personal-versus-team attribution.
- Titles should be readable without specialized medical knowledge; technical terminology belongs in case bodies rather than on first-screen summaries.
- Use three image types consistently: real personal/conference photography, evidence diagrams, and labeled conceptual workflow drawings.
- Icons should clarify actions, not decorate every heading. Existing arrows and recognized icons are sufficient.
- Animation should remain a restrained once-per-section reveal, respecting reduced-motion; no parallax, count-up animation or autoplay video.
- All navigational elements should be keyboard focusable; links should describe destinations and case images should remain optional evidence, not sole narrative carriers.

## Further manual production QA

Inspect all routes after Github Pages deploy at >=1440px, 768px, 390px, and 360px; use Chrome dev tools for hover and keyboard focus, both languages, light/dark themes. Confirm correct X-ray image proportions and zoom interactions on real devices. Verify current external TAF, institute, paper and credential URLs (offline checks cannot guarantee external link availability).
