# V5.24 — Final Content, Semantic & Consistency QA

## Release intent

This is a production-focused pass across the full portfolio. It does not introduce a new visual direction; instead it tightens hierarchy, semantics, naming, recruiter readability, contact discoverability, mobile behavior, and dark-mode consistency.

## Global / Footer

- Visible contact email is now shown on every page: `tinatai@andrew.cmu.edu`.
- Broad location is shown as `Pittsburgh, PA, USA`.
- LinkedIn and Resume remain direct footer actions.
- No phone number or street address is published. A recruiter-facing portfolio does not need either, and leaving them out avoids unnecessary personal exposure.
- Footer semantics and mobile wrapping were improved.

## Homepage

- Selected Work wording remains aligned to three domains: product translation, clinical AI, and regulated technical validation.
- Project 03 wording is stronger and action-oriented: structured testing, evidence packaging, and reporting.
- Homepage Experience tags now stay at the same abstraction level; MATLAB is no longer mixed into the high-level teaser.
- Research abbreviations stay compact on the homepage; full conference names are reserved for the Research bibliography.

## Work Landing

- Project summaries are synchronized with the homepage.
- Medical AI Product now uses an action-oriented summary rather than “Bridging...”.
- Clinical AI summary is shortened and makes cohort separation explicit.
- Validation summary emphasizes structured testing and reporting.

## Work Detail — Medical AI Product

- Reduced to five major case-study headings so the TOC is concise.
- “My role” and product decisions are combined into a 2×2 responsibility module.
- Product workflow and research architecture are separated more clearly.
- MIDL and AMLDS are now equal Research Evidence cards rather than uneven sections.
- Research evidence and regulatory execution are consolidated into one evidence/impact section.
- Hero remains a faint background visual; no large hero image is inserted below the title.
- Ends with Capabilities Demonstrated rather than a résumé-like Skills section.

## Work Detail — Clinical AI

- Reduced to five major headings.
- Study scope is organized as Development / Independent Test / Centers.
- Results use value / metric / denominator-subscope semantics.
- Tooling is grouped into Imaging Pipeline / Modeling / Evaluation & Data instead of a keyword dump.
- Research engineering and research communication are consolidated.
- Mobile image height is constrained so figures do not dominate the viewport.

## Work Detail — Third-Party Testing & Validation Operations

- Testing and quantitative-imaging responsibilities are explicitly separated.
- Accreditation language is shortened to a small contextual note.
- Results use semantic metric cards with supporting scope.
- MATLAB quantitative CT is presented as a separate workstream rather than being conflated with accredited testing.
- Reduced to five major headings.

## Experience

- AITEWAN capitalization is standardized.
- AITEWAN keeps the four-part Product / Validation / Regulatory / Execution scope row.
- Wu Lab’s redundant Research Engineering deep link is removed.
- Thoracic Aorta navigation now points to the Foundational Research section.
- Chen Lab copy is more direct and distinguishes testing from quantitative imaging.
- NTUH Certificate of Excellence has clearer visual hierarchy.

## Education

- All three degrees remain parallel: institution / unit / degree / descriptor / Academic Focus / optional coursework.
- Degree-level Research & Recognition / Related Project CTAs are removed.
- Outstanding Thesis Award appears only under Honors & Credentials, not repeated under the degree.
- `CURRENT FOCUS` / `FOUNDATION` inconsistencies are standardized to `ACADEMIC FOCUS`.
- Technical certificates remain a lighter `ADDITIONAL TRAINING` layer.
- AMLDS in Honors stays abbreviated because the full conference name belongs in the bibliography.

## Research

- Brain Tumor and Thoracic Aorta remain parallel research areas.
- Thoracic Aorta is labeled `FOUNDATIONAL RESEARCH · NSTC`.
- Upper Research Areas no longer repeats AUC / DSC; the detailed Foundational Research block owns those metrics.
- Featured Outputs subtitle is shortened to `One research program, two complementary outputs.`
- Recognition clarifies that `Medical Imaging & Diagnostic AI` is a session.
- Research Engineering tags keep explicit separators for accessible text rendering.
- Selected Publications & Presentations now spells out:
  - Medical Imaging with Deep Learning (MIDL)
  - 2nd International Conference on Advanced Machine Learning and Data Science (AMLDS)
  - 44th Annual Meeting of the Taiwanese Society of Biomedical Engineering (TSBME)
- Each entry now includes output type: Short Paper Poster / Oral Presentation / Conference Paper.

## About

- Duplicate opening paragraph is removed.
- Capability naming changes `Machine & Deep Learning` to `Machine Learning & AI`.
- Stakeholder context is converted from a floating paragraph into a two-part evidence strip.
- Leadership remains reverse chronological.
- Earlier Activities and Outside Work stay separate.

## Production QA completed

- Parsed `hugo.toml` successfully.
- Parsed all public Markdown YAML front matter successfully.
- Verified all six Work case studies have exactly five H2 sections.
- Checked all local image references used by public templates/content; no missing referenced image files were found.
- Checked public layouts/content for stale phrases and old anchors.
- Confirmed footer exposes location + full email and does not expose a phone number.
- Added dark-mode overrides for case-study cards/hero.
- Added mobile figure-height constraints.
- Checked Hugo template brace counts for basic syntax sanity.
