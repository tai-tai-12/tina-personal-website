# V8.8 Quality Assurance

## Offline checks

Run `python3 scripts/verify_v88.py` from the site root. This validates version/cache markers, main navigational routes, the shared metrics component and structured bilingual data, direct research and role navigation, deduplicated sections, source-linked image files, site CSS syntax when `tinycss2` is available, and absence of named private attachments.

## Browser checks

Validate at 1440px, 1024px, 768px, 390px and 360px in both English and Traditional Chinese, including page scrolling, typography, long item labels, metric grids, visible pictures and captions, light/dark presentation, and keyboard accessibility. The source-preview screenshots are not a substitute for browser checks on the formally built GitHub Pages site.

## Remaining deployment gates

- A successful GitHub Actions Hugo build (Hugo 0.164.0 specified in `.github/workflows/hugo.yaml`).
- Production visual confirmation of live site URLs and localized routes after cache propagation.
- Manual activation of external certificate links, LinkedIn and other external destinations (availability can change independently of this package).

## Privacy and integrity

No source transcripts, medical license originals, GMAT or IELTS reports, or the non-scanned Future Tech Award event photo should be included in the website's public static assets. The official resume file is preserved byte-for-byte from the user-supplied Oct 13 PDF when locally available for comparison.
