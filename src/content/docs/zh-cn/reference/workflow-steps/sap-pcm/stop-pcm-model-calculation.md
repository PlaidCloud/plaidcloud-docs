---
title: Stop PCM Model Calculation 步骤
description: 通过 PlaidCloud 工作流步骤停止正在运行的 SAP PCM 模型计算，以便在检测到错误或问题时中止处理。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation.md
---

## 说明



中止正在进行的 SAP PCM 模型计算。适用于计算耗时过长、使用了错误的输入数据启动，或需要停止以释放服务器资源给更高优先级作业的情况。

如果当前没有正在运行的计算，该步骤会向工作流日志写入一条警告并继续执行。


## 我们的资质


PlaidCloud 是 SAP 官方合作伙伴，也是 SAP PCM 模型设计与实施相关服务的首选供应商。




## 示例


从下拉列表中选择“要使用的代理”，输入“Model Name”，选中“Wait for Copy to Complete”复选框，然后单击“Save and Run Step”。
