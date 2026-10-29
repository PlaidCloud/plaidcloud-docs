---
title: Grok
description: 通过自定义连接器，将 xAI 的 Grok 连接到 PlaidCloud 的 MCP 服务器。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/grok.md
---

[Grok](https://grok.com) 通过自定义连接器支持 MCP 服务器，连接器在 grok.com 上配置。

## 设置

1. 前往 [grok.com/connectors](https://grok.com/connectors)，点击 **New Connector → Custom**。
2. 粘贴 MCP 服务器 URL：`https://<your-workspace>.plaid.cloud/mcp`。
3. Grok 将您重定向到 PlaidCloud 后，完成登录。此时会看到 **Application Access Request** 页面，其中列出请求访问的应用程序以及凭据将发送到的重定向 URI，批准前请确认两者与 Grok 一致。

## 企业套餐

Business 和 Enterprise 工作区通过团队管理员设置连接器：由工作区管理员在 grok.com/connectors 配置连接器，之后成员再将各自的账户连接到该连接器。

## 刷新访问权限

如果 Grok 提示连接需要重新授权，请重复登录步骤。连接器会保留其 URL，因此无需从头重新添加。
