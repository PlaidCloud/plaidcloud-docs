---
title: Create SAP PCM Model 步骤
description: 通过 PlaidCloud 工作流步骤创建新的 SAP PCM 模型，以搭建盈利能力和成本管理的计算结构。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/create-sap-pcm-model.md
---

## 说明



在 PCM 服务器上创建一个新的空白 SAP 盈利能力与成本管理（PCM）模型。适用于以编程方式配置模型，例如当新的业务单元或方案需要自己的模型时，工作流可以直接创建，而无需等待手动设置。

大多数用户会通过 [Copy SAP PCM Model 步骤](/zh-cn/reference/workflow-steps/sap-pcm/copy-sap-pcm-model/)从现有模型模板复制，而不是从空白开始。


## 我们的资质


PlaidCloud 是 SAP 官方合作伙伴，也是 SAP PCM 模型设计与实施相关服务的首选供应商。








## 示例


从下拉列表中选择要使用的代理。输入“Model Name”，并从下拉列表中选择“Model type”（两者都位于“模型信息”部分）。勾选“Wait for Copy to Complete”复选框，然后单击“Save and Run Step”。
