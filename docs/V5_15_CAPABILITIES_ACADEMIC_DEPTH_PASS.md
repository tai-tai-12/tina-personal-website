# V5.15 — Capabilities & Academic Depth Pass

## Purpose
V5.15 builds on V5.14 and focuses on three goals:
1. make the Education page more academically informative without turning it into a transcript,
2. surface a curated capability model instead of a long LinkedIn-style skills inventory,
3. add a light human/community layer without adding another navigation page.

It also includes a QA sweep of V5.14 and carries forward the stability, visual, education-seal, research-engineering, and Project 03 corrections from prior releases.

## V5.14 QA fixes included

### Page-context labels now differ from page titles
Top-level pages use contextual eyebrow labels rather than repeating the H1:
- ACADEMIC BACKGROUND → Education & Credentials
- CAREER PATH → Experience
- SELECTED RESEARCH → Research & Recognition
- PORTFOLIO → Selected Work
- PROFILE → About

The page-context partial now derives these labels from the URL first, so stale `contextLabel` front matter cannot force duplicate labels on top-level pages.

### Credential note shortened
Old:
> Additional IBM, Google, data-engineering, and SQL credentials are kept on LinkedIn so this page stays curated rather than becoming a certificate inventory.

New:
> More technical credentials are listed on LinkedIn ↗

### V5.14 corrections retained
- V5.12 segmented EN / 中文 control
- V5.13 third-party testing / MATLAB bone-analysis workstream separation
- V5.14 cropped NYCU seal and equalized education marks
- V5.14 research-engineering section
- GitHub Pages-safe relative asset paths

## Education updates

### CMU M.S. Business Analytics
Keeps CURRENT FOCUS rather than inventing completed coursework before the program is further along:
- Analytics
- Machine Learning
- Optimization
- Technology Strategy

### NYCU M.S. Biophotonics
Adds SELECTED COURSEWORK:
- Deep Learning & Biomedical Applications
- Machine Learning & Biomedical Applications
- Magnetic Resonance in Medicine
- Medical Device Regulatory Requirements

### NYCU B.S.
Keeps the foundation tags and adds SELECTED COURSEWORK:
- Programming Language
- Principles of Magnetic Resonance Imaging

The coursework is intentionally selective; this is a portfolio, not a transcript.

## About updates

### Capabilities
Adds four curated capability groups:
1. Product & Strategy
2. Analytics & AI
3. Healthcare & Regulated Tech
4. Technical Toolkit

This replaces the need for a dedicated Skills page and avoids copying the full LinkedIn skills inventory.

### Beyond Work
Adds a small section for:
- Lions Club blood-donation service (2025–2026)
- earlier community service spanning animal welfare, fundraising, and environmental service

This section is intentionally light and remains off the homepage/navigation.

## Deliberately not added

### Test scores
GMAT / IELTS / TOEIC remain on LinkedIn and are not added to the portfolio. They add less recruiter value than project evidence, experience, education, and capabilities.

### Full skills inventory
No separate `/skills/` page. Skills are curated by capability and continue to appear contextually in work and experience sections.

### Full volunteer page
No separate `/volunteer/` page. Community involvement is a humanizing About-page layer rather than a primary portfolio navigation item.
