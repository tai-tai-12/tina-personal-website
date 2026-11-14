---
title: FairPay AI — 以證據為基礎的帳單流程
translationKey: fairpay-ai
independent: true
weight: 4
category: 獨立作品 · AI 產品
summary: 黑客松原型：核對 AI 擷取的合約資訊、獨立處理財務規則，並透過人工授權控制 PayPal Sandbox 帳單草稿。
description: FairPay AI 黑客松產品原型，使用合成資料展示合約證據核對、人工審核與 PayPal Sandbox 帳單草稿控制。
heroSize: compact
heroBackground: images/projects/fairpay-evidence-flow-v815-zh.svg
detailHero: images/projects/fairpay-evidence-flow-v815-zh.svg
heroDek: 以來源證據為核心，將 AI 提議、財務核對及人工授權清楚分開的合約至帳單產品原型。
snapshot:
- title: 問題
  body: 合約、折抵、驗收與帳單分散在不同工具；AI 擷取錯誤可能放大問題。
- title: 我的重點
  body: 問題定義、來源證據審核流程、人工授權機制與原型驗證。
- title: 原型
  body: 本機單人使用的總覽、合約與帳務畫面；可選用本機 AI 和 PayPal Sandbox。
- title: 適用邊界
  body: 僅使用合成情境，非正式上線的支付服務，也沒有完成銀行入帳驗證。
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
heroThemes:
- AI 輔助合約審查
- 來源證據核對
- 人工授權帳單草稿
---

<span id="problem"></span>
## 能從合約找到金額，不代表可以直接開立帳單

自由工作者與小型團隊常將合約、里程碑、折抵與帳單分散在不同工具。即使 AI 正確讀出合約費用，仍可能因尚未驗收、折抵未確認或變更條款未簽署，而不適合立刻請款。

**FairPay AI** 探索更審慎的流程：**來源證據 → 人工核對 → 財務檢查 → 明確授權 → PayPal Sandbox 帳單草稿**。核心決策是將「合約金額吻合」與「已獲准開立帳單」分開判斷。

<span id="decisions"></span>
## FairPay 的三項產品設計決策

<div class="fairpay-decision-grid">
  <article><span>01 · 證據先於自動化</span><h3>讓 AI 提議可以追溯來源</h3><p>本機 AI 會附上費用、里程碑及對應合約文字，供使用者審核。在一個合成案例中，AI 將合約的 <strong>500 美元</strong>提議為 <strong>50 美元</strong>；產品辨識差異並依據原文修正。</p></article>
  <article><span>02 · 財務規則獨立處理</span><h3>金額吻合不等於可以請款</h3><p>合約金額、人工記錄的折抵與待收款金額分開處理。驗收未完成、折抵待核、缺少證據或金額不符，都可能阻擋帳單草稿。</p></article>
  <article><span>03 · 明確的人工授權</span><h3>開立動作需要人員確認</h3><p>建立 PayPal Sandbox 帳單草稿前，必須先完成審核及人工授權。系統不會自行批准請款，也不會將草稿視為已付款。</p></article>
</div>

<span id="tour"></span>
## 三個真實產品畫面

以下是使用合成資料的 **FairPay 本機原型真實畫面**。點選圖片可放大檢視；三個畫面代表不同的示範情境。

<div class="fairpay-screens">
{{< fairpay-screen src="images/projects/fairpay-overview-v815.webp" alt="FairPay 總覽畫面，展示兩個合成帳務情境" title="01 · Overview 總覽。" caption="合約費用 500 美元、人工記錄的 100 美元折抵，以及另一個未簽署的價格變更案例；唯讀預覽不會儲存或送出資料。" zoom="放大產品畫面" >}}
{{< fairpay-screen src="images/projects/fairpay-agreements-v815.webp" alt="FairPay 合約畫面，展示 AI 提議 50 美元與來源 500 美元的差異" title="02 · Agreements 合約。" caption="AI 提議 50 美元，但原始合約寫明 500 美元；核對來源不等於已取得請款授權。" zoom="放大產品畫面" >}}
{{< fairpay-screen src="images/projects/fairpay-payments-v815.webp" alt="FairPay 帳務畫面，因折抵及驗收待核對而阻擋草稿" title="03 · Payments 帳務。" caption="折抵與驗收資訊尚未核對時，系統會阻擋草稿；這個示範畫面沒有建立 PayPal 帳單。" zoom="放大產品畫面" >}}
</div>

<div class="fairpay-action-links"><a href="https://www.youtube.com/watch?v=pivk3KyXpEQ" target="_blank" rel="noopener noreferrer">觀看三分鐘 Demo ↗</a><a href="https://github.com/tai-tai-12/fairpay-ai" target="_blank" rel="noopener noreferrer">GitHub 原始碼 ↗</a><a href="https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/PRODUCT_TOUR.md" target="_blank" rel="noopener noreferrer">三個畫面產品導覽 ↗</a></div>

<span id="evidence"></span>
## 測試證據及適用限制

公開文件記錄 **2026 年 11 月 4 日的本機專項測試有 161 項通過**，涵蓋當前回歸測試、合成情境評估、隔離的 HTTP 測試及固定的對抗測試。這**不代表歷史上的全部測試都通過**：專案文件也保留過去測試失敗及尚未完成的外部驗證項目。

影片另外展示另一組合成案例的既有 **400 美元 PayPal Sandbox 草稿**；該草稿沒有寄送或付款，人工記錄的折抵也未經銀行驗證。

**原型限制：** FairPay 為本機單人使用程式，以合成資料展示；AI 提取需額外啟動本機模型；可使用自行設定的 PayPal Sandbox 帳號測試草稿作業。沒有正式產品身分驗證、真實客戶付款、銀行入帳驗證或公開託管的金流服務。50／500 美元比對、帳單阻擋，以及另一例 400 美元 Sandbox 草稿是**三個不同情境**。

<div class="fairpay-action-links fairpay-subtle-links"><a href="https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/VALIDATION.md" target="_blank" rel="noopener noreferrer">測試證據與限制 ↗</a><a href="https://github.com/tai-tai-12/fairpay-ai/blob/main/docs/DEVELOPER_GUIDE.md" target="_blank" rel="noopener noreferrer">本機安裝與操作 ↗</a></div>

<span id="takeaway"></span>
## 核心收穫

FairPay 展示 **AI 模型以外的產品判斷**：保留可追溯的來源、將財務規則分開，並在人員審核後才允許高風險動作。它延伸了我的跨產業產品能力，但仍是使用合成資料的黑客松原型，並非已正式上線的產品。

<div class="case-capabilities-v523"><span class="case-capabilities-label-v523">代表能力</span><div class="case-capabilities-chips-v523"><span>AI 產品設計</span><span>問題定義</span><span>財務流程規劃</span><span>證據核對</span><span>人工審核控制</span><span>原型測試</span></div></div>
