# V5.21 — Selected Work Detail Editorial Redesign

## Scope

V5.21 focuses on every **Explore Project** page rather than the portfolio landing page.

### Layout
- Rebuilt the work-detail template as a recruiter-friendly editorial case study.
- New oversized title hierarchy, proof chips, skills metadata, and full-width hero visual.
- Added a desktop sticky table of contents and cleaner long-form reading column.
- Added numbered section hierarchy and stronger mobile responsiveness.
- Refined metrics, proof cards, conference evidence cards, captions, and final back-to-work navigation.

### New visual system
Each case now uses a dedicated set of newly produced visuals rather than reusing the older generic diagrams.

**Product Translation**
- Clinical MRI workstation hero
- Physician-centered review workflow
- Deployment / data / governance visual

**Clinical AI · ML**
- Brain MRI analytics dashboard hero
- Lesion-wise cascade visual
- Candidate filtering and evaluation visual

**Regulated Testing · Operations**
- Laboratory testing hero
- Testing / documentation workflow
- Measurement and validation visual

The generated images are used as conceptual portfolio illustrations; captions avoid presenting them as literal screenshots of the underlying clinical or laboratory systems.


## Build hotfix

Fixed YAML front-matter closing delimiters in all six EN/ZH work detail Markdown files. This resolves the GitHub Actions Hugo error: `EOF looking for end YAML front matter delimiter`.
