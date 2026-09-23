---
title: 從醫療 AI 研究走向可部署產品
translationKey: medical-ai-product
tags:
- 產品管理
- 醫療 AI
- 法規
- 跨團隊協作
category: 產品轉譯
summary: 透過持續醫師需求探索、模型取捨與法規執行，把腦瘤 MRI 研究轉化為真實臨床工作流程。
proof:
- ~67% faster AI processing
- 2 medical centers
visual: product-visual
weight: 1
heroBackground: images/projects/work-product-v519.webp
detailHero: images/projects/detail-v521/product-hero-v521.webp
heroSize: compact
detailHeroAlt: Clinical AI product workflow at a brain MRI review workstation
heroDek: 透過持續使用者研究、技術取捨、release sequencing、驗證與 TFDA 執行，把腦瘤 MRI 研究推向以醫師為核心的產品。
heroStats:
- value: ~67%
  label: AI 處理時間縮短
- value: 5 physicians · 2 centers
  label: 持續 workflow discovery
- value: TFDA
  label: 送件執行
snapshot:
- title: 挑戰
  body: 技術表現良好的模型，仍需要變得更快、更可理解、可設定，也要有足夠清楚的證據才能真正進入臨床使用。
- title: 我的角色
  body: 使用者研究、需求定義、技術取捨、release planning、驗證與法規執行。
- title: 範圍
  body: 兩家醫療中心的 5 位醫師，以及 AI/ML、軟體/UI、臨床、法規與主管利害關係人。
- title: 成果
  body: 更快的處理速度、更清楚的使用回饋、依工作流程調整的 operating point，以及受保護的送件時程。
relatedPrevTitle: 第三方測試與驗證營運
relatedPrevURL: work/structured-validation/
relatedNextTitle: 病灶層級臨床 AI 建置與驗證
relatedNextURL: work/clinical-ai-at-scale/
navItems:
- id: problem
  label: 01 產品問題
- id: role
  label: 02 產品決策
- id: workflow
  label: 03 工作流程
- id: evidence
  label: 04 證據與執行
- id: takeaway
  label: 05 重點收斂
---

<span id="problem"></span>
## 強模型仍需要變成醫師真正能用的產品

研究系統在技術上已有良好表現，但醫師回饋揭露了模型指標無法直接回答的產品問題：**接近兩分鐘的處理時間太慢、使用者不知道還要等多久，而且不同臨床情境對 sensitivity 與 false-positive burden 的容忍度不同。** 同時，任何模型變更都會牽動驗證、文件與法規工作的連鎖影響。

<span id="role"></span>
## 三個改變產品路徑的決策

<div class="product-decision-list-v6">
  <article><span>01 · USABILITY VS. MODEL PERFORMANCE</span><h3>優化真實工作流程，而不是只追求學術上最好的模型</h3><p>我透過持續的醫師 workflow testing，把「太慢」轉成低於一分鐘的第一階段產品目標，並與工程師共同評估 latency–sensitivity trade-off。在臨床可接受的小幅 sensitivity 下降下，端到端處理時間由約兩分鐘降到約四十秒。當醫師指出系統仍讓人感覺很慢，是因為不知道剩餘時間時，我提出百分比 progress indicator；功能上線後獲得正面回饋。</p></article>
  <article><span>02 · ONE MODEL, DIFFERENT WORKFLOWS</span><h3>把模型指標轉成 operating-point 決策</h3><p>我把 sensitivity 與 false-positive burden 翻譯成醫師實際閱片時的工作量，再透過產品試用與 competitor benchmarks 定義 institution-level thresholds。結果顯示，偏 screening 的情境可更重視 sensitivity，而其他醫療中心工作流程則可使用較平衡的 operating point。</p></article>
  <article><span>03 · BETTER MODEL VS. SHIPPING ON TIME</span><h3>不是拒絕更好的模型，而是安排正確的 release sequencing</h3><p>送件後期出現明顯改善的新模型時，我評估的不只是 engineering time，而是驗證與文件的下游重工，估計若納入當期 release 將增加約三到六個月影響。我建議沿用已完成驗證的版本送件，並把新模型排入下一開發週期；主管採納此方案，團隊維持原定六月 TFDA 送件時程。</p></article>
</div>

[AITEWAN 公司官網 ↗](https://www.aitewan-bio.com/en/)

<span id="workflow"></span>
## 從研究模型走向醫師工作流程

底層研究採逐病灶 cascade：先產生 sensitivity-oriented candidates，再降低偽陽性，最後對保留病灶進行五類分類。完整技術評估另見 **Building and Validating Lesion-Wise Clinical AI**。

產品層不只包含模型，也涵蓋 **PACS case access、AI processing-state visibility、AI-assisted lesion overlays、病灶層級閱片與報告審閱**。在兩家醫療中心進行的持續醫師 discovery，讓速度、等待可見性、operating point 與 release scope 都能被轉成具體產品需求。

<figure class="case-visual-v521 case-visual-full-v521">
  {{< site-img src="images/projects/detail-v521/product-deployment-v521.webp" alt="醫療 AI 產品部署、資料流與治理概念圖" >}}
  <figcaption><strong>概念產品流程。</strong> 呈現資料連接、AI 輔助閱片、文件與治理，不是實際產品畫面截圖。</figcaption>
</figure>

<span id="evidence"></span>
## 研究證據與產品執行

產品路徑建立在同一條逐病灶腦瘤 AI 研究主線上，並透過不同公開發表形式呈現。

<div class="case-evidence-grid">
  <article class="case-evidence-card">{{< site-img src="images/research/midl-poster.webp" alt="Tina Tai 與 MIDL 2026 海報" >}}<div><span>MIDL · 2026</span><h3>First-Author Short Paper Poster</h3><p>逐病灶偽陽性降低與五類腫瘤分類的公開研究成果。</p></div></article>
  <article class="case-evidence-card">{{< site-img src="images/research/amlds-talk.webp" alt="Tina Tai 在 AMLDS 2026 進行口頭報告" >}}<div><span>AMLDS · 2026</span><h3>First-Author Oral Presentation</h3><p>同一技術主線上聚焦候選病灶驗證與偽陽性降低的延伸研究，並獲 Outstanding Oral Presentation。</p></div></article>
</div>

<div class="case-metrics case-metrics-v524">
  <div class="case-metric"><strong>2&nbsp;</strong><span>Medical centers</span><small>持續臨床 workflow discovery</small></div>
  <div class="case-metric"><strong>TFDA&nbsp;</strong><span>Submission execution</span><small>驗證、文件與 release planning</small></div>
  <div class="case-metric"><strong>Level I&nbsp;</strong><span>Connectathon validation</span><small>2024 醫療影像流程能力驗證</small></div>
  <div class="case-metric"><strong>June&nbsp;</strong><span>Submission timeline maintained</span><small>Late model upgrade 排入下一週期</small></div>
</div>

<span id="takeaway"></span>
## Takeaway

AI 產品工作最困難的往往不是選出技術上最強的模型，而是判斷 **哪個 trade-off 對使用者最有價值、哪些證據足以支持決策，以及哪些功能該現在交付、哪些應該排到下一個 release。**

<div class="case-capabilities-v523"><span class="case-capabilities-label-v523">CAPABILITIES DEMONSTRATED</span><div class="case-capabilities-chips-v523"><span>User Discovery</span><span>Product Judgment</span><span>Technical Trade-offs</span><span>Release Planning</span><span>Regulatory Execution</span></div></div>
