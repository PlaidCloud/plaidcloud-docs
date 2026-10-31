---
title: Oracle Essbase 连接器
description: 使用服务账户将 PlaidCloud 连接到 Oracle Essbase 21c 或 Oracle Analytics Cloud，从工作流对 Essbase 多维数据集运行实时 MDX 查询。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-essbase.md
---

## API 文档

此连接器调用 [Oracle Essbase 的 REST API](https://docs.oracle.com/en/database/other-databases/essbase/)，即 Oracle 为 Essbase 21c 和 Oracle Analytics Cloud（OAC）记录的 `grid/mdx`、应用程序、数据库和大纲端点。

## 连接对象

Oracle Essbase **21c 或更高版本**，以及 Oracle Analytics Cloud（OAC）Essbase。这些版本通过有文档记录的 REST API 提供 Essbase 服务，PlaidCloud 调用的正是该 API。**不支持**早于 REST 的本地部署 Essbase 版本——没有旧版 Java API 或网格客户端路径。

连接创建后，[Essbase：查询多维数据集](/zh-cn/reference/workflow-steps/essbase/essbase-query/)步骤会对多维数据集运行实时 MDX，并将结果网格写入表；[Essbase：读取维度](/zh-cn/reference/workflow-steps/essbase/essbase-dimension-read/)步骤会将维度大纲加载到 PlaidCloud 维度中。

## 身份验证的工作方式

连接通过 HTTP 基本身份验证，使用服务账户的用户名和密码进行验证。该账户在 Essbase 中的预配决定了它能看到和查询哪些应用程序与多维数据集，因此请仅授予它对计划查询的应用程序的读取权限，不要多给。

## 配置

| 字段 | 类型 | 说明 |
|---|---|---|
| 名称 | 文本 | 此连接的显示名称。 |
| 基础 URL | 文本 | Essbase 服务器的源，例如 `https://your-host:9001`。只输入源，不要带结尾的 `/essbase/...` 路径。 |
| 默认应用程序 | 文本 *（可选）* | 在 Essbase：查询多维数据集步骤表单中预先选择此应用程序。 |
| 用户名 | 文本 | 用于 HTTP 基本身份验证的服务账户用户。 |
| 密码 | 文本 | 服务账户密码。加密存储。 |
| 验证 SSL | 开关 | 默认开启。仅对使用自签名或其他无法验证的证书的主机关闭。 |

## 测试连接

在连接编辑器中使用**测试连接**。测试成功表示已连上 Essbase 服务器，列出服务账户可见的应用程序并报告数量——在构建查询之前，同时确认基础 URL 和凭据无误。

## 相关内容

- [Essbase：查询多维数据集](/zh-cn/reference/workflow-steps/essbase/essbase-query/) — 对多维数据集运行实时 MDX 查询，并将结果写入表。
- [Essbase：读取维度](/zh-cn/reference/workflow-steps/essbase/essbase-dimension-read/) — 将维度大纲加载到 PlaidCloud 维度中。
- [Oracle Essbase 步骤](/zh-cn/reference/workflow-steps/essbase/)
- [连接到 Oracle Essbase（指南）](/zh-cn/guides/connections/essbase/)
- [创建和管理连接](/zh-cn/guides/connections/create-connection/)
