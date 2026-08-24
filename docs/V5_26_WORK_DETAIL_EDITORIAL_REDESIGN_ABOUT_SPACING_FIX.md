# V5.26 — Work Detail Editorial Redesign & About Spacing Fix

## Why this release

V5.26 addresses two visual-production issues identified from live desktop screenshots: the three Work case-study pages were not truly centered on wide screens and still read as a repeated template system, while the About page had an oversized empty band between its intro and first visual.

## Work detail pages

- Explicitly centers the entire hero composition on the viewport using a fixed max-width shell with auto inline margins.
- Removes pill-heavy/card-heavy hero styling. Project capabilities are now a quiet text line; facts are typographic rather than dashboard cards.
- Replaces the boxed Project Snapshot with an open Project Brief: a short editorial intro plus four ruled fields.
- Centers the body composition as a unit and brings the margin navigation inward.
- Keeps the navigation small, sticky, and limited to five top-level sections.
- Removes the repeated box/card language from role grids, study scope, results, tooling, and capability sections. These now use open ruled editorial structures.
- Keeps research evidence image-led, but removes surrounding card chrome.
- Constrains figures so they can break wider than the copy without becoming full-page banners.
- Reworks Related Work into quiet text navigation rather than another card grid.
- Preserves project-specific faint hero imagery at low opacity without inserting a large image below the title.
- Mobile and dark-mode behavior are included.

## About

- Reduces hero bottom spacing.
- Removes excessive top padding before the first About image.
- Removes the first figure's extra top margin.
- Constrains the thesis-presentation image height so the opening story flows continuously.

## Scope

This release intentionally leaves Home, Work landing, Experience, Education, Research, and global navigation structure unchanged. It focuses on the three project detail pages and About opening rhythm.
