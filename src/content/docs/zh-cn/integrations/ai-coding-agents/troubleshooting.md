---
title: 故障排除
description: 将 AI 代理连接到 PlaidCloud MCP 服务器时的常见问题及解决方法。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/troubleshooting.md
---

## Cursor（或其他严格客户端）完全无法连接

现象：在 Cursor 及类似的严格客户端中，服务器始终无法建立会话，而同一工作区在 Claude Code 中可以正常使用。

原因：服务器 URL 末尾带有**斜杠**。请使用 `https://<your-workspace>.plaid.cloud/mcp`，而不是 `.../mcp/`。严格客户端会拒绝末尾带斜杠的 URL（或不会跟随旧路径发出的重定向），而 Claude Code 等宽松客户端可以容忍。

解决办法：删除配置中 `url` 末尾的斜杠，然后重新连接。这些指南中的所有示例都使用不带斜杠的形式。

## “failed to Connect” / “session Not Found”

现象：客户端配置看起来正确，但服务器在客户端的 MCP 状态面板中显示为失败。服务器日志显示 404 `Session not found` 错误。

原因：部分 MCP 客户端存在已知缺陷（最典型的是使用静态 `Authorization` 标头的 Claude Code 2.1.111），客户端在连续的 HTTP 请求之间不会保留 `mcp-session-id`。PlaidCloud 的 MCP 服务器以无状态 HTTP 模式运行，以规避此问题；如果在修复后尚未重新部署的租户上遇到此问题，请联系管理员重新部署。

在重新部署完成之前，不带静态 `Authorization` 标头的 OAuth 流程仍可使用，因为它走的是客户端中的另一条代码路径。

## “application Access Request” 页面

现象：在 OAuth 授权过程中登录 PlaidCloud 后，会进入一个标题为 **Application Access Request** 的页面，页面列出了应用程序和重定向 URI，需要点击“批准”后流程才会继续。

原因：这是正常现象。通过 PlaidCloud 的 MCP 服务器进行的每次 OAuth 授权都会显示此页面，以便在获取令牌之前确认所连接的对象，页面会列出请求方应用程序以及凭据将被发送到的重定向 URI。请检查两者是否与您实际要连接的客户端一致，不要批准不是由您发起的请求。

已连接的客户端在刷新令牌时不会再次看到此页面，只有全新的授权（首次连接，或刷新令牌过期或被撤销之后）才会再次出现。

解决办法：无需处理，批准该页面即可继续。如果授权是在一个浏览器（或配置文件）中发起的，而页面显示在另一个浏览器中，则无法完成：同意操作绑定到发起流程的浏览器。请在已登录 PlaidCloud 的同一浏览器中重新发起授权。

## Claude Code 登录时出现 “oauth Flow is Not in Progress”

现象：在浏览器中完成授权后，将回调 URL 粘贴到 Claude Code 中，却提示没有正在进行的流程。

原因：桥接程序内存中的 OAuth 状态按端口保存，可能在 `authenticate` 与 `complete_authentication` 两次工具调用之间丢失，在远程/SSH 会话中尤为常见，因为浏览器回调无法到达 `localhost`。

解决办法：改用静态 Bearer 流程。在已登录 PlaidCloud 的浏览器中打开 `https://<your-workspace>.plaid.cloud/mcp/setup/token`，将代码片段复制到 `.mcp.json` 中，然后重启 Claude Code。

## 令牌已过期

现象：昨天还能用的工具现在返回 401 Unauthorized。

原因：静态 Bearer 令牌遵循 Keycloak 域的访问令牌有效期策略（通常为几小时到一天）。

解决办法：重新加载 `https://<your-workspace>.plaid.cloud/mcp/setup/token` 以生成新令牌，并将其粘贴到配置中。对于长时间运行的会话，建议使用 OAuth：支持 OAuth 的客户端会自动刷新令牌。

## “no `access_token` in Session”

