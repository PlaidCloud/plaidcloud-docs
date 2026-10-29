---
title: Apache Spark
description: 在 PlaidCloud 中设置 Apache Spark 数据库连接，以运行分布式查询并将大数据集成到工作流中。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/spark.md
---

**Apache Spark** 是常用于大型数据集 ETL 的分布式计算引擎。使用此连接器可通过 Spark SQL 端点（通常是 Spark Thrift Server）读写数据。对于 Databricks 托管的 Spark，建议改用 [Azure Databricks](../azure-databricks/) 连接器。

## 上游文档
[Apache Spark 文档](https://spark.apache.org/documentation.html)。

[Apache 项目](https://spark.apache.org/)。

## 设置

此连接器使用供应商特有的身份验证流程，可直接在工作区的**连接**屏幕中配置。显示的配置字段取决于租户管理员为该集成预配的凭据。

最新的设置细节请参阅上游 [spark 文档](https://spark.apache.org/docs/latest/)。

如果需要帮助为租户设置此连接器，请联系您的客户团队——连接器专用的凭据、环境 URL 以及任何必需的预配置，通常需要与 PlaidCloud 支持团队协调。
