# V5.10 — Education Identity + Work Stack Pass

## Education
- Standardized degree locations to city-level geography:
  - Carnegie Mellon University — Pittsburgh, PA, USA
  - NYCU Institute of Biophotonics — Taipei, Taiwan
  - NYCU Biomedical Imaging & Radiological Sciences — Taipei, Taiwan
- Added official university links and school/unit links.
- Added restrained CMU/NYCU institution marks for faster visual scanning.
- Kept the professional credential separate from the degree timeline so it is not forced into the same location taxonomy.
- Avoided campus-photo backgrounds by default because they compete with degree information and create licensing/crop inconsistency. A future version can swap in user-owned campus photos or official logo files.

## Work
- Rebuilt `/work/` as three full-width horizontal rows stacked vertically.
- Every row uses the same orientation: visual on the left, project copy on the right.
- Removed the mixed card-grid behavior that was causing the layout to feel broken.
- Mobile/tablet collapses each row to visual-above-copy.

## Files changed
- `layouts/education/single.html`
- `layouts/work/list.html`
- `static/css/site.css`
