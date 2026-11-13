---
title: "FairPay AI — Evidence-Led Billing"
translationKey: fairpay-ai
independent: true
weight: 4
category: INDEPENDENT BUILD · AI PRODUCT
summary: A hackathon prototype that checks AI-extracted contract terms against source evidence, keeps financial review explicit, and requires human authorization before PayPal Sandbox invoice drafting.
description: "FairPay AI is a hackathon prototype for evidence-led agreement review and guarded invoice drafts, demonstrated with synthetic data and PayPal Sandbox."
heroSize: compact
heroBackground: images/projects/fairpay-evidence-flow-v814.svg
detailHero: images/projects/fairpay-evidence-flow-v814.svg
heroDek: Designing a human-reviewed agreement-to-invoice workflow where AI suggestions do not become billable amounts without source evidence and authorization.
heroStats:
- value: "3"
  label: Product screens
- value: "161"
  label: Focused local checks reported
- value: "Sandbox"
  label: Invoice drafts only
snapshot:
- title: Problem
  body: Contract terms, milestone acceptance, credits, and invoices can drift across tools. AI-generated values can introduce additional mistakes.
- title: My focus
  body: Product problem framing, evidence-first workflow design, safety gates, prototype demonstration, and documenting testing limits.
- title: Prototype
  body: A local, single-user app with Overview, Agreements, and Payments screens; local AI extraction and optional PayPal Sandbox testing.
- title: Boundary
  body: Synthetic data and illustrative scenarios only. Not a hosted product, verified settlement system, or live payment service.
relatedPrevTitle: Running Client-Facing Validation Operations
relatedPrevURL: work/structured-validation/
navItems:
- id: problem
  label: 01 Product Problem
- id: decisions
  label: 02 Design Decisions
- id: tour
  label: 03 Product Tour
- id: evidence
  label: 04 Testing & Limitations
- id: takeaway
  label: 05 Takeaway
---

<span id="problem"></span>
## The risk is not just an incorrect invoice. It is an unsupported billing decision.

Freelancers and small service teams often keep agreements, milestone approvals, credits, and invoices in different places. A fee may appear clearly in a contract, but that does **not** mean the amount is ready to invoice: a credit might need review, the milestone may not be accepted, or a newer amendment may not be signed. When AI extracts a number incorrectly, automation can make that mistake move faster.

**FairPay AI** is a hackathon prototype exploring a safer workflow: **source evidence → human review → financial checks → explicit authorization → PayPal Sandbox invoice draft**. The prototype is designed to keep evidence and billing permission separate.

<span id="decisions"></span>
## Three decisions behind the prototype

<div class="fairpay-decision-grid">
  <article><span>01 · EVIDENCE BEFORE AUTOMATION</span><h3>Make the source auditable</h3><p>Local AI proposes fees, milestones and relevant excerpts. The user reviews the actual agreement before accepting a suggestion. In one fictional example, the AI proposed <strong>$50</strong>, while the quoted milestone was <strong>$500</strong>; the discrepancy was identified and corrected against the source.</p></article>
  <article><span>02 · FINANCIAL RULES ARE SEPARATE</span><h3>Do not treat matching text as money owed</h3><p>Agreement amounts, manually entered credits, and outstanding balances are separate records. Acceptance, credits, missing evidence, and discrepancies can prevent an invoice from being drafted.</p></article>
  <article><span>03 · HUMAN AUTHORIZATION</span><h3>Keep invoice actions explicit</h3><p>The prototype uses PayPal Sandbox for draft workflows. A demonstrated existing <strong>$400 Sandbox DRAFT</strong> belonged to a separate fictional scenario. It was <strong>not sent, paid, or bank-verified</strong>.</p></article>
</div>

<span id="tour"></span>
## Explore the three product screens

The images below are **actual screenshots of the local FairPay prototype using synthetic examples**. They are hosted in the public project repository. Each screen documents a distinct demonstration, not a single completed payment transaction.

<div class="fairpay-screens">
  <figure class="fairpay-screen"><img src="https://raw.githubusercontent.com/tai-tai-12/fairpay-ai/main/assets/fairpay-overview-demo.png" loading="lazy" decoding="async" alt="Actual FairPay AI Overview screen with read-only synthetic billing decision examples"><figcaption><strong>01 · Overview.</strong> Compare a fictional $500 fee with a $100 manually recorded illustrative credit, and separately inspect an unsigned-amendment scenario. These previews do not save projects or contact PayPal.</figcaption></figure>
  <figure class="fairpay-screen"><img src="https://raw.githubusercontent.com/tai-tai-12/fairpay-ai/main/assets/fairpay-agreement-evidence-demo.png" loading="lazy" decoding="async" alt="Actual FairPay AI Agreements screen showing an AI $50 suggestion corrected against a $500 source excerpt"><figcaption><strong>02 · Agreements.</strong> Compare an AI-proposed $50 amount with a source excerpt stating $500. Source matching still does not establish milestone acceptance or authorization to bill.</figcaption></figure>
  <figure class="fairpay-screen"><img src="https://raw.githubusercontent.com/tai-tai-12/fairpay-ai/main/assets/fairpay-payments-review-demo.png" loading="lazy" decoding="async" alt="Actual FairPay AI Payments screen showing unresolved review and a blocked invoice"><figcaption><strong>03 · Payments.</strong> The prototype blocks invoice drafting while credits and approval evidence remain unresolved. No PayPal invoice was created in this screenshot.</figcaption></figure>
</div>

<div class="fairpay-action-links"><a href="https://www.youtube.com/watch?v=pivk3KyXpEQ" target="_blank" rel="noopener noreferrer">Watch the 3-minute demo ↗</a><a href="https://github.com/tai-tai-12/fairpay-ai" target="_blank" rel="noopener noreferrer">GitHub repository ↗</a><a href="https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/PRODUCT_TOUR.md" target="_blank" rel="noopener noreferrer">Product tour &amp; screenshots ↗</a></div>

<span id="evidence"></span>
## What was tested — and what was not

The public release documents **161 focused checks passing in a local run on November 4, 2026**. They covered current regression checks, synthetic evaluation cases, isolated HTTP checks, and frozen adversarial cases. This does **not** mean every historical test passed: the project's validation document preserves older failures and an incomplete external verification step.

**Scope and limitations:** FairPay runs locally, uses synthetic data, requires separately configured local AI for extraction, and can work with PayPal Sandbox credentials for authorized draft testing. It has no production authentication, real customer payments, verified bank settlement, or public hosted payment service. The $50/$500 correction, blocked billing decision, and separate $400 Sandbox draft are **different scenarios**.

<div class="fairpay-action-links fairpay-subtle-links"><a href="https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/VALIDATION.md" target="_blank" rel="noopener noreferrer">Validation and limitations ↗</a><a href="https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/DEVELOPER_GUIDE.md" target="_blank" rel="noopener noreferrer">Reproduce locally ↗</a></div>

<span id="takeaway"></span>
## Takeaway

This build demonstrates **AI product judgment beyond the model itself**: make AI output traceable, preserve business and financial rules, and design explicit human approval around higher-stakes actions. It broadens my product portfolio beyond healthcare without claiming production adoption or real financial impact.

<div class="case-capabilities-v523"><span class="case-capabilities-label-v523">CAPABILITIES DEMONSTRATED</span><div class="case-capabilities-chips-v523"><span>AI Product Design</span><span>Problem Framing</span><span>Financial Workflow Design</span><span>Evidence Review</span><span>Human-in-the-Loop Controls</span><span>Prototype QA</span></div></div>
