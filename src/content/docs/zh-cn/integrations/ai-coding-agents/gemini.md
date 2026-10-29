---
title: Google Gemini CLI
description: 配置 Google 的 gemini-cli 以调用 PlaidCloud 的 MCP 工具。
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/gemini.md
---

Google 的 [`gemini-cli`](https://github.com/google-gemini/gemini-cli) 通过 `~/.gemini/settings.json`（用户范围）或项目根目录中的 `.gemini/settings.json`（项目范围）支持 MCP 服务器。

## 设置

1. 在已登录 PlaidCloud 的浏览器中访问 `https://<your-workspace>.plaid.cloud/mcp/setup/token`，获取持有者令牌。

2. 编辑 `~/.gemini/settings.json`（如果不存在则创建）：

    ```json
    {
      "mcpServers": {
        "plaidcloud": {
          "httpUrl": "https://<your-workspace>.plaid.cloud/mcp",
          "headers": {
            "Authorization": "Bearer eyJhbGc…"
          }
        }
      }
    }
    ```

3. 重启 `gemini`。在会话中运行 `/mcp`，验证服务器已连接并列出其工具。

## 使用

直接提示 Gemini 使用 PlaidCloud 工具：

- “使用 plaidcloud 列出 `Sales Forecasting` 项目中的工作流。”
- “描述 `customers` 表的列以及最近的快照。”

如果您想在调用之前查看某个工具的输入架构，也可以使用 `/tools` 命令显式调用工具。

## 刷新令牌

令牌过期后，重新加载 `https://<your-workspace>.plaid.cloud/mcp/setup/token`，并更新 `settings.json` 中 `Authorization` 的值。重启 `gemini` 以获取更改。

## Gemini Code Assist（IDE）

VSCode/JetBrains 中的 Gemini Code Assist 在其代理设置下接受相同的 `mcpServers` 配置。其架构与 CLI 形式一致，将同一段代码片段粘贴到 IDE 的 MCP 服务器设置面板下即可。
