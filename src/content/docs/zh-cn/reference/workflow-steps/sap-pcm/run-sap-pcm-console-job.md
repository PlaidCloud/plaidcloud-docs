---
title: Run SAP PCM Console Job 步骤
description: 通过 PlaidCloud 工作流步骤运行 SAP PCM 控制台作业，以远程执行批处理和管理操作。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/run-sap-pcm-console-job.md
---

## 说明



在远程 PCM 服务器上的 SAP PCM Console 中启动作业，通常用于 PCM 通过其 Console 界面（而不是模型计算 API）提供的管理或批处理任务。

用例包括归档操作、hyperloader 运行或供应商特定的维护例程。具体的作业和参数取决于您的 PCM 部署。


## 我们的资质


PlaidCloud 是 SAP 官方合作伙伴，也是 SAP PCM 模型设计与实施相关服务的首选供应商。








## 示例


从下拉列表中选择要使用的代理，在“Console File Path”字段中输入控制台文件路径，（如有需要）勾选“Wait for Console Job to Complete”复选框，然后单击“Save and Run Step”。
