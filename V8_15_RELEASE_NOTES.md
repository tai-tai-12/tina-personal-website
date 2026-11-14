# V8.15 — Work Consistency & FairPay Readability Refinement

## Information architecture

1. Keep the three original work cases in their established order and preserve their independent evidence-based visuals, descriptions, outcome metrics, and source references.
2. Put FairPay underneath a single **Independent Product Build** classification. Use the same two-column Work row instead of a visually dominating special card; maintain a secondary status through placement and a modest heading.
3. Eliminate the repeated independent category badge, large duplicated section headline, and card-within-card presentation. FairPay title now has a semantic h3 underneath the category's h2.

## Interactions / accessibility

- Apply equivalent 2px hover lift and subtle box-shadow to each linked case visual (the whole element, not inner text/graphs). Keyboard focus has a visible outline; reduced-motion preference disables movement.
- Three documented FairPay screenshots are locally served at `static/images/projects/fairpay-{overview,agreements,payments}-v815.webp` and can be opened via an accessible native dialog; the direct asset link remains a fallback.
- Improve the case navigation's small desktop typography and show current section with `aria-current=location`.
- Print-only CSS hides the Skip Link while preserving keyboard users' access in the live site.

## Content accuracy

- FairPay hero: replaced incomparable numeric items with Product Focus themes; the 161-check QA claim remains in Testing only.
- Clear independent work breadcrumb, concise Problem, My Focus, Prototype and Boundary summaries, readable product-decision cards, concise captions, and a more direct takeaway.
- Explicitly describe the separate $50/$500 correction, synthetic blocked-draft test and $400 Sandbox DRAFT as distinct examples, none a live financial transaction.
- All changed user-facing content is synchronized in English and Traditional Chinese.

## Preservation

No changes to other project outcomes, the homepage three core cases, Experience, Education, Research, About, publications, original image evidence, or the resume. Existing URLs are retained.
