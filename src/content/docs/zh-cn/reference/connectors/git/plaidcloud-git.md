---
title: PlaidCloud Git 连接器
description: 将 Panel 应用、Dash 应用或工作流连接到 PlaidCloud Git（内置的托管 Git 服务）中的仓库，无需配置服务器 URL 或凭据。
sidebar:
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/git/plaidcloud-git.md
---

**PlaidCloud Git** 是内置于工作区的托管 Git 服务。PlaidCloud Git 连接可将 Panel 或 Dash 部署，或者工作流，指向您的某个仓库。由于该服务是托管的，因此**无需服务器 URL、用户名或令牌**：PlaidCloud 会提供主机并代您进行身份验证。

有关通过此类连接部署应用的完整操作步骤，请参阅[从 PlaidCloud Git 部署 Panel 应用](/zh-cn/guides/panel-apps/deploy-from-git/)或[从 PlaidCloud Git 部署 Dash 应用](/zh-cn/guides/dash-apps/deploy-from-git/)。如需创建仓库并推送代码，请参阅 [PlaidCloud Git 指南](/zh-cn/guides/git/)。

## 配置

在 **Tools > Connections** 中，点击**新建连接**并选择 **PlaidCloud Git**。该表单不包含外部 Git 提供商所显示的身份验证、SSL 和 SSH 部分（凭据由平台派生），只保留连接的标识、用法和仓库目标。

### 标识

| 字段 | 类型 | 说明 |
|---|---|---|
| 账户名称 | 文本 | 此连接的显示名称。 |
| 备注 | 文本 | 关于该连接用途的可选说明。 |

### 仓库

| 字段 | 类型 | 说明 |
|---|---|---|
| 仓库 | 选择器 | 要使用的仓库。点击**刷新**可列出工作区中的仓库（例如 `apps` 或 `udfs`），然后选择其一。 |
| 默认分支 | 选择器 | 要读取的分支，从所选仓库的分支中选择。 |
| 起始路径 | 选择器 | 可选。浏览所选仓库并选择一个文件夹，将所有文件查找限定在某个子目录内。 |

**用法**（`Active` / `Read Only`）和 **安全模型**（工作区中哪些人可以使用该连接）属于标准连接设置，请参阅[连接指南](/zh-cn/guides/connections/plaidcloud-git/)和[创建和管理连接](/zh-cn/guides/connections/create-connection/)。

## 常见用途

- 从工作区的 `apps` 仓库部署 [HoloViz Panel 应用](/zh-cn/guides/panel-apps/deploy-from-git/)或 [Plotly Dash 应用](/zh-cn/guides/dash-apps/deploy-from-git/)。
- 获取存放在 PlaidCloud Git 中的用户定义函数、配置或模板化文件。

## 相关内容

- [PlaidCloud Git 连接](/zh-cn/guides/connections/plaidcloud-git/) — 创建连接的任务指南，包含用法和安全模型
- [从 PlaidCloud Git 部署 Panel 应用](/zh-cn/guides/panel-apps/deploy-from-git/) — 从仓库到已部署应用的完整路径
- [从 PlaidCloud Git 部署 Dash 应用](/zh-cn/guides/dash-apps/deploy-from-git/) — Plotly Dash 应用的相同路径
- [PlaidCloud Git 指南](/zh-cn/guides/git/) — 仓库、议题、拉取请求等
- [Git 仓库连接](/zh-cn/reference/connectors/git/) — 外部 Git 提供商（GitHub、GitLab 等）
