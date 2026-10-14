# V8.8 — Cross-Page Consistency & Final UX Polish

V8.8 is a complete, bilingual, full-replacement Hugo source tree based on the approved V8.7 site, retaining all three cases, four primary roles, three degrees, recognized research outputs, selected certifications, current Oct 13 resume, and privacy exclusions.

## Changes

- **Shared project outcome strip:** Home and Work now render the same `case-metrics-v88.html` component, with a large number and a readable, qualified label. 90.16% is explicitly the five-class accuracy **on retained true-positive lesions**, not sensitivity or accuracy for all candidates.
- **Reduced duplicate micro-information:** The three unified evidence illustrations emphasize either the workflow or the clinical comparison rather than restating every number already present adjacent to the illustration. Their explanatory text remains available to accessibility readers.
- **Consistent navigation:** Research area cards now navigate directly to the two respective detailed pages. Each homepage Experience timeline item navigates to its own exact role heading. Main navigation order now follows the homepage order: Work, Experience, Research, Education, About.
- **Research editorial consolidation:** MIDL/AMLDS presentation photographs accompany their corresponding publication entries at a controlled size. The separate Featured Research Outputs section is removed; the two Research Honors cards and publications remain unchanged in attribution and substance.
- **De-duplicated thoracic-aorta results:** The hero retains the 308 studies, 0.95 AUC and 0.782 DSC. The Results section focuses on the original research figure instead of repeating the same three numbers.
- **Consistent call-to-action language:** Work uses “Read case study” in both languages, consistent with Home. About gains a direct email link. The Home closing section offers an explicit email CTA and a secondary About link.
- **Cache and version hygiene:** Fresh V8.8 filename entrypoints for CSS, fresh asset cache query, V8.8 version marker, single current source verifier and workflow. Historical validation docs and styles are not part of the deployment package.

## Explicitly preserved

- Future Tech Award is a team/project achievement, not a personal award; the excluded non-scan award photograph is still not published.
- The independent MRI study's 94.54% candidate reduction and associated sensitivity change (84.96% to 80.97%) remain qualified as a retrospective cohort comparison.
- Original published materials, private-file exclusions, source-backed study images, original certifications and verification links.
- Existing site routes, English and Traditional Chinese; no new Projects tab or route needed.

## Build note

The deliverable includes Hugo source and a GitHub Actions workflow, not a pre-built `public/` site. GitHub Actions must complete the Hugo build successfully before V8.8 is considered fully deployed. See QA report for offline test coverage.
