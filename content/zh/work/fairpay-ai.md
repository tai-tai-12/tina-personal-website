---
title: "FairPay AI — 以證據為基礎的帳單流程"
translationKey: fairpay-ai
independent: true
weight: 4
category: 獨立作品 · AI 產品
summary: 黑客松原型：將 AI 從合約提取的條款與來源文字比對，區分財務審核與人工授權，在確認條件前不建立 PayPal Sandbox 帳單草稿。
description: "FairPay AI 黑客松產品原型，使用合成資料展示合約證據核對、人工審核與 PayPal Sandbox 帳單草稿控制。"
heroSize: compact
heroBackground: images/projects/fairpay-evidence-flow-v814-zh.svg
detailHero: images/projects/fairpay-evidence-flow-v814-zh.svg
heroDek: 讓 AI 提議、原始合約證據、財務審核與人工授權各自有明確邊界，避免未經核對就產生帳單草稿。
heroStats:
- value: "3"
  label: 產品主要畫面
- value: "161"
  label: 紀錄中通過的本機專項檢查
- value: "Sandbox"
  label: 僅示範帳單草稿
snapshot:
- title: 問題
  body: 合約、里程碑驗收、折抵金額與帳單散落在不同工具，AI 提取錯誤可能進一步造成錯誤開立。
- title: 工作重點
  body: 產品問題定義、來源證據審核流程、阻擋機制、原型展示及測試限制紀錄。
- title: 原型範圍
  body: 本機單人使用的 Overview、Agreements、Payments 三個畫面；可選用本機 AI 提取及 PayPal Sandbox 測試。
- title: 使用邊界
  body: 僅使用合成資料和示例情境；非正式上線產品、銀行結算驗證工具或真實付款服務。
relatedPrevTitle: 執行客戶導向的第三方驗證作業
relatedPrevURL: work/structured-validation/
navItems:
- id: problem
  label: 01 產品問題
- id: decisions
  label: 02 設計決策
- id: tour
  label: 03 產品導覽
- id: evidence
  label: 04 測試與限制
- id: takeaway
  label: 05 核心收穫
---

<span id="problem"></span>
## 問題不只是帳單金額錯誤，而是缺少可核對的開立依據

自由工作者及小型服務團隊常將合約條款、里程碑驗收、折抵紀錄與帳單分散保存在不同工具。即使合約寫明費用，也**不表示現在就可以開立帳單**：可能有尚未審核的折抵、尚未驗收的工作，或尚未簽署的新價格條款。AI 若提取錯誤數字，過度自動化反而可能放大錯誤。

**FairPay AI** 是一個黑客松產品原型，探索更審慎的流程：**來源證據 → 人工核對 → 財務規則 → 明確授權 → PayPal Sandbox 帳單草稿**。設計重點是區分「來源數字正確」與「已獲准開立帳單」。

<span id="decisions"></span>
## 三項關鍵產品設計決策

<div class="fairpay-decision-grid">
  <article><span>01 · 證據先於自動化</span><h3>讓 AI 提議可以追溯來源</h3><p>本機 AI 提出費用、里程碑與相應合約文字，使用者確認來源後才能接受。在其中一個合成情境中，AI 將合約中的 <strong>500 美元</strong>提議為 <strong>50 美元</strong>，產品協助辨識差異並依據原文修正。</p></article>
  <article><span>02 · 財務規則必須獨立</span><h3>金額符合合約，不等於可以請款</h3><p>合約費用、人工記錄的折抵金額和待收款金額分開處理；驗收狀態、折抵是否核對、缺少證據或金額不符，都可能阻止建立帳單草稿。</p></article>
  <article><span>03 · 人工授權不可省略</span><h3>每次帳單動作都需明確核准</h3><p>原型透過 PayPal Sandbox 示範帳單草稿流程。影片另外展示的既有 <strong>400 美元 Sandbox 草稿</strong>來自另一組合成案例，並<strong>未寄送、未付款，也未經銀行驗證</strong>。</p></article>
</div>

<span id="tour"></span>
## 三個真實產品畫面

