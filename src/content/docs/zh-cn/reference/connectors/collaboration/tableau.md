---
title: Tableau 连接
description: 使用个人访问令牌将 PlaidCloud 连接到 Tableau Server 或 Tableau Cloud，使工作流能够发布数据源。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/collaboration/tableau.md
---

Tableau 连接保存 Tableau Server 或 Tableau Cloud 站点的地址以及个人访问令牌。[Publish to Tableau](/zh-cn/reference/workflow-steps/export/export-to-tableau/) 步骤使用它将 `.hyper` 提取发布为数据源。

## 开始之前

在 Tableau 中，为要执行发布的账户创建个人访问令牌：依次选择 **My Account Settings** 和 **Personal Access Tokens**。Tableau 显示令牌密钥时请将其复制下来，因为 Tableau 不会再次显示。该账户需要有权限将数据源发布到您要发布到的项目。

## 创建连接

1. 打开 **Analyze**，选择 **Tools → 外部数据连接**，然后选择 **+ 新建连接 → Tableau**。
2. 输入连接的名称和描述。
3. 输入连接设置：

| 字段 | 输入内容 |
| --- | --- |
| **服务器 URL** | 服务器或 Tableau Cloud pod 的地址，例如 `https://prod-useast-a.online.tableau.com`。仅有主机名时按 `https` 处理，`http` 地址会被拒绝。 |
| **站点** | 站点的内容 URL，即浏览器地址中 `#/site/` 之后的部分。对于默认站点请留空。 |
| **个人访问令牌名称** | 您在 Tableau 中为令牌指定的名称。 |
| **个人访问令牌密钥** | 令牌密钥。它以加密方式存储，重新打开连接时显示为空白。留空则保留已保存的密钥。 |

4. 选择 **创建**。

服务器必须可从互联网访问。PlaidCloud 不会连接到专用网络上的 Tableau 服务器。

## 相关内容

- [Publish to Tableau](/zh-cn/reference/workflow-steps/export/export-to-tableau/) 步骤
- [Tableau Hyper Export](/zh-cn/reference/workflow-steps/export/export-hyper/) 步骤
