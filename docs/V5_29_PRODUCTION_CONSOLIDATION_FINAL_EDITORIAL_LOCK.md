# V5.29 — Production Consolidation & Final Editorial Lock

## Purpose

V5.29 is the production-lock release. It does not add new pages, imagery, features, or visual gimmicks. It consolidates the final hierarchy, ensures the reduction decisions from V5.28 are authoritative, and adds explicit build/cache markers so future live-site QA can verify which release is actually being served.

## Production diagnostics

- Adds `<meta name="portfolio-version" content="5.29">`.
- Adds `data-portfolio-version="5.29"` to the root HTML element.
- Cache-busts `site.css`, `production-lock.css`, and `site.js` with `?v=5.29.0`.
- Adds a dedicated `production-lock.css` loaded after legacy styles. This is the single authoritative final override layer; older versioned CSS remains for backward compatibility but can no longer silently win the cascade.

## Work detail hierarchy

- Hero is centered at the container level, not just text-aligned.
- Long project titles use a compact hero size; shorter titles use the standard size.
- Medical Product keeps three headline facts; Clinical AI keeps three outcome facts; Validation keeps four operational facts.
- Hero capability rows remain removed.
- `AT A GLANCE` is the only brief label; helper copy is removed.
- Sidebar uses five short manual labels rather than full H2 text.
- Reading shell is optically centered and the sidebar behaves as a margin note.
- Technical grids, metric blocks, and responsibility modules use rules and typography instead of card styling.
- Clinical engineering reads as a process list.
- Product research photos are reduced to documentary evidence scale.
- Accreditation context is styled as a footnote.
- Capabilities at page end are inline text rather than pills.

## Cross-page restraint

- Homepage Experience remains free of skill/tag rows.
- Homepage About remains photo-free and closes with the career journey.
- Experience role-end skill rows remain removed.
- Education Academic Focus stays inline rather than pill-based.
- Research Engineering remains a vertical editorial sequence.
- Publication hierarchy prioritizes paper title over venue name.
- About photo is constrained and follows the first narrative paragraph.
- Footer is a compact contact utility with visible email and U.S./Taiwan opportunity note.

## QA intent

This release is intended to stop the iterative patch cycle. Future changes should be content-driven or clearly justified rather than adding additional version-specific visual overrides.
