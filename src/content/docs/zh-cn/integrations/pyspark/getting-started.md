---
title: PySpark 入门
description: 开始在 PlaidCloud 中使用 PySpark，在用户定义函数和 Jupyter 笔记本中进行分布式数据处理。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/pyspark/getting-started.md
---

## PySpark 文档
PySpark 的使用方式与 Pandas 类似，但支持分布式计算，且不受内存限制。PySpark 可用于 UDF 和 Jupyter 笔记本。

UDF 通过 Spark Connect 使用 Spark 集群，可使用 PySpark 的 DataFrame 和 SQL API（`pyspark.sql`）。需要 Java 与代码一同运行的 PySpark 部分无法在 UDF 中使用：无法导入 `SparkContext`、`RDD`、`pyspark.streaming` 以及 `pyspark.mllib` 中大部分基于 RDD 的 API，也无法将 Spark DataFrame 传递给 statsforecast 或 Fugue。

## Spark 集群
默认情况下，工作区未启用 Spark 集群。要激活 Spark 集群，请前往工作区管理应用并启用“Spark Compute Cluster”服务。

激活后，即可向集群提交 Spark 作业。

可通过工作区的 `spark` 子域监控集群（例如 `https://spark.my_workspace.plaid.cloud`）
