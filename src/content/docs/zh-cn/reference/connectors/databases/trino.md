---
title: Trino
description: 在 PlaidCloud 中设置 Trino 分布式查询引擎连接，以跨多个数据源运行联合查询。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/trino.md
---

**Trino**（前身为 PrestoSQL）是常用于数据湖的分布式 SQL 查询引擎。使用此连接器可从 PlaidCloud 工作流查询 Trino 部署。身份验证使用 HTTP 基本身份验证或 JWT；所指定的目录和模式决定查询访问的底层数据源。

## 上游文档
[Trino 文档](https://trino.io/docs/current/index.html)。

## 设置

此连接器使用供应商特有的身份验证流程，可直接在工作区的**连接**屏幕中配置。显示的配置字段取决于租户管理员为该集成预配的凭据。

最新的设置细节请参阅上游 [trino 文档](https://trino.io/docs/current/)。

如果需要帮助为租户设置此连接器，请联系您的客户团队——连接器专用的凭据、环境 URL 以及任何必需的预配置，通常需要与 PlaidCloud 支持团队协调。
