# V8.6 — Education & Experience Information Architecture Refinement

## Scope

A targeted update to **Education** and **Experience**, not a redesign of Home, Work, Research, or About. The latest resume, case studies, original award photographs and certificates remain preserved.

### Education
- Identical hierarchy in all three degree records: degree → focus → **Selected Coursework** → **Campus Highlights**.
- Fall 2026 CMU courses explicitly labeled *In progress*, not completed credentials.
- Matching course lists with a clean two-column editorial design (one column on mobile).
- Campus Highlights shares the same section header and layout, but retains accurate types:
  - CMU: Student Involvement — MSBA Student Ambassador
  - NYCU M.S.: Ceremonial Representation — went onstage to receive recognition on behalf of graduating students; **not a speaker or student-government position**
  - NYCU B.S.: Student Leadership — Department Student Association President
- Existing professional license, selected honors and five curated certificate groups retain their V8.4 design and verification links.

### Experience
- Common timeline component for all four roles: organization / date → role / scope → **one featured outcome** → selected contributions → optional recognition → relevant links.
- AITEWAN: ~67% reduced processing time (approx. 2 min to 40 sec); physician/center/stakeholder context; release sequencing.
- NYCU Medical AI: 94.5% fewer FP candidates (1,007→55), qualified as retrospective independent evaluation with sensitivity trade-off; 2 actual research projects, engineering as secondary scope.
- NTUH: 1,040 hours over 26 weeks and three rotations; Certificate of Excellence.
- NYCU BIPI: 8 tested regulated products, 5 clients, 10+ reports; two separated workstreams.
- Shared award component visually matches Future Tech and NTUH recognition while distinguishing **team/project** vs **individual internship** achievement.

### Out of scope / privacy
- No Future Tech ceremony photo; no raw academic or healthcare license files.
- No claim of TFDA approval, prospective clinical evaluation, or personal ownership of project award.
- No new claim that the graduation representative was a commencement speaker.

### Deployment
- Replace V8.5 project files with V8.6 project contents including `.github/`.
- Remove old public `portfolio-v85.css` from the repository.
- CI runs `python3 scripts/verify_v86.py` then Hugo build and deploy.
- Expected version marker: `portfolio-version=8.6`, CSS `portfolio-v86.css?v=8.6.0`.
