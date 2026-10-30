---
title: Notify via Microsoft Teams 步骤
description: 通过 PlaidCloud 工作流步骤发送 Microsoft Teams 通知，向频道或用户提醒工作流事件和状态。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-microsoft-teams.md
---

从工作流添加 Microsoft Teams 通知分为两个部分：


1. 创建 Microsoft Teams 外部连接
2. 将 Microsoft Teams 通知步骤添加到工作流

## 将 Microsoft Teams 通知步骤添加到工作流


将 Microsoft Teams 通知步骤添加到工作流与添加其他步骤相同。添加步骤后，打开步骤配置，填写表单并保存。随后即可测试 Microsoft Teams 通知。



## 设置 Microsoft Teams 消息的格式


Teams 提供多种格式设置选项，包括添加图像和提及用户。详情请参阅 [Teams 消息文本格式设置](https://support.microsoft.com/en-us/office/use-markdown-formatting-in-teams-4d10bd65-55e2-4b2d-a1f3-2bebdcd2c772)文档。



## 创建 Microsoft Teams 外部连接


这是一次性设置，允许 PlaidCloud 代表您发送 Microsoft Teams 通知。Microsoft Teams 允许创建 Webhook 应用（通过互联网发送通知的通用方式）。在 Microsoft Teams 中创建 Webhook 应用后，将提供的凭据添加到 PlaidCloud 即可使用它。



### 创建 Microsoft Teams Webhook 应用


这些步骤需要由 Microsoft Teams 管理员执行。请按照此处所述的步骤[创建传入 Webhook（Microsoft Teams 文档）](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook#create-incoming-webhook-1)。



### 设置 PlaidCloud 外部连接


这些步骤需要由具有创建外部数据连接权限的 PlaidCloud 工作区管理员执行。请按以下步骤创建连接：


1. 导航到 `Analyze > Tools > External Data Connections`
2. 在 `+ New Connection` 选项下，选择 Microsoft Teams Webhook
3. 填写名称、描述，并粘贴上文创建 Webhook 时生成的 Webhook URL。此处提供的名称将显示为工作流步骤中的选项，因此应尽可能具有描述性。任何持有该 URL 的人都可以向您的频道发帖，因此 **Webhook URL** 字段会在您粘贴时将其遮蔽，并在您重新打开连接时显示为空；保持为空即可保留已保存的 URL。
4. 选择 `+ Create` 按钮


## 示例

暂无示例…
