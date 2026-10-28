---
title: 設計不只看準確率的 AI 評估
translationKey: clinical-ai-at-scale
tags:
- Machine Learning
- Analytics
- Medical Imaging
- Experimentation
category: AI 評估 · ML
summary: 以獨立 MRI 測試評估如何減少 AI 錯誤提示，同時量測漏掉真實病灶的代價，而非只看一項準確率。
proof:
- 偽陽性候選減少 94.5%
- 264 例獨立 MRI 測試
- 90.16% 五類分類準確率
displayMetrics:
- value: "94.5%"
  label: "偽陽性候選減少"
- value: "264"
  label: "獨立 MRI 測試"
- value: "90.16%"
  label: "保留正確偵測病灶的五類分類準確率"
visual: clinical-ai-visual
weight: 2
heroBackground: images/projects/work-clinical-ai-v519.webp
detailHero: images/projects/detail-v521/clinical-hero-v521.webp
heroSize: standard
detailHeroAlt: Clinical AI dashboard showing lesion-wise brain MRI analysis
heroDek: 透過獨立多中心 MRI 測試，評估如何減少 AI 錯誤提示，以及這樣做可能漏掉多少真實病灶。
heroStats:
- value: '264'
  label: 獨立測試病例
- value: '0.21'
  label: 每掃描偽陽性
- value: 90.16%
  label: 五類分類準確率
snapshot:
- title: 挑戰
  body: MRI AI 若將正常區域誤判為腫瘤，會增加醫師審查工作；降低錯誤提示時，也必須同時量測漏掉的病灶。
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
## 減少錯誤提示，也要衡量漏掉的真實病灶

腦部 MRI AI 可能把正常區域誤標為疑似腫瘤，讓醫師需要花時間確認。我參與評估多階段模型，在 **264 例獨立回溯性 MRI 測試**中，將錯誤候選數從 **1,007 降至 55（減少 94.54%）**；同時，真實病灶的偵測比例也從 **84.96% 降至 80.97%**。這是回溯性研究評估，不代表已證實醫師臨床閱片速度改善。

<span id="role"></span>
## 我的角色與研究範圍

作為研究助理與專案負責人，我負責腦部影像模型開發與評估、臨床資料處理、錯誤模式分析，以及向臨床與國際研究場合傳達技術結果。

<div class="case-proof-grid technical-scope-grid">
  <div class="case-proof"><strong>12,125</strong><span>模型開發用 MRI 病例</span><small>23,341 個標註腫瘤病灶</small></div>
  <div class="case-proof"><strong>132 / 132</strong><span>陽性／陰性病例</span><small>正負樣本平衡的獨立測試組</small></div>
  <div class="case-proof"><strong>2</strong><span>醫療中心</span><small>Taipei VGH · Taichung VGH</small></div>
</div>

開發資料用於模型訓練、內部驗證及決策閾值評估；**獨立臨床測試資料**則保留作為最終端到端評估。

<figure class="case-visual case-visual-vector">{{< site-img src="images/projects/detail-v521/clinical-cascade-v521.webp" alt="逐病灶 AI 三階段評估流程" >}}<figcaption><strong>評估流程：</strong> 第 0 階段建立高敏感度候選池，第 1 階段移除明顯偽陽性，第 2 階段處理剩餘偽陽性並進行保留病灶分類。</figcaption></figure>

<span id="evaluation"></span>
## 不只看表面準確率

評估設計刻意分離 模型開發資料與獨立臨床測試，並把 逐病灶敏感度、每張影像的偽陽性數量及精確率 一起解讀，同時分析 遭移除的真陽性病灶與剩餘偽陽性；腫瘤分類結果只在保留的 真陽性病灶 上計算。

