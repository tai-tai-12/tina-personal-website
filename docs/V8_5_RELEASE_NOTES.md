# V8.5 — About Narrative & Leadership Architecture Refresh

Based on the complete V8.4 deployment project. All original Hugo routes, research metrics, publications, verified credentials, and the October 13 resume are retained.

## About

- Rebuilt with a two-column professional introduction, genuine NYCU thesis photo, concise bilingual narrative, four **overlapping** perspectives (not a chronology), two featured leadership roles, a smaller community-activities list, and personal interests/links.
- Department Student Association President (NYCU, 2023–24) is the featured campus leadership role.
- MSBA Student Ambassador is explicitly described as **selected for 2026–27**, not as accomplishments already completed.
- Medical Camp Organizer, University Basketball Team Manager, and Lions Club involvement are retained as supporting experiences without inventing unverified individual dates. Hip-Hop Dance Club member, sign language, Rotary volunteer work, and personal interests are low-key.
- Removed the large repetitive technical-capabilities grid from About, while keeping verified technical skills and products elsewhere on the site.
- Simplified the Home About teaser by removing a duplicate capabilities grid and linking directly to the expanded About story and leadership.

## Education

- NYCU M.S.: graduation-ceremony representative is described as receiving onstage recognition on behalf of the Institute's graduating cohort, **not a commencement speaker, an elected class office, or another academic award**.
- NYCU B.S.: added Department Student Association President, with a route to the richer About explanation.
- CMU Student Ambassador remains where it was; curated license/honors/certifications retain the V8.4 format.

## Research

- Recognition title shortened to **Selected Research Honors** / **精選研究榮譽**.
- Rebuilt two equally structured compact photo + copy cards. Both use original award photos with a fixed 4:3 object-fit crop and independent focal points. No Future Tech Award event photograph is exposed.
- MIDL/AMLDS/publications and original research figures remain unchanged.

## Technical / validation

- One public stylesheet `static/css/portfolio-v85.css` (V8.4 file promoted; the V8.5 component rules are scoped at the end).
- Version marker in HTML/head plus cache busters update to 8.5.0.
- `scripts/verify_v85.py` runs before the Hugo build on GitHub Actions.
- EN/zh preview tests using Chromium at 1440, 768, 390 and 360 px. These are **template-based** checks, not an actual Hugo rendering of the published website.
- The environment lacks a Hugo binary; GitHub Actions remains the authoritative production build gate.
