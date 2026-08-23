---
title: "大規模臨床 AI 的建立與驗證"
translationKey: "clinical-ai-at-scale"
tags: ["Machine Learning", "Analytics", "Medical Imaging", "Experimentation"]
category: "臨床 AI · ML"
summary: "以嚴謹的 development／independent test 分離建立與驗證逐病灶臨床 AI。"
proof: ["12.1K development exams", "264 independent test exams"]
visual: "clinical-ai-visual"
weight: 2
---

這個案例聚焦我的分析與技術能力：如何在真實世界醫學影像資料中建立、評估並溝通模型效能。

## 挑戰

醫學影像模型不能只看單一 headline metric。需要在具臨床意義的任務、獨立資料、failure modes，以及漏診與偽陽性檢閱負擔的 trade-off 下評估系統。

## 我的角色

作為 Research Assistant / Project Lead，我負責腦部影像模型的開發與評估工作、臨床資料處理、錯誤模式分析，以及將技術結果向臨床與國際 audience 溝通。

## 研究資料範圍

<div class="case-proof-grid technical-scope-grid">
  <div class="case-proof"><strong>12,125</strong><span>開發 MRI examinations</span><small>23,341 個標註腫瘤病灶</small></div>
  <div class="case-proof"><strong>264</strong><span>獨立測試 examinations</span><small>132 positive + 132 negative</small></div>
  <div class="case-proof"><strong>2</strong><span>家醫學中心</span><small>台北榮總 + 台中榮總</small></div>
</div>

Development cohort 用於模型開發、內部驗證與 operating-point characterization；**264-case independent clinical test cohort** 則保留給最終 end-to-end evaluation。

<figure class="case-visual case-visual-vector">
  {{< site-img src="images/projects/medical-ai-product/three-stage-ai-cascade.svg" alt="候選生成、偽陽性降低與保留病灶腫瘤分類的三階段 AI 串聯流程" >}}
  <figcaption>最終碩論的評估架構：Stage 0 建立敏感度導向候選池，Stage 1 去除明顯偽陽性，Stage 2 處理殘餘偽陽性並對保留病灶進行分類。</figcaption>
</figure>

## 評估方法

- 明確區分 **development** 與 **independent clinical test** 資料範圍。
- 將病灶層級 sensitivity 與 FP/scan、precision 一起解讀，而非只看單一指標。
- 分析被刪除的 true positives、殘餘 false positives、病灶大小、腫瘤類型與 operating-point trade-offs。
- Tumor typing 僅針對經評估流程後保留下來的 true-positive lesions 計算。
- 將結論限制在 retrospective technical evidence，不將結果誇大為 prospective workflow benefit。

<div class="case-metrics">
  <div class="case-metric"><strong>80.97%</strong><span>獨立測試 cohort 的病灶層級 sensitivity</span></div>
  <div class="case-metric"><strong>0.21</strong><span>full cascade 後的 false positives per scan</span></div>
  <div class="case-metric"><strong>76.89%</strong><span>最終病灶層級 precision</span></div>
  <div class="case-metric"><strong>90.16%</strong><span>保留 true-positive lesions 的五分類 accuracy</span></div>
</div>

## 技術深度

架構使用 T1C 與 T2 MRI、敏感度導向的 **3D nnU-Net v2** proposal stage、lesion-centered downstream patches，以及 mask-gated classification models 進行偽陽性降低與保留病灶分類。我的 broader toolkit 包括 Python、pandas、NumPy、scikit-learn、XGBoost、PyTorch、TensorFlow/Keras、MONAI、SimpleITK、NiBabel、3D Slicer、Git、BigQuery 與 MLflow。

## 研究溝通

相關研究成果於 **MIDL 2026** 與 **IEEE AMLDS 2026** 發表。這些 conference artifacts 對應相關研究版本；本頁 headline metrics 統一採用最終碩論的 independent-cohort evaluation，避免混用不同 study versions。

## 我學到的事

Technical credibility 不只來自模型 accuracy，而來自清楚的 data scope、denominator-aware metrics、明確的 failure analysis，以及對 evidence 能夠支持與不能支持什麼保持紀律。

## Skills

Machine learning · Medical imaging · Python · Model evaluation · Error analysis · Research communication