<div class="case-metrics case-metrics-v524">
  <div class="case-metric"><strong>80.97%&nbsp;</strong><span>逐病灶敏感度</span><small>獨立測試組</small></div>
  <div class="case-metric"><strong>0.21&nbsp;</strong><span>每張影像的偽陽性數量</span><small>完整級聯流程後</small></div>
  <div class="case-metric"><strong>76.89%&nbsp;</strong><span>逐病灶精確率</span><small>完整級聯 output</small></div>
  <div class="case-metric"><strong>90.16%&nbsp;</strong><span>五類腫瘤分類準確率</span><small>Retained 真陽性病灶</small></div>
</div>

<p class="clinical-key-outcome-v82"><strong>偽陽性候選從 1,007 降至 55（−94.54%）。</strong>降低判讀負擔的同時，逐病灶敏感度也有實際下降，因此下方並列呈現兩項結果。</p>

<section class="clinical-tradeoff-v81" aria-labelledby="tradeoff-title-v81">
  <div class="clinical-tradeoff-heading-v81"><span>效能取捨 · 同一組 264 例回溯性獨立測試</span><h3 id="tradeoff-title-v81">降低大量誤報，也必須呈現 敏感度下降的代價。</h3><p>與 第 0 階段候選池相比，完整級聯流程大幅減少偽陽性檢閱負擔，但同時額外損失九個真陽性病灶。這兩個方向都是模型評估的重要部分。</p></div>
  <div class="clinical-tradeoff-pair-v81"><div><span>每例偽陽性 每張影像偽陽性數</span><div class="tradeoff-comparison-v81"><span class="tradeoff-value-v81">第 0 階段 <strong>3.81</strong></span><div class="tradeoff-line-v81"><i style="width:100%"></i></div><span class="tradeoff-value-v81">Full cascade <strong>0.21</strong></span><div class="tradeoff-line-v81"><i style="width:5.51%"></i></div></div><b>偽陽性候選減少 94.54%</b></div><div><span>逐病灶敏感度 敏感度</span><div class="tradeoff-comparison-v81"><span class="tradeoff-value-v81">第 0 階段 <strong>84.96%</strong></span><div class="tradeoff-line-v81"><i style="width:84.96%"></i></div><span class="tradeoff-value-v81">Full cascade <strong>80.97%</strong></span><div class="tradeoff-line-v81"><i style="width:80.97%"></i></div></div><b>下降 3.99 個百分點</b></div></div>
  <p class="clinical-tradeoff-source-v81">資料來源：最終碩士論文、264 例回溯性 MRI 測試（226 個標註病灶）。此為研究評估，並非前瞻性臨床成效研究；最終 精確率為 76.89%，第 0 階段 為 16.01%。</p>
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

相關研究成果發表於 **MIDL 2026** 與 **AMLDS 2026**；AMLDS 2026 論文現已收錄於 [IEEE Xplore 正式會議論文集](https://ieeexplore.ieee.org/xpl/conhome/11723344/proceeding)。本頁核心數據統一採用碩士論文中的 **264 例回溯性獨立測試** 結果，不與 AMLDS 論文的另一組評估數據混用。

<div class="case-boundary-v81"><strong>研究證據的限制</strong><p>這是雙中心回溯性獨立測試，不是 prospective reader study，亦未證實臨床實務中醫師判讀時間、alert fatigue、病人預後或自主診斷能力的改善。MIDL 2026 公開論文使用的是<strong>另一組 249 例</strong>的 held-out cohort，其 90.13% sensitivity 和 0.41 FP/scan 不能與本論文 264 例數據混為同一組結果。</p></div>

<span id="takeaway"></span>
## 重點總結

技術可信度不只來自模型 accuracy，也來自清楚的資料範圍、正確的 denominator、明確的 failure analysis，以及對證據能支持與不能支持之處的精準溝通。

<div class="case-capabilities-v523"><span class="case-capabilities-label-v523">CAPABILITIES DEMONSTRATED</span><div class="case-capabilities-chips-v523"><span>Machine Learning</span><span>Medical Imaging</span><span>Model Evaluation</span><span>Error Analysis</span><span>Research Communication</span></div></div>
