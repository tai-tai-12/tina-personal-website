# Tina Tai Website · V8.2 Visual Refinement

**Build target:** Hugo 0.164.0 · GitHub Pages · English and Traditional Chinese

## Changes by page

| Page | V8.2 change | Why |
|---|---|---|
| Home / Hero | Restrained 52–68px name scale; lead paragraph max measure; portrait bounds | Avoid competing typographic elements |
| Home / Work | Case titles standardized around 31–41px on desktop; images 16:10 with a 354px cap | Work details should not be three additional hero sections |
| Home / Experience | Replaced `118px 1.25fr .75fr` with `132px minmax(0,1fr)`; enlarged year and description; added compact clinical internship | Fix unoccupied phantom column and tiny years |
| Home / Research | Equal 4:3 imagery and legible 14–16px metadata | Prevent oversized unequal research images and miniature labels |
| Home / About | Replaced giant quotation with a small headline, narrative bridging Imaging → AI Research → PM → Analytics, and concise foundation modules | Make the career connection intelligible |
| Experience | Team award redesigned as vertical label / title / description / official link; four duplicate decorative scope boxes hidden | Fix broken flex layout and duplication |
| Research | Publications promoted after research areas and before large photos; award images capped; dates ≥14px | Publications are more scannable and visible earlier |
| Education | Degrees and school seals constrained; metadata and coursework made readable | More stable type hierarchy |
| Work overview | About 40/60 image/text split on desktop, bounded images, smaller headings | Recruiter-friendly scanning |
| Medical AI Product | 5 micro-columns grouped into 3 clear phases, preserving doctor confirmation and LLM draft governance | Eliminate 11–13px text and implied implementation claims |
| Clinical AI | Removed standalone duplicate FP chart; candidate counts placed above combined FP/scan and sensitivity comparison | Clear, single evaluation outcome and cost |
| Aorta research | Original NSTC figures capped / object-fit:contain; captions normalized | Keep the scientific content truthful and readable |
| About detail | Consistent paragraph widths, years and supporting rows | Better reading rhythm |
| All pages | `--v82-type-*`, `--v82-space-section`, `--v82-reading`, responsive breakpoints | Consistent editorial design system |

## Data retained and not altered

- Clinical research: 264-case retrospective cohort, 1,007 → 55 FP candidates, 84.96% → 80.97% lesion-wise sensitivity, 94.54% FP reduction, conditional 5-class classification accuracy.
- Medical AI Product: regulatory submission coordination, physician testing, official award verification, measured end-to-end latency improvement, team-vs-individual attribution.
- Academic: CMU MSBA, NYCU degrees, MIDL/AMLDS/TSBME publications, NSTC aorta project, credentials.
- Resume: October 13 2026 file, byte-identical to source.
- No Future Tech Award photograph was added.

## CSS approach

V8.2 ships one public `portfolio-v82.css` asset. Legacy styles are concatenated in original load order (to preserve existing visual components and reduce deployment risk); the clearly marked V8.2 section follows, providing coherent design tokens and explicit component-level refinements. This consolidates delivery and design decisions; it does *not* pretend that the entire historical cascade was manually reduced to a minimal atomic CSS architecture. Old source files are archived in `docs/legacy-styles/` for eventual migration.

## Browser acceptance (required after deployment)

Review at 1440, 1024, 768, 390 and 360px, EN and zh, light and dark. Check homepage section rhythms, all research card crops, date visibility, award badge wrapping, project workflow width, table/chart overflowing, image labels, case TOC anchors, resume PDF and external URLs. Fail if any section creates horizontal scrolling, cropped clinical diagram labels, sub-12px important metadata or an award attribution ambiguity.
