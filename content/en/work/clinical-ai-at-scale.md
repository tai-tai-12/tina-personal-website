---
title: "Building and Validating Clinical AI at Scale"
translationKey: "clinical-ai-at-scale"
tags: ["Machine Learning", "Analytics", "Medical Imaging", "Experimentation"]
---

This case study focuses on the analytical and technical side of my clinical-AI work: building, evaluating, and communicating model performance across real-world medical imaging datasets.

## The challenge

Medical imaging models need more than a single headline metric. Performance must be evaluated across clinically meaningful tasks, independent data, practical failure modes, and the trade-off between missed lesions and false-positive review burden.

## My role

As a research assistant and project lead, I led brain-imaging model development and evaluation work, handled clinical datasets, investigated error modes, and translated technical results for clinical and international audiences.

## Study scope

<div class="case-proof-grid technical-scope-grid">
  <div class="case-proof"><strong>12,125</strong><span>development MRI exams</span><small>23,341 annotated tumor lesions</small></div>
  <div class="case-proof"><strong>264</strong><span>independent test exams</span><small>132 positive + 132 negative</small></div>
  <div class="case-proof"><strong>2</strong><span>medical centers</span><small>Taipei VGH + Taichung VGH</small></div>
</div>

The development cohort was used for model development, internal validation, and operating-point characterization. The **264-case independent clinical test cohort** was reserved for final end-to-end evaluation.

<figure class="case-visual case-visual-vector">
  {{< site-img src="images/projects/medical-ai-product/three-stage-ai-cascade.svg" alt="Three-stage lesion-wise AI cascade used for candidate generation, false-positive reduction, and retained-lesion tumor typing" >}}
  <figcaption>Final-thesis evaluation framework: Stage 0 generates a sensitivity-oriented candidate pool, Stage 1 removes obvious false positives, and Stage 2 models residual false positives while typing retained lesions.</figcaption>
</figure>

## Evaluation approach

- Separate **development** and **independent clinical test** data scopes.
- Evaluate lesion-wise sensitivity together with FP/scan and precision rather than relying on a single metric.
- Analyze deleted true positives, residual false positives, lesion size, tumor class, and operating-point trade-offs.
- Report tumor typing only on true-positive lesions retained by the evaluated cascade.
- Keep the interpretation bounded to retrospective technical evidence rather than claiming prospective workflow benefit.

<div class="case-metrics">
  <div class="case-metric"><strong>80.97%</strong><span>lesion-wise sensitivity on the independent test cohort</span></div>
  <div class="case-metric"><strong>0.21</strong><span>false positives per scan after the full cascade</span></div>
  <div class="case-metric"><strong>76.89%</strong><span>final lesion-wise precision</span></div>
  <div class="case-metric"><strong>90.16%</strong><span>five-class accuracy on retained true-positive lesions</span></div>
</div>

## Technical depth

The framework used T1C and T2 MRI, a sensitivity-oriented **3D nnU-Net v2** proposal stage, lesion-centered downstream patches, and mask-gated classification models for false-positive reduction and retained-lesion tumor typing. My broader toolkit includes Python, pandas, NumPy, scikit-learn, XGBoost, PyTorch, TensorFlow/Keras, MONAI, SimpleITK, NiBabel, 3D Slicer, Git, BigQuery, and MLflow.

## Research communication

This work contributed to research presented at **MIDL 2026** and **IEEE AMLDS 2026**. Those conference artifacts represent related study versions and are presented as research outputs; the metrics above follow the final master's-thesis independent-cohort evaluation.

## What I learned

Technical credibility comes from more than model accuracy. It requires clean data scopes, denominator-aware metrics, explicit failure analysis, and disciplined communication about what the evidence does—and does not—show.

## Skills

Machine learning · Medical imaging · Python · Model evaluation · Error analysis · Research communication
