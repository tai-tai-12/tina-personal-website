---
title: "從醫療 AI 研究走向可部署產品"
translationKey: "medical-ai-product"
tags: ["產品管理", "醫療 AI", "法規", "跨團隊協作"]
category: "產品轉譯"
summary: "串接臨床 AI 研究、驗證、法規準備與部署就緒。"
proof: ["2 medical centers", "TFDA submission"]
visual: "product-visual"
weight: 1
heroBackground: "images/projects/work-product-v519.webp"
detailHero: "images/projects/detail-v521/product-hero-v521.webp"
detailHeroAlt: "Clinical AI product workflow at a brain MRI review workstation"
---

我參與將腦瘤 MRI 研究轉化為可融入臨床使用情境的工作流程，同時協調產品、驗證與法規工作，推進產品化與部署準備。

<figure class="case-visual case-visual-vector">
  {{< site-img src="images/projects/detail-v521/product-workflow-v521.webp" alt="從 PACS 個案調閱、AI 輔助 MRI 判讀到醫師覆核的概念性臨床產品流程" >}}
  <figcaption>依公開安全原則重新繪製的概念流程：PACS 個案調閱 → AI 狀態 → MRI 判讀 → 病灶圈註 → 病灶分析 → 報告 → 醫師覆核。</figcaption>
</figure>

## 挑戰

模型表現好，不代表已經是一個可部署的產品。臨床使用還需要符合放射科醫師的判讀流程、以可理解方式呈現 AI 結果、完成驗證，並建立技術、臨床與法規利害關係人都能信任的證據。

## 我的角色

我的工作涵蓋 **產品管理、專案領導、臨床轉譯與法規執行**，包括協調醫師、工程師、主管與法規利害關係人，安排驗證優先順序、支援 TFDA 送件，以及改善送件文件與版本管理流程。

[AItewan 公司官網 ↗](https://www.aitewan-bio.com/en/)

## 方法

1. 將臨床工作流程需求轉成產品範圍與驗證優先順序。
2. 將模型表現與醫院及法規審查所需證據連結。
3. 協調技術、臨床、商業與法規團隊。
4. 建立可重複使用的文件與追蹤流程，使決策與版本更清楚。

<div class="case-proof-grid">
  <div class="case-proof"><strong>2</strong><span>家醫學中心</span><small>跨院臨床轉譯情境</small></div>
  <div class="case-proof"><strong>TFDA</strong><span>送件</span><small>產品與法規執行</small></div>
  <div class="case-proof"><strong>PACS</strong><span>連接工作流程</span><small>AI 判讀融入臨床影像調閱</small></div>
</div>

## 產品與技術決策

研究架構採用病灶層級串聯式流程，而不是把 detection 當成單一終點。高敏感度候選生成先建立廣泛病灶候選，再由後續分類器降低偽陽性，最後將保留病灶分成五類腫瘤。完整技術驗證則獨立整理於 **逐病灶臨床 AI 建立與驗證** 案例中。

<figure class="case-visual case-visual-vector">
  {{< site-img src="images/projects/detail-v521/clinical-cascade-v521.webp" alt="候選生成、偽陽性降低與最終病灶分類的三階段 AI 串聯流程" >}}
  <figcaption>為作品集重新簡化的研究架構：先優先保留敏感度，再降低偽陽性，最後進行保留病灶的腫瘤分類。</figcaption>
</figure>

## 從研究證據走向產品流程

產品層不只包含模型。臨床流程涵蓋 PACS 個案調閱、AI 處理狀態、影像瀏覽、AI 輔助病灶圈註、病灶分析，以及在醫師最終判斷前的報告檢視。系統定位為 **輔助決策工具**，最終判讀仍由臨床專業人員負責。

<div class="case-evidence-grid">
  <article class="case-evidence-card">
    {{< site-img src="images/research/midl-poster.webp" alt="Tina Tai 在 MIDL 2026 腦瘤 AI 海報前合照" >}}
    <div>
      <h3>MIDL 2026</h3>
      <p>病灶層級串聯架構以 short paper poster 形式發表於 MIDL 2026，成為這個產品案例背後可公開呈現的研究證據之一。</p>
    </div>
  </article>
  <article class="case-evidence-card">
    {{< site-img src="images/research/amlds-talk.webp" alt="Tina Tai 在 IEEE AMLDS 2026 進行口頭報告" >}}
    <div>
      <h3>IEEE AMLDS 2026</h3>
      <p>與此技術主線密切相關的病灶候選驗證與偽陽性降低工作，也以 oral presentation 形式發表於 IEEE AMLDS 2026。</p>
    </div>
  </article>
</div>

<figure class="case-visual-v521 case-visual-full-v521">
  {{< site-img src="images/projects/detail-v521/product-deployment-v521.webp" alt="醫療 AI 部署、資料串接與治理概念視覺" >}}
  <figcaption>概念性作品集視覺：呈現連接資料、產品監測、安全性與臨床治理如何共同支撐 deployment readiness。</figcaption>
</figure>

## 成果與影響

- 支援橫跨 **兩家醫學中心** 的臨床 AI 工作流程。
- 推動產品完成 **TFDA 送件**，支援商業化與醫院部署準備。
- 協調醫師、工程師、主管與法規利害關係人，對齊產品範圍、驗證優先順序與時程。
- 支援 **2024 Taiwan Medical Informatics Connectathon Level I** 醫學影像工作流程能力聲明驗證。
- 將分散的 TFDA 文件整合為雲端追蹤系統，改善檔案搜尋與版本管理。

## 我學到的事

AI 產品最困難的部分往往不只是模型，而是讓技術能力、使用者需求、審查所需證據，以及組織真正能執行的流程彼此對齊。

## Skills

產品管理 · 利害關係人協作 · Clinical AI · 法規執行 · 驗證策略 · 流程設計
