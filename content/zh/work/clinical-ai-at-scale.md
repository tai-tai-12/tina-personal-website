---
title: 設計不只看 Accuracy 的 AI 評估
translationKey: clinical-ai-at-scale
tags:
- Machine Learning
- Analytics
- Medical Imaging
- Experimentation
category: AI 評估 · ML
summary: 以 sensitivity、FP/scan、precision 與 failure analysis 設計不只看單一 accuracy 的逐病灶 AI 評估。
proof:
- 偽陽性候選減少 94.5%
- 264 例獨立 MRI 測試
- 90.16% 五類分類準確率
visual: clinical-ai-visual
weight: 2
heroBackground: images/projects/work-clinical-ai-v519.webp
detailHero: images/projects/detail-v521/clinical-hero-v521.webp
heroSize: standard
detailHeroAlt: Clinical AI dashboard showing lesion-wise brain MRI analysis
heroDek: 以多中心資料、實務失敗模式與敏感度／閱片負擔取捨，評估病灶層級腦部 MRI AI。
heroStats:
- value: '264'
  label: 獨立測試病例
- value: '0.21'
  label: 每掃描偽陽性
- value: 90.16%
  label: 五類分類準確率
snapshot:
- title: 挑戰
  body: 單一 headline metric 無法完整描述病灶偵測品質與後續閱片負擔。
- title: 我的角色
  body: 模型開發、評估設計、錯誤分析與技術溝通。
- title: 範圍
  body: 12,125 筆開發資料，加上一個正負病例平衡的多中心獨立臨床測試 cohort。
- title: 成果
  body: 建立同時考量 sensitivity、precision、FP/scan 與保留病灶分類的評估架構。
relatedPrevTitle: 在真實臨床限制下推進醫療 AI 產品
relatedPrevURL: work/medical-ai-product/
relatedNextTitle: 客戶導向的第三方驗證營運
relatedNextURL: work/structured-validation/
navItems:
- id: problem
  label: 01 評估問題
- id: role
  label: 02 角色與範圍
- id: evaluation
  label: 03 效能評估
- id: engineering
  label: 04 研究工程
- id: takeaway
  label: 05 重點收斂
---


<span id="problem"></span>
## 單一 accuracy 無法描述臨床閱片品質

醫療影像模型不能只看一個 headline metric；評估需要同時考慮獨立資料、實際失敗模式，以及漏診與偽陽性閱片負擔之間的取捨。

<span id="role"></span>
## 我的角色與研究範圍

作為 Research Assistant / Project Lead，我負責腦部影像模型開發與評估、臨床資料處理、錯誤模式分析，以及向臨床與國際研究場合傳達技術結果。

<div class="case-proof-grid technical-scope-grid">
  <div class="case-proof"><strong>12,125</strong><span>Development MRI exams</span><small>23,341 個標註腫瘤病灶</small></div>
  <div class="case-proof"><strong>132 / 132</strong><span>Positive / negative exams</span><small>平衡的獨立測試 cohort</small></div>
  <div class="case-proof"><strong>2</strong><span>Medical centers</span><small>Taipei VGH · Taichung VGH</small></div>
</div>

Development cohort 用於模型開發、internal validation 與 operating-point characterization；**independent clinical test cohort** 則保留作為最終端到端評估。

<figure class="case-visual case-visual-vector">{{< site-img src="images/projects/detail-v521/clinical-cascade-v521.webp" alt="逐病灶 AI 三階段評估流程" >}}<figcaption><strong>Evaluation framework.</strong> Stage 0 建立高敏感度候選池，Stage 1 移除明顯偽陽性，Stage 2 處理剩餘偽陽性並進行保留病灶分類。</figcaption></figure>

<span id="evaluation"></span>
## 不只看 headline accuracy

評估設計刻意分離 development 與 independent clinical testing，並把 lesion-wise sensitivity 與 FP/scan、precision 一起解讀，同時分析 deleted true positives 與 residual false positives；腫瘤分類結果只在保留的 true-positive lesions 上計算。

<div class="case-metrics case-metrics-v524">
  <div class="case-metric"><strong>80.97%&nbsp;</strong><span>Lesion-wise sensitivity</span><small>Independent test cohort</small></div>
  <div class="case-metric"><strong>0.21&nbsp;</strong><span>False positives / scan</span><small>完整 cascade 後</small></div>
  <div class="case-metric"><strong>76.89%&nbsp;</strong><span>Lesion-wise precision</span><small>Final cascade output</small></div>
  <div class="case-metric"><strong>90.16%&nbsp;</strong><span>Five-class accuracy</span><small>Retained true-positive lesions</small></div>
</div>

<p class="clinical-key-outcome-v82"><strong>偽陽性候選從 1,007 降至 55（−94.54%）。</strong>降低判讀負擔的同時，逐病灶敏感度也有實際下降，因此下方並列呈現兩項結果。</p>

