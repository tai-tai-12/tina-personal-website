---
title: Shipping Medical AI Under Real Clinical Constraints
translationKey: medical-ai-product
tags:
- Product Management
- Healthcare AI
- Regulatory
- Cross-functional Leadership
category: PRODUCT MANAGEMENT · AI
summary: Used physician discovery, technical trade-offs, and release sequencing to move brain-tumor MRI AI into real clinical workflow.
proof:
- ~67% faster AI processing
- 2 medical centers
visual: product-visual
weight: 1
heroBackground: images/projects/work-product-v519.webp
detailHero: images/projects/detail-v521/product-hero-v521.webp
heroSize: compact
detailHeroAlt: Clinical AI product workflow at a brain MRI review workstation
heroDek: Turning brain-tumor MRI research into a physician-led product through recurring user discovery, technical trade-offs, release sequencing, validation, and TFDA execution.
heroStats:
- value: ~67%
  label: Faster AI processing
- value: 5 physicians · 2 centers
  label: Recurring workflow discovery
- value: TFDA
  label: Submission execution
snapshot:
- title: Challenge
  body: A technically strong model still had to become fast, interpretable, configurable, and defensible enough for real clinical use.
- title: My role
  body: Product discovery, requirements, technical trade-off decisions, release planning, validation, and regulatory execution.
- title: Scope
  body: Five physician users across two medical centers, plus AI/ML, software/UI, clinical, regulatory, and leadership stakeholders.
- title: Outcome
  body: Faster processing, clearer user feedback, workflow-specific operating points, and a protected submission timeline.
relatedPrevTitle: Running Client-Facing Validation Operations
relatedPrevURL: work/structured-validation/
relatedNextTitle: Designing AI Evaluation Beyond Accuracy
relatedNextURL: work/clinical-ai-at-scale/
navItems:
- id: problem
  label: 01 Product Problem
- id: role
  label: 02 Product Decisions
- id: workflow
  label: 03 Workflow
- id: evidence
  label: 04 Evidence & Execution
- id: takeaway
  label: 05 Takeaway
---

<span id="problem"></span>
## A strong model still had to work for users

The research system performed well technically, but physicians exposed the product problems that model metrics alone could not solve. **Nearly two minutes of processing felt too slow in workflow, users could not tell how long processing would continue, and different clinical contexts valued sensitivity and false-positive burden differently.** At the same time, every model change carried validation, documentation, and regulatory consequences.

<span id="role"></span>
## Three product decisions that changed the path

<div class="product-decision-list-v6">
  <article><span>01 · USABILITY VS. MODEL PERFORMANCE</span><h3>Optimize for the workflow, not the academically best model</h3><p>I led recurring workflow testing with physicians and translated feedback into an initial sub-one-minute latency target. Working with engineers, we accepted a small, clinically validated sensitivity decrease and reduced end-to-end processing from roughly two minutes to about forty seconds. When physicians said the system still <em>felt</em> slow because they could not tell how much longer it would run, I proposed a percentage progress indicator based on physician feedback, which was subsequently deployed in the product.</p></article>
  <article><span>02 · ONE MODEL, DIFFERENT WORKFLOWS</span><h3>Turn model metrics into operating-point decisions</h3><p>I translated sensitivity and false-positive burden into what physicians would experience during review, then used product trials and competitor benchmarks to define institution-level thresholds. The work showed that screening-oriented settings could prioritize sensitivity, while other medical-center workflows could use a more balanced operating point.</p></article>
  <article><span>03 · BETTER MODEL VS. SHIPPING ON TIME</span><h3>Sequence the upgrade instead of destabilizing the release</h3><p>When a materially improved model arrived late in the submission cycle, I assessed downstream revalidation and documentation work—not just engineering time—and estimated roughly three to six months of additional impact. I recommended keeping the already validated version for the current release and sequencing the new model into the next cycle. Leadership adopted the plan, and the team maintained the June TFDA submission timeline.</p></article>
</div>

[AITEWAN company website ↗](https://www.aitewan-bio.com/en/)

<span id="workflow"></span>
## From research model to physician workflow

The underlying research used a lesion-wise cascade rather than treating detection as a single end point. A sensitivity-oriented proposal stage generated candidates, a downstream classifier suppressed false positives, and the final stage typed retained lesions. The detailed technical evaluation is covered separately in **Designing AI Evaluation Beyond Accuracy**.

The product layer extended beyond the model itself. It included **PACS-connected case access, processing-state visibility, AI-assisted lesion overlays, lesion-level review, and report review before physician judgment**. Repeated physician discovery across two centers turned technical performance into concrete requirements for speed, visibility, operating point, and release scope.

<figure class="case-visual-v521 case-visual-full-v521">
  {{< site-img src="images/projects/detail-v521/product-deployment-v521.webp" alt="Conceptual illustration of secure medical-AI deployment, data flow, and governance" >}}
  <figcaption><strong>Conceptual product workflow.</strong> Connected data, AI-assisted review, documentation, and governed clinical use—not a literal product screenshot.</figcaption>
</figure>

<span id="evidence"></span>
## Research evidence and execution

The product pathway grew from the same lesion-wise brain-tumor AI research program communicated through complementary public outputs.

<div class="case-evidence-grid">
  <article class="case-evidence-card">
    {{< site-img src="images/research/midl-poster.webp" alt="Tina Tai standing beside her MIDL 2026 poster on lesion-wise brain tumor AI" >}}
    <div><span>MIDL · 2026</span><h3>First-Author Short Paper Poster</h3><p>Public research artifact on lesion-wise false-positive reduction and five-class tumor typing.</p></div>
  </article>
  <article class="case-evidence-card">
    {{< site-img src="images/research/amlds-talk.webp" alt="Tina Tai giving an oral presentation at AMLDS 2026" >}}
    <div><span>AMLDS · 2026</span><h3>First-Author Oral Presentation</h3><p>A closely related extension focused on candidate verification and false-positive reduction; recognized with an Outstanding Oral Presentation award.</p></div>
  </article>
</div>

<div class="case-metrics case-metrics-v524">
  <div class="case-metric"><strong>2&nbsp;</strong><span>Medical centers</span><small>Recurring clinical workflow discovery</small></div>
  <div class="case-metric"><strong>TFDA&nbsp;</strong><span>Submission execution</span><small>Validation, documentation, and release planning</small></div>
  <div class="case-metric"><strong>Level I&nbsp;</strong><span>Connectathon validation</span><small>2024 medical-imaging workflow capability statement</small></div>
  <div class="case-metric"><strong>June&nbsp;</strong><span>Submission timeline maintained</span><small>Late model upgrade sequenced to the next cycle</small></div>
</div>

<span id="takeaway"></span>
## Takeaway

The hardest part of AI product work is often not choosing the technically strongest model. It is deciding **which trade-off creates the best product for the user, which evidence is defensible, and what the team should ship now versus sequence next**.

<div class="case-capabilities-v523">
  <span class="case-capabilities-label-v523">CAPABILITIES DEMONSTRATED</span>
  <div class="case-capabilities-chips-v523"><span>User Discovery</span><span>Product Judgment</span><span>Technical Trade-offs</span><span>Release Planning</span><span>Regulatory Execution</span></div>
</div>
