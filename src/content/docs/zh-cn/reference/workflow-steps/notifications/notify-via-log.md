---
title: Notify Via Log 步骤
description: 通过 PlaidCloud 工作流步骤写入日志条目，以记录状态消息、调试信息和审计追踪事件。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-log.md
---

## 描述


向 Analyze 工作流日志写入一条消息。



### 消息参数


输入要写入日志的消息，然后从以下三个严重级别中选择一个：


* 信息
* 警告
* 错误

请注意，项目变量和工作流变量都可用于此转换。


## 示例


在此示例中，执行此转换会向日志追加一条**信息**项，内容为 *Write a message to the workflow log. I believe you have my stapler, Demo.*
