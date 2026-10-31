---
title: OAuth 令牌
description: 为 PlaidCloud API 访问设置 OAuth 令牌，用于认证 Jupyter 笔记本、CLI 工具和自定义应用连接。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/oauth-setup.md
---

PlaidCloud 使用标准的 JSON-RPC 请求，任何能够发送此类请求的应用程序都可以使用它。请求通过 OAuth 令牌保护。


## 获取 OAuth 令牌

OAuth 令牌在 PlaidCloud 应用中生成。要查看分配给您的当前 OAuth 令牌列表并生成新令牌，请前往 `Analyze > Tools > Registered Systems`。

进入后，可以查看现有令牌，也可以选择创建新令牌。

## 下载 OAuth PlaidCloud 配置文件
选择“Register a New System”。

填写表单，并记下您输入的名称，以便在列表中找到它。

创建完成后，点击齿轮图标打开已注册系统的记录。这将显示配置文件的文本。

注意：请务必从顶部的下拉列表中选择要使用此连接的项目。项目唯一标识符会被添加到配置中。

将此文本复制到系统上的 plaid.conf 文件中，并将其放在 .plaid 目录中。

## 在本地创建配置文件
在笔记本目录的上一级目录，或计划使用命令行交互的位置的上一级目录中，创建一个名为 `.plaid` 的目录。

在 `.plaid` 目录中创建一个名为 `plaid.conf` 的文件，并将上面复制的内容粘贴到该文件中。保存文件后，即可使用 PlaidCloud 实用工具和 rpc 方法进行连接。


## 高级用法

虽然将 `.plaid` 文件夹放在靠近使用位置的地方比较方便，但它实际上可以放在上级目录树中的任意位置。初始化过程会沿目录树向上查找，直到找到 `.plaid` 目录。

如果有多个操作都需要访问，但无法共存于同一个较低层级的目录结构中，将 `.plaid` 目录放在更高的层级可能会很有用。


## 可选的路径设置
如果使用本地 Jupyter 笔记本安装或在命令行中操作，可以借助辅助工具导出数据、Excel 文件和其他数据，也可以将本地数据读入 DataFrame。为此需要一个 paths.yaml 文件。

除 `plaid.conf` 文件外，还需创建一个 `paths.yaml` 文件。`paths.yaml` 应与 `.plaid` 目录中的 `plaid.conf` 文件位于同一级。它应包含以下路径信息：

```yaml
paths:
 PROJECT_ROOT: '{WORKING_USER}/Documents'
 LOCAL_STORAGE: '{PROJECT_ROOT}/local_storage'
 DEBUG: '{PROJECT_ROOT}/local_storage'
 REPORTS: '{PROJECT_ROOT}/reports'
 
 create: []
 local: {}
```
