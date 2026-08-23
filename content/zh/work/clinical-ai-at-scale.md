---
title: "大規模臨床 AI 的建立與驗證"
translationKey: "clinical-ai-at-scale"
tags: ["Machine Learning", "Analytics", "Medical Imaging", "Experimentation"]
---

這個案例更聚焦我的分析與技術能力：如何在真實醫學影像資料中建立、評估並溝通模型效能。

## 挑戰

醫學影像模型不能只看單一 headline metric。需要從臨床任務、真實資料與實際 failure modes 評估系統是否可靠。

## 我的角色

作為 Research Assistant / Project Lead，我領導腦部與心臟影像專案，處理臨床資料、支援模型開發與評估，並把成果向臨床與國際 audience 溝通。

## 做法

- 定義具臨床意義的預測與驗證問題。
- 建立結構化的醫學影像分析流程。
- 使用適合任務的指標評估模型。
- 分析錯誤與失敗案例，而非只依賴總體 accuracy。
- 把技術結果轉成臨床與產品利害關係人可理解的證據。

## 技術深度

主要工具包括 Python、pandas、NumPy、scikit-learn、XGBoost、PyTorch、TensorFlow/Keras、MONAI、SimpleITK、NiBabel、3D Slicer、Git、BigQuery 與 MLflow。

## 成果

- 腦瘤工作流程：**10,893 cases、91% tumor-type classification accuracy**。
- Cardiac imaging：CT angiography model 在 **308 cases** 上報告 **92% accuracy**。
- 研究成果於國際場合發表，包括 **MIDL 2026** 與 **IEEE AMLDS 2026** 相關工作。

## 我學到的事

Technical credibility 最有價值的地方，是讓決策更好：選對 metric、理解模型在哪裡失敗，並把 uncertainty 清楚溝通到足以支援產品與臨床判斷。

