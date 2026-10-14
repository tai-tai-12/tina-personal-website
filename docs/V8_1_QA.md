# V8.1 QA Report

## Verified in authoring environment

- V8.1 source assertions: run `python3 scripts/verify_v81.py` (includes translation parity, Hugo frontmatter presence, shortcode/static asset existence, work anchors, award-photo exclusion, date/cohort terminology, evidence sections, and repository privacy scan).
- CSS parsed without syntax errors using tinycss2; JavaScript source checked with Node `--check`.
- Both new NSTC research crops visually reviewed; no obvious personal identifiers in reproduced figures.
- Links inserted from user-supplied credential records and official institution / conference product pages.
- Current resume is unchanged from V8.0; compare to the original supplied October 13 PDF before shipping.
- ZIP will be tested for integrity and excluded files/metadata after packaging.

## Known release limitation

The authoring container did not have a Hugo binary and could not reach GitHub to install Hugo. A formal Hugo compile, interactive navigation and mobile browser-screenshot regression have not been executed here. The GitHub Actions deployment workflow uses Hugo 0.164.0 and now runs the V8.1 source validator before build. **A passing offline verifier is not a substitute for a Hugo build or browser QA.**

## Manual post-deployment checklist

1. Check `/`, `/zh/`, `/work/medical-ai-product/`, `/zh/work/medical-ai-product/`, `/work/clinical-ai-at-scale/`, `/zh/work/clinical-ai-at-scale/`, `/research/`, `/zh/research/`, and `/research/thoracic-aorta/`.
2. In both themes and at phone/desktop widths, check product flow wrap, sensitivity bars, proof notes, award verification link, and original research image scale.
3. Check Resume button and confirm latest October 13 PDF is served, not browser-cached prior PDF.
4. Validate external link accessibility for FUTEX, MIDL scientific program, credential.net, Coursera, and Harvard CS50 (credential providers may use JavaScript/login).
5. Check that `IMG_9931.JPG`, raw transcripts and test screenshots are absent from the repository's public branch.
