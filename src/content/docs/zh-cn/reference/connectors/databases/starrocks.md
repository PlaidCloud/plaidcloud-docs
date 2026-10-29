---
title: StarRocks
description: 在 PlaidCloud 中配置 StarRocks 数据库连接，对大规模数据集运行高性能分析查询。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/starrocks.md
---

**StarRocks** 是支撑 PlaidCloud Lakehouse v2 的高性能分析型数据库（对应 StarRocks 4.1）。使用此连接器可查询独立部署的 StarRocks；对于产品内置的 Lakehouse，则无需此连接器。

## 上游文档
[StarRocks 文档](https://docs.starrocks.io/docs/introduction/StarRocks_intro/)。

## 设置

此连接器使用供应商特有的身份验证流程，可直接在工作区的**连接**屏幕中配置。显示的配置字段取决于租户管理员为该集成预配的凭据。

最新的设置细节请参阅上游 [starrocks 文档](https://docs.starrocks.io/)。

如果需要帮助为租户设置此连接器，请联系您的客户团队——连接器专用的凭据、环境 URL 以及任何必需的预配置，通常需要与 PlaidCloud 支持团队协调。