现象：打开 `/mcp/setup/token` 时显示 “Sign-in required” 或 “No access_token in session”，但您已登录 PlaidCloud。

原因：您的会话是通过未缓存 Keycloak 令牌的登录路径建立的（不常见，但可能发生）。

解决办法：退出 PlaidCloud，然后通过标准登录页面重新登录。新会话将带有访问令牌。

## 工具缺失或目录不完整

现象：`mcp_introspect` 返回的工具比预期少，或者需要的某些工具不存在。

原因 1，作用域：工具需要特定的 PlaidCloud 作用域（例如 `analyze.workflow.write`）。如果您的账户缺少该作用域，工具将拒绝执行。运行 `mcp_introspect(name='<tool>')` 查看 `required_scopes`。请联系工作区管理员授予该作用域，或使用具备该作用域的账户执行该操作。

原因 2，版本不匹配：较旧的部署可能不包含最新文档中描述的所有工具。将 `mcp_introspect()` 返回的工具数量与当前版本的发行说明进行对比；如有需要，请求重新部署。

## 多租户：代理刚才访问的是哪个租户？

现象：配置了多个 PlaidCloud 租户，代理的响应可能来自其中任何一个。

解决办法：在提示中明确指出租户（例如“在 **dev** 租户中，列出工作流……”）。您在配置中为 MCP 服务器取的名称（例如 `plaidcloud-prod`、`plaidcloud-dev`）同时也是模型可用来区分的标识。对于高风险操作，在确实需要之前，请在连接器选择器中保持关闭生产环境。

## 速率限制与配额

PlaidCloud 的 REST 接口通过与 UI 前端相同的中间件，按每分钟请求数进行速率限制。MCP 调用共享该限制。如果代理连续发出大量 `find` 调用（例如尝试枚举所有项目、工作流和步骤），可能会触及限制。请使用分页（`cursor`、`limit`），并用 `count_only=True` 进行规模检查，而不要获取完整的结果集。

请注意，find 默认每页返回 25 行（`step_find` 为 50 行），因此枚举大型集合所需的调用次数比以前更多：进行有意的全量扫描时，请提高 `limit`，而不是按默认值逐页翻取。反过来，如果您不断触及限制，使用 `count_only=True` 和更精简的 `fields=[...]` 投影，通常意味着根本不需要全量扫描。

## 列表看起来太短，或代理说“就这些了”

现象：find 返回的行数比预期少，或者代理断定某个项目有 25 张表，而实际有 300 张。

解决办法：检查响应信封。被截断的页面会设置 `next_cursor`，find 工具还会在 `truncated` 中指出被截断的列表，这两者都表示还有更多数据可获取。`total` 始终报告完整数量，请将其与已获得的行数对比。让代理使用游标翻页，或使用更高的 `limit` 重新运行。

## 结果看起来像 `{"_fmt": "cols", ...}`

现象：工具返回了 `{"_fmt": "cols", "cols": [...], "rows": [[...]]}`，而不是预期的对象列表。

对于所有行都带有相同字段的大型结果，这是预期的形态：字段名只发送一次，而不是在每一行中重复。第 *i* 行为 `dict(zip(cols, rows[i]))`。代理在连接时会被告知这一点，无需提示即可处理；如果您在自己的代码中读取这些响应，请同时解码两种形态，因为小型和不规则的结果仍以普通对象数组形式返回。信封的其他部分不变，也不会更改任何值。请参阅 [AI 编码代理入门](/zh-cn/integrations/ai-coding-agents/getting-started/#列式结果)。

## 获取帮助

对于服务器端问题，例如身份验证失败、工具返回错误但原因不明、工具缺失，请先检查响应中的 `error` 信封。每次失败都包含 `code`、`retryable`、`message`，通常还有 `hint`。如果提示不足以解决问题，请联系 PlaidCloud 管理员，或附上请求 ID（在 `X-Request-Id` 响应标头中返回）提交支持工单。
