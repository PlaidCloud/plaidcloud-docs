---
title: PySparkを使い始める
description: PlaidCloudでPySparkを使い、ユーザー定義関数とJupyterノートブック内で分散データ処理を行う方法を説明します。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/pyspark/getting-started.md
---

## PySparkドキュメント
PySparkの使い方はPandasに似ていますが、分散コンピューティングが可能で、RAMに制約されません。PySparkは、UDFとJupyterノートブックの両方で利用できます。

UDFは、PySparkのDataFrameおよびSQL API（`pyspark.sql`）を使い、Spark Connect経由でSparkクラスターを利用します。コードと並行してJavaを実行する必要があるPySparkの機能は、UDFでは使用できません。`SparkContext`、`RDD`、`pyspark.streaming`、およびRDDベースの `pyspark.mllib` APIのほとんどはインポートできず、SparkのDataFrameをstatsforecastやFugueに渡すこともできません。

## Sparkクラスター
デフォルトでは、ワークスペースでSparkクラスターは有効になっていません。Sparkクラスターを有効にするには、ワークスペース管理アプリで「Spark Compute Cluster」サービスを有効にします。

有効にすると、Sparkジョブをクラスターに送信できるようになります。

クラスターは、ワークスペースの `spark` サブドメイン（例：`https://spark.my_workspace.plaid.cloud`）で監視できます。
