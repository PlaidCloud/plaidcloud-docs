---
title: 命令行
description: 使用 PlaidCloud 命令行界面自动化任务、运行脚本，并通过终端与 PlaidCloud 资源交互。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

PlaidCloud 使用标准的 JSON-RPC 请求，任何能够发送此类请求的应用程序都可以使用它。


为简化连接和调用 API 的过程，我们提供了一个 Python 包。


## 所需安装

在终端中运行以下命令：

```bash
pip install plaidcloud-rpc
```


## 使用 SimpleRPC 对象发出请求

要使用 `plaidcloud-rpc` 包发出请求，请使用 `SimpleRPC` 对象。

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC  
  
auth_token = "Your PlaidCloud Auth Token" # See Obtaining Token below  
endpoint_uri = "plaidcloud.com" # or plaidcloud.net  
rpc = SimpleRPC(auth_token, endpoint_uri)
```

创建 `SimpleRPC` 对象后，即可向 PlaidCloud 发出 RPC 请求。以下示例请求一张表的元数据。

```python
table = rpc.analyze.table.table(  
            project_id=project_id,  
            table_id=table_id  
        )
```

## 有哪些可用的 API？

有许多可用的 API，几乎可以控制 PlaidCloud 的各个方面。交互式 API 参考由各 PlaidCloud 工作区自行提供：打开您的工作区，进入 API 文档菜单，即可查看实时的端点目录。


## 获取 OAuth 令牌

有关如何获取 OAuth 令牌以及如何配置系统以实现自动认证，请参阅 [OAuth 设置](/zh-cn/reference/cli/jupyter/oauth-setup/)。
