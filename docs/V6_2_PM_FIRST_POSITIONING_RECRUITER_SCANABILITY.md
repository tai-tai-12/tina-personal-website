# V6.2 — PM-First Positioning & Recruiter Scanability

## Release goal

Selectively apply the strongest recommendations from the latest positioning review without turning the portfolio into a generic PM site or hiding the technical depth that differentiates Tina.

The core positioning is now:

**Product Manager first → AI/ML & analytics depth second → healthcare as differentiated domain expertise third.**

## Recommendations accepted

### 1. PM-first homepage positioning

Homepage hero now leads with:

- Product Manager
- AI/ML × Analytics
- User needs + technical evidence + trade-offs → executable product decisions
- CMU Tepper MSBA ’27 · Medical AI PM experience

The exact phrase “Former Medical AI PM” was not used because it is unnecessarily backward-looking. “Medical AI PM experience” communicates prior ownership without making employment status the headline.

### 2. PM-first About narrative

About now starts with product identity and decision-making rather than a researcher-first chronology. The research story remains, but functions as the technical foundation for product judgment.

Healthcare remains visible as a differentiated area of depth, not the top-level job category.

### 3. Recruiter-oriented case-study titles

Display titles were reframed around the problem / decision being demonstrated while preserving the existing URLs:

- Shipping Medical AI Under Real Clinical Constraints
- Designing AI Evaluation Beyond Accuracy
- Running Client-Facing Validation Operations

This improves transferability without changing established links.

### 4. Medical-AI case: stronger evidence discipline

The progress-indicator wording now says it was proposed from physician feedback and subsequently deployed. The previous “positively received” language was removed because deployment is the stronger, more defensible proof point.

### 5. Clinical-AI case: technical depth moved lower

The reasoning and clinical-insight story now leads. Detailed tools are preserved under a compact “Technical details” disclosure instead of occupying early-page visual priority.

### 6. Validation case: client-facing framing

The case now foregrounds requirement scoping, technical execution, issue / retesting communication, and formal reporting. Quantitative imaging remains a distinct secondary workstream rather than being conflated with accredited testing.

### 7. CMU Student Ambassador

Education now adds a single Leadership & Community line under CMU:

- MSBA Student Ambassador

It is intentionally not turned into a large new section.

### 8. SEO / browser-title alignment

Site title and default description now reflect the PM-first positioning:

- Tina Tai — Product Manager | AI/ML & Analytics

## Recommendations deliberately modified or not applied

### “Former Medical AI PM”

Not used. It is accurate in spirit but makes the brand sound backward-looking. The site uses “Medical AI PM experience” instead.

### Healthcare removal

Not applied. Healthcare remains a meaningful differentiator across the site, but is no longer the first recruiter category in the hero / SEO positioning.

### Full technical simplification

Not applied. Tools and research engineering remain available because they materially differentiate Tina for AI PM / technical PM roles. They are simply moved lower in the reading hierarchy.

### LinkedIn Featured / LinkedIn Projects / custom domain

Not changed in this website package. Those are separate profile / distribution tasks rather than site-content changes.

### NYCU date reconciliation

No website date changes were made. The current website and current resume use the same 2023–2026 AI Lab range. Any remaining LinkedIn mismatch should be reconciled at the source rather than guessed in the site.

### Brain-tumor metric reconciliation

No research metrics were silently replaced. The portfolio continues to separate development-scale figures from the final independent-cohort thesis metrics. The 12,437 / 73.2% / 90.13% resume figures should be reconciled against their exact cohort / denominator before they replace any website metric.

## Recruiter-readability changes carried into V6.2

- Experience date / location / employer metadata remains enlarged from V6.1.
- AITEWAN adds a compact, non-pill impact row:
  - 5 physicians
  - 2 medical centers
  - ~67% faster processing
  - June TFDA timeline maintained
- NTUH Certificate of Excellence now has a small line icon and clearer hierarchy.
- Education Selected Honors uses restrained award icons rather than certificate images.
- Footer keeps one primary email only.
- Email is no longer bold.
- LinkedIn and Resume are now small utility buttons.
- Body line length stays constrained for comfortable scanning on wide monitors.

## What V6.2 intentionally does not add

- no new certificate gallery
- no new hero images
- no new animations
- no second footer email
- no new research metrics
- no route / URL changes
- no large architecture redesign

## QA completed

- `hugo.toml` parsed successfully.
- 20 Markdown files parsed with valid YAML front matter.
- All six EN / ZH Work cases retain exactly five H2 sections and five navigation items.
- 25 referenced local static assets were checked; zero missing.
- Hugo-template delimiter counts were checked for basic syntax sanity.
- CSS brace counts were checked.
- V6.1 version-specific stylesheet was consolidated into `v62-recruiter-polish.css`; the old V6.1 file is no longer loaded.
- Portfolio version marker and cache-busting query strings were advanced to 6.2.