下列圖片是 **FairPay AI 本機原型使用合成資料的真實畫面截圖**，檔案存放於公開 GitHub repository。每個畫面對應不同測試情境，並不是同一筆已完成的付款交易。

<div class="fairpay-screens">
  <figure class="fairpay-screen"><img src="https://raw.githubusercontent.com/tai-tai-12/fairpay-ai/main/assets/fairpay-overview-demo.png" loading="lazy" decoding="async" alt="FairPay AI Overview 的真實畫面，展示兩組合成帳務決策情境"><figcaption><strong>01 · Overview 總覽。</strong> 示範合約費用 500 美元減去人工記錄的 100 美元折抵；另一個案例說明尚未簽署的價格調整。這些唯讀預覽不會儲存專案或聯絡 PayPal。</figcaption></figure>
  <figure class="fairpay-screen"><img src="https://raw.githubusercontent.com/tai-tai-12/fairpay-ai/main/assets/fairpay-agreement-evidence-demo.png" loading="lazy" decoding="async" alt="FairPay AI Agreements 真實畫面，顯示 AI 提議 50 美元、合約來源寫 500 美元"><figcaption><strong>02 · Agreements 合約。</strong> AI 提議 50 美元，而來源文字是 500 美元；即使與合約吻合，也不表示里程碑已經驗收或已獲得請款授權。</figcaption></figure>
  <figure class="fairpay-screen"><img src="https://raw.githubusercontent.com/tai-tai-12/fairpay-ai/main/assets/fairpay-payments-review-demo.png" loading="lazy" decoding="async" alt="FairPay AI Payments 真實畫面，顯示審核未完成而阻擋建立帳單"><figcaption><strong>03 · Payments 帳務。</strong> 折抵與驗收證據未完成審核前，原型會阻擋建立帳單草稿。這張截圖中沒有建立 PayPal 帳單。</figcaption></figure>
</div>

<div class="fairpay-action-links"><a href="https://www.youtube.com/watch?v=pivk3KyXpEQ" target="_blank" rel="noopener noreferrer">觀看三分鐘 Demo ↗</a><a href="https://github.com/tai-tai-12/fairpay-ai" target="_blank" rel="noopener noreferrer">GitHub 原始碼 ↗</a><a href="https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/PRODUCT_TOUR.md" target="_blank" rel="noopener noreferrer">三個畫面產品導覽 ↗</a></div>

<span id="evidence"></span>
## 測試證據及適用限制

公開文件記錄 **2026 年 11 月 4 日的本機專項測試有 161 項通過**，涵蓋當前回歸測試、合成情境評估、隔離的 HTTP 測試及固定的對抗測試。這**不代表歷史上的全部測試都通過**：專案文件也保留過去測試失敗及尚未完成的外部驗證項目。

**原型限制：** FairPay 為本機單人使用程式，以合成資料展示；AI 提取需額外啟動本機模型；可使用自行設定的 PayPal Sandbox 帳號測試草稿作業。沒有正式產品身分驗證、真實客戶付款、銀行入帳驗證或公開託管的金流服務。50／500 美元比對、帳單阻擋，以及另一例 400 美元 Sandbox 草稿是**三個不同情境**。

<div class="fairpay-action-links fairpay-subtle-links"><a href="https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/VALIDATION.md" target="_blank" rel="noopener noreferrer">測試證據與限制 ↗</a><a href="https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/DEVELOPER_GUIDE.md" target="_blank" rel="noopener noreferrer">本機安裝與操作 ↗</a></div>

<span id="takeaway"></span>
## 核心收穫

這項作品展現的不只是 AI 模型能力，更是**如何把 AI 的不確定性轉化成可審核的產品流程**：保留來源、獨立處理財務規則，並在風險較高的動作前設置人工授權。它也讓我的產品經驗從醫療科技延伸到 FinTech，但不宣稱已正式上線、獲得客戶採用或產生真實金流成效。

<div class="case-capabilities-v523"><span class="case-capabilities-label-v523">代表能力</span><div class="case-capabilities-chips-v523"><span>AI 產品設計</span><span>問題定義</span><span>財務流程規劃</span><span>證據核對</span><span>人工審核控制</span><span>原型測試</span></div></div>