<section class="clinical-tradeoff-v81" aria-labelledby="tradeoff-title-v81">
  <div class="clinical-tradeoff-heading-v81"><span>效能取捨 · 同一組 264 例回溯性獨立測試</span><h3 id="tradeoff-title-v81">降低大量誤報，也必須呈現 sensitivity 的代價。</h3><p>與 Stage-0 候選池相比，完整 cascade 大幅減少偽陽性檢閱負擔，但同時額外損失九個真陽性病灶。這兩個方向都是模型評估的重要部分。</p></div>
  <div class="clinical-tradeoff-pair-v81"><div><span>每例偽陽性 FP/SCAN</span><div class="tradeoff-comparison-v81"><span class="tradeoff-value-v81">Stage 0 <strong>3.81</strong></span><div class="tradeoff-line-v81"><i style="width:100%"></i></div><span class="tradeoff-value-v81">Full cascade <strong>0.21</strong></span><div class="tradeoff-line-v81"><i style="width:5.51%"></i></div></div><b>偽陽性候選減少 94.54%</b></div><div><span>逐病灶敏感度 SENSITIVITY</span><div class="tradeoff-comparison-v81"><span class="tradeoff-value-v81">Stage 0 <strong>84.96%</strong></span><div class="tradeoff-line-v81"><i style="width:84.96%"></i></div><span class="tradeoff-value-v81">Full cascade <strong>80.97%</strong></span><div class="tradeoff-line-v81"><i style="width:80.97%"></i></div></div><b>下降 3.99 個百分點</b></div></div>
  <p class="clinical-tradeoff-source-v81">資料來源：最終碩士論文、264 例回溯性 MRI 測試（226 個標註病灶）。此為研究評估，並非前瞻性臨床成效研究；最終 precision 為 76.89%，Stage 0 為 16.01%。</p>
</section>

<span id="engineering"></span>
## 從臨床洞察到技術設計

最終 cascade 只是整體工作的一層；可重複的評估還仰賴影像 preprocessing、ground-truth 管理、實驗設計與清楚的 study-scope 溝通。

<div class="clinical-insight-v6"><span>CLINICAL INSIGHT → TECHNICAL DESIGN</span><h3>用臨床 domain knowledge 找模型失敗原因，而不是只換 architecture</h3><p>當 glioma 與 metastasis 長期容易混淆時，我重新回到 MRI 影像本身，利用醫事放射背景觀察肉眼可辨識特徵，與醫師確認後，再把這些臨床 insight 轉成模型與 augmentation 實驗。這是我把臨床推理轉成技術設計的代表例子。</p></div>

重點先放在問題判斷與 evidence；工具則作為支撐。

<div class="clinical-evidence-notes-v81"><article><span>GROUND-TRUTH 品質</span><h3>專家達成共識前的一致性</h3><p>腫瘤類型的 Fleiss’ κ 為 <strong>0.9416</strong>，軸內／軸外分類為 <strong>0.9514</strong>；分割 mean Dice 為 <strong>0.8864</strong>。這些評估的是標註一致性，不是模型準確率。</p></article><article><span>減少輸入序列的次要分析</span><h3>T1C-only vs. T1C + T2</h3><p>次要 T1C-only 組態的 sensitivity 為 <strong>73.89%</strong>、<strong>0.09 FP/scan</strong>、保留真陽性五分類 accuracy 為 <strong>88.62%</strong>；主要 T1C+T2 組態則為 <strong>80.97%</strong>、<strong>0.21</strong>、<strong>90.16%</strong>。兩組保留的病灶並不完全相同，因此五分類數值不能直接當作相同病灶的比較。</p></article></div>

<details class="technical-details-v62">
  <summary>Technical details</summary>
  <div class="case-tooling-grid-v524">
    <article><span>IMAGING PIPELINE</span><p>ANTs · SimpleITK · NiBabel · 3D Slicer</p></article>
    <article><span>MODELING</span><p>PyTorch · MONAI · nnU-Net · scikit-learn</p></article>
    <article><span>EVALUATION & DATA</span><p>Python · pandas · NumPy · statistical analysis</p></article>
  </div>
  <p>相關工作還包含 MRI registration、hospital-data standardization / format conversion、ground-truth consensus 管理，以及 radiomics / segmentation / classification experiments。</p>
</details>

相關研究版本發表於 **MIDL 2026** 與 **AMLDS 2026**；本頁 headline metrics 刻意統一採最終碩論 independent-cohort evaluation。

<div class="case-boundary-v81"><strong>研究證據的限制</strong><p>這是雙中心回溯性獨立測試，不是 prospective reader study，亦未證實臨床實務中醫師判讀時間、alert fatigue、病人預後或自主診斷能力的改善。MIDL 2026 公開論文使用的是<strong>另一組 249 例</strong>的 held-out cohort，其 90.13% sensitivity 和 0.41 FP/scan 不能與本論文 264 例數據混為同一組結果。</p></div>

<span id="takeaway"></span>
## Takeaway

技術可信度不只來自模型 accuracy，也來自清楚的資料範圍、正確的 denominator、明確的 failure analysis，以及對證據能支持與不能支持之處的精準溝通。

<div class="case-capabilities-v523"><span class="case-capabilities-label-v523">CAPABILITIES DEMONSTRATED</span><div class="case-capabilities-chips-v523"><span>Machine Learning</span><span>Medical Imaging</span><span>Model Evaluation</span><span>Error Analysis</span><span>Research Communication</span></div></div>
