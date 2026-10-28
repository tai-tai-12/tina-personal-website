---
title: Designing AI Evaluation Beyond Accuracy
translationKey: clinical-ai-at-scale
tags:
- Machine Learning
- Analytics
- Medical Imaging
- Experimentation
category: AI EVALUATION · ML
summary: Evaluated how to cut false MRI tumor alerts while tracking missed lesions, using independent test data rather than relying on headline accuracy.
proof:
- 94.5% fewer FP candidates
- 264 independent MRI cases
- 90.16% 5-class accuracy
displayMetrics:
- value: "94.5%"
  label: "Fewer false alarms"
- value: "264"
  label: "Independent MRI cases"
- value: "90.16%"
  label: "Tumor-type accuracy on detected lesions"
visual: clinical-ai-visual
weight: 2
heroBackground: images/projects/work-clinical-ai-v519.webp
detailHero: images/projects/detail-v521/clinical-hero-v521.webp
heroSize: standard
detailHeroAlt: Clinical AI dashboard showing lesion-wise brain MRI analysis
heroDek: Reduced false tumor alerts on brain MRI while measuring the trade-off in real lesions detected, using independent multi-center test data.
heroStats:
- value: '264'
  label: Independent test exams
- value: '0.21'
  label: False positives / scan
- value: 90.16%
  label: 5-class accuracy
snapshot:
- title: Challenge
  body: An AI scan can flag too many areas as tumors, slowing clinical review; reducing false alarms must be measured alongside missed tumors.
- title: My role
  body: Model development, evaluation design, error analysis, and technical communication.
- title: Scope
  body: 12,125 development exams plus a balanced independent multi-center clinical
    test cohort.
- title: Outcome
  body: A lesion-wise evaluation framework balancing sensitivity, precision, FP/scan,
    and retained-lesion typing.
relatedPrevTitle: Shipping Medical AI Under Real Clinical Constraints
relatedPrevURL: work/medical-ai-product/
relatedNextTitle: Running Client-Facing Validation Operations
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
## Fewer false alarms—without ignoring what gets missed

A brain MRI AI system can mistakenly flag healthy areas as possible tumors. Those false alarms add work for clinicians. I helped evaluate a multi-stage approach that reduced false-positive candidates by **94.54% (1,007 to 55)** across **264 independently tested MRI exams**. The trade-off mattered: the proportion of real lesions detected declined from **84.96% to 80.97%**. This was a retrospective research evaluation, not evidence that clinicians read scans faster in routine practice.

<span id="role"></span>
## My role and study scope

As a research assistant and project lead, I led brain-imaging model development and evaluation, handled clinical datasets, investigated error modes, and translated technical results for clinical and international audiences.

<div class="case-proof-grid technical-scope-grid">
  <div class="case-proof"><strong>12,125</strong><span>Development MRI exams</span><small>23,341 annotated tumor lesions</small></div>
  <div class="case-proof"><strong>132 / 132</strong><span>Positive / negative exams</span><small>Balanced independent cohort</small></div>
  <div class="case-proof"><strong>2</strong><span>Medical centers</span><small>Taipei VGH · Taichung VGH</small></div>
</div>

The development cohort supported model development, internal validation, and operating-point characterization. The **independent clinical test cohort** was reserved for final end-to-end evaluation.

<figure class="case-visual case-visual-vector">
  {{< site-img src="images/projects/detail-v521/clinical-cascade-v521.webp" alt="Three-stage lesion-wise AI cascade used for candidate generation, false-positive reduction, and retained-lesion tumor typing" >}}
  <figcaption><strong>Evaluation framework.</strong> Stage 0 creates a sensitivity-oriented candidate pool, Stage 1 removes obvious false positives, and Stage 2 models residual false positives while typing retained lesions.</figcaption>
</figure>

<span id="evaluation"></span>
## Measuring more than headline accuracy

The evaluation deliberately separated development and independent clinical testing, paired lesion-wise sensitivity with FP/scan and precision, examined deleted true positives and residual false positives, and reported tumor typing only on retained true-positive lesions.

<div class="case-metrics case-metrics-v524">
  <div class="case-metric"><strong>80.97%&nbsp;</strong><span>Lesion-wise sensitivity</span><small>Independent test cohort</small></div>
  <div class="case-metric"><strong>0.21&nbsp;</strong><span>False positives / scan</span><small>After the full cascade</small></div>
  <div class="case-metric"><strong>76.89%&nbsp;</strong><span>Lesion-wise precision</span><small>Final cascade output</small></div>
  <div class="case-metric"><strong>90.16%&nbsp;</strong><span>Five-class accuracy</span><small>Retained true-positive lesions</small></div>
</div>

<p class="clinical-key-outcome-v82"><strong>1,007 → 55 false-positive candidates (−94.54%).</strong> The reduction in review burden came with a measured reduction in lesion-wise sensitivity; the two outcomes are presented together below.</p>

