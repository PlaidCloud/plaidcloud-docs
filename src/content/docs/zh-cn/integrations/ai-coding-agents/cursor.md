---
title: Cursor
description: 配置 Cursor IDE，通过其内置的 MCP 支持调用 PlaidCloud 的 MCP 工具。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/cursor.md
---

[Cursor](https://cursor.com) 通过 `mcp.json` 配置文件支持 MCP 服务器。其格式与 Claude Code 的 `.mcp.json` 相同，因此同一段持有者令牌配置在两者中均可使用。

从 PlaidCloud 头像（用户）菜单打开的**连接您的 AI**窗口提供**在 Cursor 中安装**一键链接，通过 OAuth 登录添加服务器，无需配置文件。请优先尝试该方式。下方的持有者令牌配置是本页完整记录的设置方式，也是在一键链接未能添加服务器或未安装 Cursor 时的备选方案。

## 设置

1. 在已登录 PlaidCloud 的浏览器中访问 `https://<your-workspace>.plaid.cloud/mcp/setup/token`，获取持有者令牌。

2. 打开 Cursor 的 MCP 配置：
   - **项目级**：在项目根目录中创建 `.cursor/mcp.json`。
   - **用户级（所有项目）**：在主目录中创建 `~/.cursor/mcp.json`。

3. 添加 PlaidCloud 服务器：

    ```json
    {
      "mcpServers": {
        "plaidcloud": {
          "url": "https://<your-workspace>.plaid.cloud/mcp",
          "headers": {
            "Authorization": "Bearer eyJhbGc…"
          }
        }
      }
    }
    ```

4. 打开 Cursor 的 **Settings → MCP**，确认服务器已连接。如果显示错误，请参阅[故障排除](../troubleshooting/)。

## 使用工具

在 Cursor 的 Composer 或聊天面板中，可以用通俗的英语向代理发出提示（例如“描述项目 `Q4 Forecast` 的结构”），它会选择合适的 `plaidcloud_*` 工具。工具调用和响应会内联显示，批准前请查看会修改数据的操作。

## 刷新令牌

令牌过期后，重新加载 `https://<your-workspace>.plaid.cloud/mcp/setup/token`，并将新值粘贴到 `mcp.json` 中。Cursor 无需完全重启即可获取更改；如有需要，请在 **Settings → MCP** 中关闭再开启该服务器。

## 多个租户

在不同名称下重复该条目：

```json
{
  "mcpServers": {
    "plaidcloud-prod": { "url": "https://prod.plaid.cloud/mcp", "headers": { "Authorization": "Bearer …" } },
    "plaidcloud-dev":  { "url": "https://dev.plaid.cloud/mcp",  "headers": { "Authorization": "Bearer …" } }
  }
}
```
