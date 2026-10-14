# V7.0 — Recruiter-Curated Portfolio & Visual System Lock

## Goal
Turn the V6 series into one coherent production baseline. V7.0 prioritizes recruiter scanning, evidence hierarchy, research discoverability, and cross-page visual consistency rather than adding new content or new component families.

## Global page-header lock
Work, Experience, Education, Research, and About now share the same opening grammar:
1. context icon + eyebrow,
2. page H1,
3. concise introduction,
4. controlled whitespace,
5. thin neutral divider,
6. first content section.

The H1 remains near-black; cobalt blue is reserved for context, links, and selective metadata. No large gradient headers were introduced.

## Research discoverability
- Research eyebrow changed from `SELECTED RESEARCH` to `RESEARCH PROFILE` because the page also contains recognition, engineering, and publications.
- Brain Tumor MRI AI is explicitly framed as primary research.
- Thoracic Aorta CT Analysis remains clearly foundational, but the card is self-contained enough to understand without clicking.
- The aorta preview was rebuilt from the higher-fidelity project visual into a 1200×750 editorial image matching the Brain Tumor preview ratio and visual family.
- The dedicated `/research/thoracic-aorta/` page remains a lighter Research Project Note, not a fourth Work case.

## Evidence rhythm
Rounded metric pills were reduced. Home, Work, and Research previews use a lighter evidence-rail treatment so values read as proof rather than interactive buttons.

Clinical AI preview evidence is now outcome-oriented:
- 264 independent test exams,
- 0.21 FP/scan,
- 90.16% five-class accuracy.

## Selected Work
- Long English project titles keep intentional line breaks.
- Desktop text/image weight is rebalanced.
- CTA buttons are slightly quieter so title, summary, and proof remain primary.

## Education and Experience
- Education header-to-content spacing is reduced so the CMU entry enters the first screen sooner.
- Experience date/location metadata remains secondary but readable; supporting text no longer falls to footnote scale.

## Footer
- Email remains directly visible and copyable; it is not hidden behind an Email button.
- Email weight is regular/medium instead of bold.
- LinkedIn and Resume are visually equal utility buttons in the footer.
- Only one primary email is shown to avoid decision friction.

## Content role split
V7.0 keeps the portfolio distinct from Resume and LinkedIn:
- Resume = qualification and ATS-ready evidence.
- LinkedIn = chronology, completeness, skills, attachments.
- Website = curated interpretation, decisions, trade-offs, visual explanation, and selected proof.

## Guardrails
V7.0 does not reconcile or overwrite unresolved date/cohort definitions. In particular, it does not silently mix alternative Brain Tumor cohort metrics or change AIMISAL dates.
