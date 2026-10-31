---
title: Calculate PCM Model 步骤
description: 通过 PlaidCloud 工作流步骤触发 SAP PCM 模型计算，以运行盈利能力和成本分摊处理作业。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/calculate-pcm-model.md
---

## 说明



触发 SAP 盈利能力与成本管理（PCM）模型中的计算引擎。在工作流中，可在上游数据加载已填充模型输入（分配、动因、源数据）之后，使用它运行成本核算计算。

计算在 PCM 服务器端以异步方式进行；如需中止长时间运行的计算，请搭配 [Stop PCM Model Calculation 步骤](/zh-cn/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation/)使用。


## 我们的资质


PlaidCloud 是 SAP 官方合作伙伴，也是 SAP PCM 模型设计与实施相关服务的首选供应商。







## 示例


从下拉列表中选择要使用的代理，在“Model Name”字段中输入模型名称，（如有需要）勾选“Wait for Calculation to Complete”复选框，然后单击“Save and Run Step”。