<section class="clinical-tradeoff-v81" aria-labelledby="tradeoff-title-v81">
  <div class="clinical-tradeoff-heading-v81"><span>THE TRADE-OFF · SAME 264-EXAM RETROSPECTIVE COHORT</span><h3 id="tradeoff-title-v81">Fewer false alarms came with a measured sensitivity cost.</h3><p>Compared with the Stage-0 proposal pool, the full cascade greatly reduced false-positive review burden while losing nine additionally detected true-positive lesions. Both sides of the trade-off belong in the evaluation.</p></div>
  <div class="clinical-tradeoff-pair-v81"><div><span>FALSE POSITIVES / SCAN</span><div class="tradeoff-comparison-v81"><span class="tradeoff-value-v81">Stage 0 <strong>3.81</strong></span><div class="tradeoff-line-v81"><i style="width:100%"></i></div><span class="tradeoff-value-v81">Full cascade <strong>0.21</strong></span><div class="tradeoff-line-v81"><i style="width:5.51%"></i></div></div><b>−94.54% false-positive candidates</b></div><div><span>LESION-WISE SENSITIVITY</span><div class="tradeoff-comparison-v81"><span class="tradeoff-value-v81">Stage 0 <strong>84.96%</strong></span><div class="tradeoff-line-v81"><i style="width:84.96%"></i></div><span class="tradeoff-value-v81">Full cascade <strong>80.97%</strong></span><div class="tradeoff-line-v81"><i style="width:80.97%"></i></div></div><b>−3.99 percentage points</b></div></div>
  <p class="clinical-tradeoff-source-v81">Source: final master's thesis, 264 retrospectively evaluated MRI exams (226 reference lesions); research evaluation, not a prospective clinical effectiveness study. Final precision was 76.89% vs. 16.01% at Stage 0.</p>
</section>

<span id="engineering"></span>
## From clinical insight to technical design

The final cascade was only one layer of the work. Reproducible evaluation also depended on imaging preprocessing, ground-truth management, experimentation, and clear communication of study scope.

<div class="clinical-insight-v6"><span>CLINICAL INSIGHT → TECHNICAL DESIGN</span><h3>Use domain knowledge to diagnose model failure—not only architecture changes</h3><p>When glioma and metastasis remained difficult to distinguish, I returned to the MRI itself, used my radiologic training to identify clinically visible patterns, consulted physicians, and translated those observations into model and augmentation experiments. It became a practical example of using clinical reasoning to guide technical design.</p></div>

The reasoning came first; the tooling supported it.

<div class="clinical-evidence-notes-v81"><article><span>GROUND-TRUTH QUALITY</span><h3>Expert agreement before consensus</h3><p>Fleiss’ κ was <strong>0.9416</strong> for tumor type and <strong>0.9514</strong> for intra-/extra-axial annotation; mean segmentation Dice was <strong>0.8864</strong>. These measure annotation consistency, not model accuracy.</p></article><article><span>REDUCED-SEQUENCE EXPLORATION</span><h3>T1C-only vs. T1C + T2</h3><p>In a secondary configuration analysis, T1C-only achieved <strong>73.89% sensitivity</strong>, <strong>0.09 FP/scan</strong> and <strong>88.62% five-class accuracy</strong> among retained true positives, versus <strong>80.97%</strong>, <strong>0.21</strong> and <strong>90.16%</strong> for the primary T1C+T2 system. Different lesions were retained, so typing accuracy is conditional and not a head-to-head comparison on identical detections.</p></article></div>

<details class="technical-details-v62">
  <summary>Technical details</summary>
  <div class="case-tooling-grid-v524">
    <article><span>IMAGING PIPELINE</span><p>ANTs · SimpleITK · NiBabel · 3D Slicer</p></article>
    <article><span>MODELING</span><p>PyTorch · MONAI · nnU-Net · scikit-learn</p></article>
    <article><span>EVALUATION & DATA</span><p>Python · pandas · NumPy · statistical analysis</p></article>
  </div>
  <p>Supporting work included MRI registration, hospital-data standardization / format conversion, ground-truth consensus management, and radiomics / segmentation / classification experiments.</p>
</details>

Related study versions were presented at **MIDL 2026** and **AMLDS 2026**. The AMLDS 2026 paper is now included in the [IEEE Xplore conference proceedings](https://ieeexplore.ieee.org/xpl/conhome/11723344/proceeding); the headline metrics on this page intentionally follow the final master's-thesis independent-cohort evaluation, not the AMLDS paper's separate evaluation.

<div class="case-boundary-v81"><strong>What these data cannot establish</strong><p>This was a retrospective, two-center independent test—not a prospective reader study or evidence of faster clinician reading, lower alert fatigue in real practice, autonomous diagnosis, or improved patient outcomes. Public MIDL 2026 results use a <em>different</em> 249-exam held-out cohort; their 90.13% sensitivity and 0.41 FP/scan should not be combined with this thesis cohort's 264-exam endpoints.</p></div>

<span id="takeaway"></span>
## Takeaway

Technical credibility comes from more than model accuracy. It requires clean data scopes, denominator-aware metrics, explicit failure analysis, and disciplined communication about what the evidence does—and does not—show.

<div class="case-capabilities-v523">
  <span class="case-capabilities-label-v523">CAPABILITIES DEMONSTRATED</span>
  <div class="case-capabilities-chips-v523"><span>Machine Learning</span><span>Medical Imaging</span><span>Model Evaluation</span><span>Error Analysis</span><span>Research Communication</span></div>
</div>
