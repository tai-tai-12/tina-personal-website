---
title: Building and Validating Lesion-Wise Clinical AI
translationKey: clinical-ai-at-scale
tags:
- Machine Learning
- Analytics
- Medical Imaging
- Experimentation
category: CLINICAL AI · ML
summary: Built and evaluated lesion-wise clinical AI across development and independent
  multi-center clinical cohorts.
proof:
- 12.1K development exams
- 264 independent test exams
visual: clinical-ai-visual
weight: 2
heroBackground: images/projects/work-clinical-ai-v519.webp
detailHero: images/projects/detail-v521/clinical-hero-v521.webp
heroSize: standard
detailHeroAlt: Clinical AI dashboard showing lesion-wise brain MRI analysis
heroDek: Evaluating lesion-wise brain MRI AI across multi-center data, practical failure
  modes, and the trade-off between sensitivity and review burden.
heroStats:
- value: '264'
  label: Independent test exams
- value: '0.21'
  label: False positives / scan
- value: 90.16%
  label: 5-class accuracy
snapshot:
- title: Challenge
  body: A single headline metric could not capture lesion detection quality or downstream
    review burden.
- title: My role
  body: Model development, evaluation design, error analysis, and technical communication.
- title: Scope
  body: 12,125 development exams plus a 264-exam independent multi-center clinical
    test.
- title: Outcome
  body: A lesion-wise evaluation framework balancing sensitivity, precision, FP/scan,
    and retained-lesion typing.
relatedPrevTitle: From Medical AI Research to a Deployable Product
relatedPrevURL: work/medical-ai-product/
relatedNextTitle: Third-Party Testing & Validation Operations
relatedNextURL: work/structured-validation/
navItems:
- id: problem
  label: 01 Evaluation Problem
- id: role
  label: 02 Role & Scope
- id: evaluation
  label: 03 Performance
- id: engineering
  label: 04 Engineering
- id: takeaway
  label: 05 Takeaway
---


<span id="problem"></span>
## Accuracy alone does not describe clinical review quality

Medical-imaging models need more than a single headline metric. Performance has to be evaluated across clinically meaningful tasks, independent data, practical failure modes, and the trade-off between missed lesions and false-positive review burden.

<span id="role"></span>
## My role and study scope

As a research assistant and project lead, I led brain-imaging model development and evaluation, handled clinical datasets, investigated error modes, and translated technical results for clinical and international audiences.

<div class="case-proof-grid technical-scope-grid">
  <div class="case-proof"><strong>12,125</strong><span>Development MRI exams</span><small>23,341 annotated tumor lesions</small></div>
  <div class="case-proof"><strong>264</strong><span>Independent test exams</span><small>132 positive · 132 negative</small></div>
  <div class="case-proof"><strong>2</strong><span>Medical centers</span><small>Taipei VGH · Taichung VGH</small></div>
</div>

The development cohort supported model development, internal validation, and operating-point characterization. The **264-case independent clinical test cohort** was reserved for final end-to-end evaluation.

<figure class="case-visual case-visual-vector">
  {{< site-img src="images/projects/detail-v521/clinical-cascade-v521.webp" alt="Three-stage lesion-wise AI cascade used for candidate generation, false-positive reduction, and retained-lesion tumor typing" >}}
  <figcaption><strong>Evaluation framework.</strong> Stage 0 creates a sensitivity-oriented candidate pool, Stage 1 removes obvious false positives, and Stage 2 models residual false positives while typing retained lesions.</figcaption>
</figure>

<span id="evaluation"></span>
## Measuring more than headline accuracy

The evaluation deliberately separated development and independent clinical testing, paired lesion-wise sensitivity with FP/scan and precision, examined deleted true positives and residual false positives, and reported tumor typing only on retained true-positive lesions.

<div class="case-metrics case-metrics-v524">
  <div class="case-metric"><strong>80.97%</strong><span>Lesion-wise sensitivity</span><small>Independent test cohort</small></div>
  <div class="case-metric"><strong>0.21</strong><span>False positives / scan</span><small>After the full cascade</small></div>
  <div class="case-metric"><strong>76.89%</strong><span>Lesion-wise precision</span><small>Final cascade output</small></div>
  <div class="case-metric"><strong>90.16%</strong><span>Five-class accuracy</span><small>Retained true-positive lesions</small></div>
</div>

<figure class="case-visual-v521 case-visual-full-v521">
  {{< site-img src="images/projects/detail-v521/clinical-evaluation-v521.webp" alt="Conceptual lesion-wise model evaluation and filtering workflow for brain MRI" >}}
  <figcaption><strong>Conceptual evaluation view.</strong> Candidate filtering, lesion-level classification, and performance evaluation—not a literal screenshot of the research pipeline.</figcaption>
</figure>

<span id="engineering"></span>
## Research engineering and communication

The final cascade was only one layer of the work. Reproducible evaluation also depended on imaging preprocessing, ground-truth management, experimentation, and clear communication of study scope.

<div class="case-tooling-grid-v524">
  <article><span>IMAGING PIPELINE</span><p>ANTs · SimpleITK · NiBabel · 3D Slicer</p></article>
  <article><span>MODELING</span><p>PyTorch · MONAI · nnU-Net · scikit-learn</p></article>
  <article><span>EVALUATION & DATA</span><p>Python · pandas · NumPy · statistical analysis</p></article>
</div>

Supporting work included **MRI registration with ANTs, hospital-data standardization and format conversion, ground-truth consensus management, and radiomics / segmentation / classification experiments**. Related study versions were presented at **MIDL 2026** and **AMLDS 2026**; the headline metrics on this page follow the final master's-thesis independent-cohort evaluation.

<span id="takeaway"></span>
## Takeaway

Technical credibility comes from more than model accuracy. It requires clean data scopes, denominator-aware metrics, explicit failure analysis, and disciplined communication about what the evidence does—and does not—show.

<div class="case-capabilities-v523">
  <span class="case-capabilities-label-v523">CAPABILITIES DEMONSTRATED</span>
  <div class="case-capabilities-chips-v523"><span>Machine Learning</span><span>Medical Imaging</span><span>Model Evaluation</span><span>Error Analysis</span><span>Research Communication</span></div>
</div>
