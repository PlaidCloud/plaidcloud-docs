---
title: 命令行
description: 使用 PlaidCloud 命令行界面自动化任务、运行脚本，并通过终端与 PlaidCloud 资源交互。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

PlaidCloud 提供 REST API，任何能够发送 HTTP 请求的应用程序都可以使用。为简化操作，`plaidcloud-rpc` Python 包会为您处理连接和请求的细节。

:::caution[JSON-RPC 已弃用]
JSON-RPC 已弃用，并将在以后的版本中移除。请使用会将调用发送到 REST API 的 `plaidcloud-rpc` 1.25.0 或更高版本，并基于 REST API 编写新的集成。请参阅[JSON-RPC 已弃用](#json-rpc-已弃用)。
:::


## 所需安装

在终端中运行以下命令：

```bash
pip install "plaidcloud-rpc>=1.25.0"
```


## 使用 SimpleRPC 对象发出请求

要使用 `plaidcloud-rpc` 包发出请求，请使用 `SimpleRPC` 对象。

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC

auth_token = "Your PlaidCloud OAuth token"  # See Obtaining an OAuth Token below
endpoint_uri = "https://<your-workspace>.plaid.cloud/json-rpc/"
rpc = SimpleRPC(auth_token, endpoint_uri)
```

实例化 `SimpleRPC` 对象后，即可向 PlaidCloud 发出请求。此示例请求一个表的元数据。

```python
table = rpc.analyze.table.table(
            project_id=project_id,
            table_id=table_id
        )
```

`SimpleRPC` 使用相同的令牌，将每个调用发送到工作区主机上 `/rest/v1/` 处的 REST API。REST API 尚未覆盖的调用，或发往仍在旧版本上运行的工作区的调用，会改用 JSON-RPC，因此同一段代码在两种情况下都能运行。调用失败时，两种情况下都会引发 `RPCError`。


## 直接调用 REST API

`call_rest` 使用与 `SimpleRPC` 相同的令牌、TLS 设置和重试机制，向任意 REST API 端点发送请求。请提供 HTTP 方法、`/rest/v1/` 下的路径，并可选择提供用于查询字符串的 `params` 和用于 JSON 请求正文的 `body`。

```python
dimensions = rpc.call_rest(
    'GET',
    'analyze/dimension/dimensions',
    params={'project_id': project_id},
)
```

它返回解码后的 JSON 响应；如果响应没有正文，则返回 `None`。任何非成功响应都会引发 `RPCError`，并以 HTTP 状态作为其 `code`。


## JSON-RPC 已弃用

JSON-RPC 已弃用，并将在以后的版本中移除。1.25.0 之前版本的 `plaidcloud-rpc` 通过 JSON-RPC 发送所有调用，因此在 JSON-RPC 移除后将无法使用。请升级到 1.25.0 或更高版本；您的 `SimpleRPC` 代码无需更改。请基于 REST API 编写新的集成。


## 有哪些可用的 API？

有许多可用的 API，几乎可以控制 PlaidCloud 的各个方面。交互式 API 参考由各 PlaidCloud 工作区自行提供：打开您的工作区，进入 API 文档菜单，即可查看实时的端点目录。


## 获取 OAuth 令牌

有关如何获取 OAuth 令牌以及如何配置系统以实现自动认证，请参阅 [OAuth 设置](/zh-cn/reference/cli/jupyter/oauth-setup/)。
