# V5.13 — Page Context & Validation Role Fix

## 1. Page eyebrow/context label
The top-left page label no longer falls back to `TINA TAI` on single pages.

Page-specific labels now render consistently:
- EXPERIENCE
- EDUCATION & CREDENTIALS
- RESEARCH & RECOGNITION
- SELECTED WORK
- ABOUT
- project-specific category labels on case studies

Implementation:
- strengthened `layouts/partials/page-context.html`
- added `contextLabel` front matter to single-page sections as a fallback

## 2. Project 03 corrected
The former “Building Repeatable Validation & Analytics Workflows” mixed two separate activities.

It is now reframed as:
**Third-Party Testing & Validation Operations**

Primary story:
- NYCU Ionizing Radiation Testing Laboratory
- industry–university technical collaboration consortium operations
- third-party equipment testing
- quality-system documentation
- testing report production
- audit / assessment readiness

The homepage and Work page now use a real-document visual assembled from:
- testing-service material
- TAF accreditation certificate
- representative test report

## 3. BMD analysis separated from testing
MATLAB-based small-animal CT bone-mineral-density analysis is now explicitly described as a separate research-support workstream, not part of the third-party product-testing reports.

## 4. Experience page improved
The Prof. Chen lab entry now shows two distinct workstreams:
1. Third-party testing & consortium operations
2. MATLAB quantitative CT analysis

It also includes an external link to Prof. Chen's lab website.

## 5. Claim precision
The case-study wording distinguishes:
- the laboratory's ISO/IEC 17025 / TAF accreditation for defined scopes
- non-TAF testing services when applicable

It does not claim that every report was TAF-accredited.
