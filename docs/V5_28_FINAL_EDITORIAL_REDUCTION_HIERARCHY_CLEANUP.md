# V5.28 — Final Editorial Reduction & Hierarchy Cleanup

## Release intent

V5.28 is a restraint pass, not a redesign. It removes repeated UI, reduces résumé-like keyword rows, clarifies page hierarchy, and makes evidence and narrative carry more of the visual weight.

## Homepage
- Keeps the lean V5.27 About close: quote + career path + About link, with no repeated thesis photo.
- Experience preview stays narrative-only; no skill-tag wall is added.
- Section numbers remain intentionally low-contrast.

## Work detail pages
- Hero stays editorial and centered with no capability/tag row.
- Medical AI Product keeps only three hero facts: medical centers, TFDA submission, PACS-connected workflow.
- Clinical AI keeps only three headline hero facts: independent test cohort, FP/scan, retained-lesion five-class accuracy.
- Validation keeps four operational facts because breadth is part of the case.
- “AT A GLANCE” stays concise without helper copy.
- Sidebar uses short, hand-authored five-item navigation labels rather than full H2 sentences.
- Medical Product keeps the product/deployment visual and does not repeat the lesion-cascade figure.
- Clinical AI separates study scope from final evaluation results and presents engineering as a workflow rather than a keyword wall.
- Validation keeps regulated testing and quantitative imaging as distinct workstreams; accreditation remains a contextual note rather than a capability badge.

## Experience
- Removes all role-level skill/tag rows. The role descriptions, scope modules, and evidence now carry the meaning.
- Keeps the AITEWAN Product / Validation / Regulatory / Execution scope because it balances the career page and directly explains product responsibility.
- Simplifies the Wu Lab cross-project engineering entry so the label and title no longer repeat “Research Engineering.”

## Education
- Keeps all Academic Focus areas as inline editorial text rather than pills.
- Honors and Additional Training remain visually secondary to the degree entries.

## Research
- Keeps Research Engineering as a vertical editorial sequence rather than a 2×2 feature-card grid.
- Keeps conference full names in Selected Publications & Presentations, while paper titles carry stronger typographic hierarchy.

## About
- Moves one short narrative paragraph before the thesis photo so the photo works as evidence inside the story rather than as a second hero.
- Keeps capabilities and stakeholder context, while V5.28 CSS further reduces card-like treatment.

## Footer
- Keeps the concise contact utility: Tina Tai, Pittsburgh location + openness to U.S./Taiwan opportunities, full email, LinkedIn, and Resume.
- No phone number or street address is published.

## Production QA targets
- English and Chinese Work case pages retain exactly five major H2 sections.
- All manually authored sidebar anchors resolve to IDs present in each case page.
- No résumé-like `.tag-row` remains on the Experience page.
- About content order is narrative → photo → remaining story in both languages.
- Local image references remain present.
