---
title: Notify via Slack 步骤
description: 通过 PlaidCloud 工作流步骤发送 Slack 通知，向频道或用户提醒工作流事件、错误和状态。
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-slack.md
---

从工作流添加 Slack 通知分为两个部分：


1. 创建 Slack Webhook 外部连接
2. 将 Slack 通知步骤添加到工作流

## 将 Slack 通知步骤添加到工作流


将 Slack 通知步骤添加到工作流与添加其他步骤相同。添加步骤后，打开步骤配置，填写表单并保存。随后即可测试 Slack 通知。



## 附加文件

在**要上传的文件**中选择一个文档，即可将其连同消息（作为其评论）一起发送到频道。Webhook 无法携带文件，因此附件需要通过 Slack 连接上的机器人令牌发送：

- 向连接添加**机器人令牌**。它是具有 `files:write` 范围的 Slack 应用的 `xoxb-` 令牌，并且该应用必须已被邀请加入该频道。
- 在步骤中输入**频道 ID**，例如 `C0123ABCD`，而不是频道名称。Slack 的文件上传只接受 ID，没有 ID 则步骤会失败。要查找 ID，请在 Slack 中打开频道详情并滚动到底部。
- 如果找不到该文档，消息将通过 Webhook 发送但不带该文档，步骤会给出带有该文档路径的警告。

## 设置 Slack 消息的格式


Slack 提供多种格式设置选项，包括添加图像和提及用户。详情请参阅 [Slack 文本格式设置](https://api.slack.com/reference/surfaces/formatting)文档。



## 创建 Slack Webhook 外部连接


这是一次性设置，允许 PlaidCloud 代表您发送 Slack 通知。Slack 允许创建 Webhook 应用（通过互联网发送通知的通用方式）。在 Slack 中创建 Webhook 应用后，将提供的凭据添加到 PlaidCloud 即可使用它。



### 创建 Slack Webhook 应用


这些步骤需要由 Slack 管理员执行。请按以下步骤创建 Slack Webhook 应用：


1. 在 Slack 中，打开工作区控制菜单并选择 `Settings & administration > Manage Apps`
2. 从应用类别列表中选择 `Custom Integrations`
3. 从应用列表中选择 `Incoming Webhooks`
4. 选择 `Add to Slack` 按钮
5. 在下一个屏幕上，选择要发布消息的 Slack 频道并继续。这是将使用的默认频道，但可以在每条通知中覆盖，包括向特定个人发送私信。
6. 复制显示的 Webhook URL。稍后会用到，请妥善保管。它看起来类似于：`https://hooks.slack.com/services/T04QZ1435/G02TGBFTOP8/K9GZrR2ThdJz1uSiL9YeZxoR`
7. 保存之前可以自定义外观、名称和表情符号。这些自定义只是默认值，可以在 PlaidCloud 工作流内的每个通知步骤上覆盖。

### 设置 PlaidCloud 外部连接


这些步骤需要由具有创建外部数据连接权限的 PlaidCloud 工作区管理员执行。请按以下步骤创建连接：


1. 导航到 `Analyze > Tools > External Data Connections`
2. 在 `+ New Connection` 选项下，选择 Slack Webhook
3. 填写名称、描述，并粘贴上文第 6 步中提供的 Webhook URL。此处提供的名称将显示为工作流步骤中的选项，因此应尽可能具有描述性。任何持有该 URL 的人都可以向您的频道发帖，因此 **Webhook URL** 字段会在您粘贴时将其遮蔽，并在您重新打开连接时显示为空；保持为空即可保留已保存的 URL。
4. 若要发送附件，还需将 Slack 应用的机器人令牌粘贴到**机器人令牌（用于上传文件）** 字段中。连接可以保存 Webhook URL、机器人令牌，或两者都保存。机器人令牌与 Webhook URL 一样会被遮蔽，并在您重新打开连接时显示为空。
5. 选择 `+ Create` 按钮


## 示例

暂无示例…
