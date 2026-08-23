---
title: "From Medical AI Research to a Deployable Product"
translationKey: "medical-ai-product"
tags: ["Product Management", "Healthcare AI", "Regulatory", "Cross-functional Leadership"]
---

I helped translate brain-tumor MRI research into a workflow designed for real clinical use, while coordinating the product, validation, and regulatory work needed to move toward deployment.

<figure class="case-visual">
  {{< site-img src="images/projects/medical-ai-product/clinical-product-workflow.webp" alt="Conceptual clinical product workflow from PACS case list through AI-assisted MRI review and physician review" >}}
  <figcaption>Public-safe conceptual workflow redrawn from product documentation: case access → AI status → MRI review → lesion overlay → lesion analysis → report → physician review.</figcaption>
</figure>

## The challenge

A strong model is not yet a deployable product. A clinically useful system has to fit the radiologist's review workflow, surface AI results in an interpretable way, support validation, and generate evidence that technical, clinical, and regulatory stakeholders can trust.

## My role

I worked across **product management, project leadership, clinical translation, and regulatory execution**. My responsibilities included aligning physicians, engineers, executives, and regulatory stakeholders; organizing validation priorities; supporting TFDA submission work; and improving submission-document management.

## Approach

1. Translate clinical workflow needs into product scope and validation priorities.
2. Connect model performance with the evidence needed for hospital and regulatory review.
3. Coordinate stakeholders across technical, clinical, business, and regulatory functions.
4. Build repeatable documentation and tracking processes so decisions and versions remained clear.

## Product + technical decisions

The underlying research used a lesion-wise cascade rather than treating detection as a single end point. A sensitivity-oriented proposal stage generated a broad candidate pool, a downstream classifier suppressed false positives, and the final stage assigned retained lesions to one of five tumor subtypes.

<figure class="case-visual">
  {{< site-img src="images/projects/medical-ai-product/three-stage-ai-cascade.webp" alt="Three-stage lesion-wise AI cascade for candidate generation, false-positive reduction, and final lesion classification" >}}
  <figcaption>Research architecture simplified for portfolio use. The cascade prioritizes sensitivity first, then reduces false positives and performs lesion-level tumor typing.</figcaption>
</figure>

<div class="case-metrics">
  <div class="case-metric"><strong>90.13%</strong><span>final lesion-wise sensitivity</span></div>
  <div class="case-metric"><strong>0.41</strong><span>false positives per scan</span></div>
  <div class="case-metric"><strong>73.2%</strong><span>FP/scan reduction vs. raw candidates</span></div>
  <div class="case-metric"><strong>89.55%</strong><span>five-class accuracy on retained lesions</span></div>
</div>

## From evidence to product workflow

The product layer extended beyond the model itself. The clinical workflow included PACS-connected case access, AI processing-state review, image viewing, AI-assisted lesion overlays, lesion-level analysis, and report review before physician judgment. The system was designed as **assistive decision support**, with the clinician retaining final interpretation.

<div class="case-evidence-card">
  {{< site-img src="images/research/midl-poster.webp" alt="Tina Tai standing beside her MIDL 2026 poster on lesion-wise brain tumor AI" >}}
  <div>
    <h3>Research translated into external evidence</h3>
    <p>The lesion-wise cascade was presented at MIDL 2026, providing a public research artifact behind the technical evidence used in this product story.</p>
  </div>
</div>

## Results & impact

- Supported a clinical AI workflow spanning **two medical centers**.
- Led product work through **TFDA submission**, supporting commercialization and hospital deployment readiness.
- Coordinated physicians, engineers, executives, and regulatory stakeholders around product scope, validation priorities, and timelines.
- Supported **2024 Taiwan Medical Informatics Connectathon Level I** capability-statement validation for medical imaging workflows.
- Consolidated fragmented TFDA records into a cloud-based tracker to improve retrieval and version control.

## What I learned

The hardest part of AI product work is often not the model itself. It is creating alignment between what the technology can do, what users actually need, what evidence reviewers require, and what an organization can operationalize.

## Skills

Product management · Stakeholder alignment · Clinical AI · Regulatory execution · Validation strategy · Process design
