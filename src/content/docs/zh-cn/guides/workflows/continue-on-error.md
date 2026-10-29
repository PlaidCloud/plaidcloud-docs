---
title: 出错时继续
description: 将 PlaidCloud 工作流步骤配置为出错时继续执行，使后续步骤在前面的步骤失败后仍能运行。
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/continue-on-error.md
---

工作流步骤可以设置为即使出错也继续处理。这在工作流启动条件或数据可能间歇性可用的情况下很有用。如果步骤出错，会记录为错误，但工作流将继续处理。



要设置此选项，请在工作流表中打开该步骤的表单（单击其齿轮图标，或右键单击并选择**编辑步骤详细信息**），然后转到**常规**选项卡。将**出错时要执行的操作**设置为**继续**。保存更新后的步骤后，该步骤的任何错误都不会导致工作流停止。



设置为出错时继续的步骤，在工作流步骤层次结构表中会有特殊标记。
