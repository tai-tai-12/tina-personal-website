# V8.16.1 — Release Notes

Base version: **V8.16**, with a strictly limited Work-page readability and print-quality update.

### Website content
- English Work intro: “Three core case studies in medical AI product delivery, model evaluation, and client-facing device validation, plus an independent AI product build.”
- Traditional Chinese Work intro: “三個核心案例涵蓋醫療 AI 產品交付、模型評估及客戶導向的設備檢測；另有一項獨立 AI 產品作品。”

### Printing
- Work cards use grouped page-break behavior and their CTAs remain within the same card when the printing engine and page size permit.
- Print-only grid uses compact two-column cards with reduced vertical padding to reduce page waste.
- CTA links have high-contrast dark ink/borders on white paper; visible without printer background graphics.
- Existing keyboard skip link and modal zoom UI remain hidden only in print, not on screen.

### Unchanged
- All 4 Work projects, 3 original core case studies, FairPay source-check image and details, bilingual pages, actual project screenshots, other research and education content, publication links, Resume PDF, and interactive web features are preserved.
- GitHub Actions retains the prior Hugo build workflow; only the verifier filename and release name are changed.

### Acceptance
- `python3 scripts/verify_v8161.py`
- `node --check static/js/site.js`
- CSS parse with tinycss2; zip integrity and fresh extraction.
- Print layout validation; final Hugo build and deploy must be confirmed on GitHub Actions.
