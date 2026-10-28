---
title: Shipping Medical AI Under Real Clinical Constraints
translationKey: medical-ai-product
tags:
- Product Management
- Healthcare AI
- Regulatory
- Cross-functional Leadership
category: PRODUCT MANAGEMENT · AI
summary: Worked with physicians and engineers to make brain MRI AI faster and easier to use, while managing release and medical-device submission decisions.
proof:
- ~67% less AI processing time
- 2 medical centers
- 5 physician users
displayMetrics:
- value: "~67%"
  label: "Faster processing"
- value: "5"
  label: "Physician users"
- value: "2"
  label: "Medical centers"
visual: product-visual
weight: 1
heroBackground: images/projects/work-product-v519.webp
detailHero: images/projects/detail-v521/product-hero-v521.webp
heroSize: compact
detailHeroAlt: Clinical AI product workflow at a brain MRI review workstation
heroDek: Helped turn brain MRI AI into medical-device software that physicians could review and use, improving speed and coordinating a Taiwan FDA submission timeline.
heroStats:
- value: ~67%
  label: Less AI processing time
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
  body: Five physician users at two medical centers, plus weekly coordination across 12 AI/ML, software/UI, clinical, regulatory, and leadership stakeholders.
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
## A technically strong model still had to work for physicians

A research model is not yet a usable product. The physicians I worked with needed faster answers, a visible processing status, and a manageable number of incorrect tumor alerts. As Product Manager, I turned these needs into priorities and worked with engineers and regulatory colleagues on delivery. **Nearly two minutes of processing felt too slow in workflow, users could not tell how long processing would continue, and different clinical contexts valued sensitivity and false-positive burden differently.** At the same time, every model change carried validation, documentation, and regulatory consequences.

<span id="role"></span>
## Three product decisions that changed the path

<div class="product-decision-list-v6">
  <article><span>01 · USABILITY VS. MODEL PERFORMANCE</span><h3>Optimize for the workflow, not the academically best model</h3><p>I led recurring workflow testing with physicians and translated feedback into an initial sub-one-minute latency target. Working with engineers, we accepted a small sensitivity trade-off discussed with clinical users and reduced end-to-end processing from roughly two minutes to about forty seconds. When physicians said the system still <em>felt</em> slow because they could not tell how much longer it would run, I proposed a percentage progress indicator based on physician feedback, which was subsequently deployed in the product.</p></article>
  <article><span>02 · ONE MODEL, DIFFERENT WORKFLOWS</span><h3>Turn model metrics into operating-point decisions</h3><p>I translated sensitivity and false-positive burden into what physicians would experience during review, then used product trials and competitor benchmarks to define institution-level thresholds. The work showed that higher-sensitivity clinical review workflows could prioritize sensitivity, while other medical-center workflows could use a more balanced operating point.</p></article>
  <article><span>03 · BETTER MODEL VS. SHIPPING ON TIME</span><h3>Sequence the upgrade instead of destabilizing the release</h3><p>When a materially improved model arrived late in the submission cycle, I assessed downstream revalidation and documentation work—not just engineering time—and estimated roughly three to six months of additional impact. I recommended keeping the already validated version for the current release and sequencing the new model into the next cycle. Leadership adopted the plan, and the team maintained the June TFDA submission timeline.</p></article>
</div>

