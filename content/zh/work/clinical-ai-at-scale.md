---
title: "大規模臨床 AI 的建立與驗證"
translationKey: "clinical-ai-at-scale"
tags: ["Machine Learning", "Analytics", "Medical Imaging", "Experimentation"]
category: "臨床 AI · ML"
summary: "以嚴謹的 development／independent test 分離建立與驗證逐病灶臨床 AI。"
proof: ["12.1K development exams", "264 independent test exams"]
visual: "clinical-ai-visual"
weight: 2
heroBackground: "images/projects/work-clinical-ai-v519.webp"
detailHero: "images/projects/detail-v521/clinical-hero-v521.webp"
detailHeroAlt: "Clinical AI dashboard showing lesion-wise brain MRI analysis"
heroDek: "以多中心資料、實務失敗模式與敏感度／閱片負擔取捨，評估病灶層級腦部 MRI AI。"
heroStats:
  - value: "12,125"
    label: "開發 MRI exams"
  - value: "264"
    label: "獨立測試 exams"
  - value: "0.21"
    label: "每掃描 FP"
  - value: "90.16%"
    label: "五分類準確率"
snapshot:
  - title: "挑戰"
    body: "單一 headline metric 無法完整描述病灶偵測品質與後續閱片負擔。"
  - title: "我的角色"
    body: "模型開發、評估設計、錯誤分析與技術溝通。"
  - title: "範圍"
    body: "12,125 筆開發資料，加上 264 筆多中心獨立臨床測試。"
  - title: "成果"
    body: "建立同時考量 sensitivity、precision、FP/scan 與保留病灶分類的評估架構。"
relatedPrevTitle: "從醫療 AI 研究到可部署產品"
relatedPrevURL: "work/medical-ai-product/"
relatedNextTitle: "第三方測試與驗證營運"
relatedNextURL: "work/structured-validation/"
---


## 單一 accuracy 無法描述臨床閱片品質

醫療影像模型不能只看一個 headline metric；評估需要同時考慮獨立資料、實際失敗模式，以及漏診與偽陽性閱片負擔之間的取捨。

## 我的角色與研究範圍

作為 Research Assistant / Project Lead，我負責腦部影像模型開發與評估、臨床資料處理、錯誤模式分析，以及向臨床與國際研究場合傳達技術結果。

<div class="case-proof-grid technical-scope-grid">
  <div class="case-proof"><strong>12,125</strong><span>Development MRI exams</span><small>23,341 個標註腫瘤病灶</small></div>
  <div class="case-proof"><strong>264</strong><span>Independent test exams</span><small>132 positive · 132 negative</small></div>
  <div class="case-proof"><strong>2</strong><span>Medical centers</span><small>Taipei VGH · Taichung VGH</small></div>
</div>

Development cohort 用於模型開發、internal validation 與 operating-point characterization；**264 例 independent clinical test cohort** 保留作為最終端到端評估。

<figure class="case-visual case-visual-vector">{{< site-img src="images/projects/detail-v521/clinical-cascade-v521.webp" alt="逐病灶 AI 三階段評估流程" >}}<figcaption><strong>Evaluation framework.</strong> Stage 0 建立高敏感度候選池，Stage 1 移除明顯偽陽性，Stage 2 處理剩餘偽陽性並進行保留病灶分類。</figcaption></figure>

## 不只看 headline accuracy

評估設計刻意分離 development 與 independent clinical testing，並把 lesion-wise sensitivity 與 FP/scan、precision 一起解讀，同時分析 deleted true positives 與 residual false positives；腫瘤分類結果只在保留的 true-positive lesions 上計算。

<div class="case-metrics case-metrics-v524">
  <div class="case-metric"><strong>80.97%</strong><span>Lesion-wise sensitivity</span><small>Independent test cohort</small></div>
  <div class="case-metric"><strong>0.21</strong><span>False positives / scan</span><small>完整 cascade 後</small></div>
  <div class="case-metric"><strong>76.89%</strong><span>Lesion-wise precision</span><small>Final cascade output</small></div>
  <div class="case-metric"><strong>90.16%</strong><span>Five-class accuracy</span><small>Retained true-positive lesions</small></div>
</div>

<figure class="case-visual-v521 case-visual-full-v521">{{< site-img src="images/projects/detail-v521/clinical-evaluation-v521.webp" alt="腦部 MRI 逐病灶模型評估與篩選概念圖" >}}<figcaption><strong>概念評估視覺。</strong> 用於解釋候選篩選、病灶分類與效能評估，不是研究 pipeline 的實際截圖。</figcaption></figure>

## 研究工程與成果溝通

最終 cascade 只是整體工作的一層；可重複的評估還仰賴影像 preprocessing、ground-truth 管理、實驗設計與清楚的 study-scope 溝通。

<div class="case-tooling-grid-v524">
  <article><span>IMAGING PIPELINE</span><p>ANTs · SimpleITK · NiBabel · 3D Slicer</p></article>
  <article><span>MODELING</span><p>PyTorch · MONAI · nnU-Net · scikit-learn</p></article>
  <article><span>EVALUATION & DATA</span><p>Python · pandas · NumPy · statistical analysis</p></article>
</div>

相關工作還包含 **ANTs MRI registration、hospital-data standardization / format conversion、ground-truth consensus 管理，以及 radiomics / segmentation / classification experiments**。相關研究版本發表於 **MIDL 2026** 與 **AMLDS 2026**；本頁 headline metrics 統一採最終碩論 independent-cohort evaluation。

## Takeaway

技術可信度不只來自模型 accuracy，也來自清楚的資料範圍、正確的 denominator、明確的 failure analysis，以及對證據能支持與不能支持之處的精準溝通。

<div class="case-capabilities-v523"><span class="case-capabilities-label-v523">CAPABILITIES DEMONSTRATED</span><div class="case-capabilities-chips-v523"><span>Machine Learning</span><span>Medical Imaging</span><span>Model Evaluation</span><span>Error Analysis</span><span>Research Communication</span></div></div>
