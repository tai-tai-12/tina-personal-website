---
title: FairPay AI — Evidence-Led Billing
translationKey: fairpay-ai
independent: true
weight: 4
category: INDEPENDENT BUILD · AI PRODUCT
summary: A hackathon prototype for source-checked AI contract review, explicit financial controls, and human-approved invoice drafts
  in PayPal Sandbox.
description: FairPay AI is a hackathon prototype for evidence-led agreement review and guarded invoice drafts, demonstrated with synthetic
  data and PayPal Sandbox.
heroSize: compact
heroBackground: images/projects/fairpay-evidence-flow-v815.svg
detailHero: images/projects/fairpay-evidence-flow-v815.svg
heroDek: An evidence-first agreement-to-invoice prototype that separates AI suggestions, financial checks, and human authorization.
snapshot:
- title: Problem
  body: Contract terms, credits, approvals, and invoices live in different tools; AI extraction can compound mistakes.
- title: My focus
  body: Problem framing, evidence-led workflow design, human review gates, and prototype validation.
- title: Prototype
  body: Local, single-user Overview, Agreements, and Payments screens; optional local AI and PayPal Sandbox.
- title: Boundary
  body: Synthetic scenarios only; not a production payment service or verified settlement system.
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
heroThemes:
- AI-assisted contract review
- Source verification
- Human-approved draft workflow
---

<span id="problem"></span>
## An invoice needs evidence and authorization, not just a number.

Freelancers and small service teams track contracts, milestones, credits, and invoices across different tools. Even if an AI system extracts a fee correctly, it may not be ready to bill: acceptance could be missing, credits may need review, or an amendment may be unsigned.

**FairPay AI** explores an evidence-first workflow: **source evidence → human review → financial checks → explicit authorization → PayPal Sandbox draft**. The key decision is to treat a matched contract amount and permission to bill as separate questions.

<span id="decisions"></span>
## Three product decisions behind FairPay

<div class="fairpay-decision-grid">
  <article><span>01 · EVIDENCE BEFORE AUTOMATION</span><h3>Make AI suggestions traceable</h3><p>Local AI proposes fees and milestones with source excerpts for review. In one synthetic example, it suggested <strong>$50</strong> where the agreement said <strong>$500</strong>; the mismatch was identified and corrected against the quoted source.</p></article>
  <article><span>02 · FINANCIAL RULES STAY SEPARATE</span><h3>A matched fee is not an approved invoice</h3><p>Contract amounts, user-recorded credits, and outstanding balances remain distinct. Unresolved acceptance, credit review, missing evidence, or mismatched amounts can block draft creation.</p></article>
  <article><span>03 · EXPLICIT HUMAN AUTHORIZATION</span><h3>Make the final action deliberate</h3><p>The workflow requires review and human approval before a PayPal Sandbox invoice draft. Automation does not independently authorize billing or treat a draft as payment.</p></article>
</div>

<span id="tour"></span>
## Explore the three product screens

These are <strong>real screenshots of the local FairPay prototype</strong> using synthetic examples. Select an image to enlarge it. Each screen documents a separate scenario.

<div class="fairpay-screens">
{{< fairpay-screen src="images/projects/fairpay-overview-v815.webp" alt="FairPay Overview real screen showing two synthetic billing scenarios" title="01 · Overview." caption="Compare a fictional $500 fee with a $100 user-recorded credit, plus a separate unsigned-amendment example. These read-only previews do not save or send anything." zoom="Enlarge screenshot" >}}
{{< fairpay-screen src="images/projects/fairpay-agreements-v815.webp" alt="FairPay Agreements real screen showing an AI $50 suggestion corrected against the $500 source" title="02 · Agreements." caption="Review an AI-proposed $50 amount against a source stating $500. Correct source matching still does not imply approval to bill." zoom="Enlarge screenshot" >}}
{{< fairpay-screen src="images/projects/fairpay-payments-v815.webp" alt="FairPay Payments real screen showing draft blocking pending financial and acceptance review" title="03 · Payments." caption="Unresolved credits and acceptance evidence block drafting. No PayPal invoice was created in this example." zoom="Enlarge screenshot" >}}
</div>

<div class="fairpay-action-links"><a href="https://www.youtube.com/watch?v=pivk3KyXpEQ" target="_blank" rel="noopener noreferrer">Watch the 3-minute demo ↗</a><a href="https://github.com/tai-tai-12/fairpay-ai" target="_blank" rel="noopener noreferrer">GitHub repository ↗</a><a href="https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/PRODUCT_TOUR.md" target="_blank" rel="noopener noreferrer">Product tour &amp; screenshots ↗</a></div>

<span id="evidence"></span>
## What was tested — and what was not

The public release documents **161 focused checks passing in a local run on November 4, 2026**. They covered current regression checks, synthetic evaluation cases, isolated HTTP checks, and frozen adversarial cases. This does **not** mean every historical test passed: the project's validation document preserves older failures and an incomplete external verification step.

The recorded demo also shows a **separate existing $400 PayPal Sandbox DRAFT** from another fictional scenario. It was not sent or paid, and its manually recorded credit was not bank-verified.

**Scope and limitations:** FairPay runs locally, uses synthetic data, requires separately configured local AI for extraction, and can work with PayPal Sandbox credentials for authorized draft testing. It has no production authentication, real customer payments, verified bank settlement, or public hosted payment service. The $50/$500 correction, blocked billing decision, and separate $400 Sandbox draft are **different scenarios**.

<div class="fairpay-action-links fairpay-subtle-links"><a href="https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/VALIDATION.md" target="_blank" rel="noopener noreferrer">Validation and limitations ↗</a><a href="https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/DEVELOPER_GUIDE.md" target="_blank" rel="noopener noreferrer">Reproduce locally ↗</a></div>

<span id="takeaway"></span>
## Takeaway

FairPay demonstrates **AI product judgment beyond model output**: source traceability, distinct financial rules, and explicit human control over higher-stakes actions. It expands my product work beyond healthcare while remaining a synthetic-data hackathon prototype, not a claim of production use.

<div class="case-capabilities-v523"><span class="case-capabilities-label-v523">CAPABILITIES DEMONSTRATED</span><div class="case-capabilities-chips-v523"><span>AI Product Design</span><span>Problem Framing</span><span>Financial Workflow Design</span><span>Evidence Review</span><span>Human-in-the-Loop Controls</span><span>Prototype QA</span></div></div>