[AITEWAN company website ↗](https://www.aitewan-bio.com/en/)

<span id="workflow"></span>
## From research model to physician workflow

The AI evaluated potential tumors in stages: first generating likely locations, then filtering mistaken alerts and classifying remaining findings. A sensitivity-oriented proposal stage generated candidates, a downstream classifier suppressed false positives, and the final stage typed retained lesions. The detailed technical evaluation is covered separately in **Designing AI Evaluation Beyond Accuracy**.

The product layer extended beyond the model itself. It included **PACS-connected case access, processing-state visibility, AI-assisted lesion overlays, lesion-level review, and physician confirmation before LLM-assisted report drafting and final clinician oversight**. Repeated physician discovery across two centers turned technical performance into concrete requirements for speed, visibility, operating point, and release scope.

<figure class="case-visual-v521 case-visual-full-v521">
  {{< site-img src="images/projects/detail-v521/product-deployment-v521.webp" alt="Conceptual illustration of secure medical-AI deployment, data flow, and governance" >}}
  <figcaption><strong>Conceptual product workflow.</strong> Connected data, AI-assisted review, documentation, and governed clinical use—not a literal product screenshot.</figcaption>
</figure>

<div class="product-flow-v81" role="group" aria-label="Team platform capability: three phases of physician-centered medical AI workflow">
  <div class="product-flow-eyebrow-v81">TEAM PLATFORM CAPABILITY · PUBLISHED PRODUCT SCOPE</div>
  <ol class="product-flow-steps-v81 product-flow-phases-v82">
    <li><span>01 · CLINICAL INTEGRATION</span><strong>DICOM / PACS</strong><p>Connect the imaging workflow and retrieve appropriate T1C or T1C + T2 MRI studies.</p></li>
    <li><span>02 · AI-ASSISTED REVIEW</span><strong>Lesion analysis &amp; physician confirmation</strong><p>Detect, segment, measure, localize and classify candidate lesions for clinician review and confirmation.</p></li>
    <li><span>03 · REPORT &amp; GOVERNANCE</span><strong>Physician-confirmed LLM draft</strong><p>Generate a draft report from confirmed findings, with final review by a clinician—not autonomous diagnosis.</p></li>
  </ol>
  <div class="product-flow-attribution-v81"><div><span>TEAM PRODUCT SCOPE</span><p>Capabilities described in the <a href="https://www.futuretech.org.tw/futuretech/index.php?action=product_detail&prod_no=P0008700008523&web_lang=en-us" target="_blank" rel="noopener noreferrer">official DeepBT A+ profile ↗</a>; this is a schematic, not a product screenshot or claim that I implemented each subsystem.</p></div><div><span>MY CONTRIBUTION</span><p>Physician discovery, requirements, progress-state usability, institution-level operating points, cross-functional release planning and regulatory coordination.</p></div></div>
</div>

<div class="case-boundary-v81"><strong>Evidence boundary</strong><p>The research metrics below describe retrospective model evaluation, while physician workflow testing, interoperability work, and TFDA submission coordination describe product execution. They are different evidence types; no reader-study efficiency gain, prospective outcome improvement, regulatory clearance, or autonomous diagnosis is claimed.</p></div>

<span id="evidence"></span>
## Product validation, research evidence, and recognition

The product pathway grew from the same lesion-wise brain-tumor AI research program communicated through complementary public outputs.

<div class="case-award-v8" aria-label="Project recognition">
  <div class="case-award-emblem-v8" aria-hidden="true"><span>2026</span><strong>FT</strong></div>
  <div class="case-award-copy-v8">
    <span>TEAM / PROJECT RECOGNITION · 2026</span>
    <h3>DeepBT A+ · Future Tech Award</h3>
    <p>I contributed to <strong>DeepBT A+</strong>, the NYCU-led intelligent brain-tumor MRI reading assistance project recognized with the <strong>2026 Future Tech Award</strong>. The honor belongs to the project team; my work centered on physician-facing product decisions, execution, and clinical/regulatory coordination.</p>
  </div>
  <p class="case-award-source-v81"><a href="https://www.futuretech.org.tw/futuretech/index.php?action=product_detail&prod_no=P0008700008523&web_lang=en-us" target="_blank" rel="noopener noreferrer">Official FUTEX / Future Tech project profile ↗</a> <span>· External verification · No award photo displayed</span></p>
</div>

<div class="case-evidence-grid">
  <article class="case-evidence-card">
    {{< site-img src="images/research/midl-poster.webp" alt="Tina Tai standing beside her MIDL 2026 poster on lesion-wise brain tumor AI" >}}
    <div><span>MIDL · 2026</span><h3>First-Author Short Paper Poster</h3><p>Public research artifact on lesion-wise false-positive reduction and five-class tumor typing.</p></div>
  </article>
  <article class="case-evidence-card">
    {{< site-img src="images/research/amlds-talk.webp" alt="Tina Tai giving an oral presentation at AMLDS 2026" >}}
    <div><span>AMLDS · 2026</span><h3>First-Author Oral Presentation</h3><p>A related extension on candidate verification and false-positive reduction, published in the <a href="https://ieeexplore.ieee.org/xpl/conhome/11723344/proceeding" target="_blank" rel="noopener noreferrer">IEEE Xplore conference proceedings</a>; recognized with an Outstanding Oral Presentation award.</p></div>
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
