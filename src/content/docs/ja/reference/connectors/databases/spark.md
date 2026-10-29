---
title: Apache Spark
description: PlaidCloudでApache Sparkデータベース接続を設定し、分散クエリを実行してビッグデータをワークフローに統合します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/spark.md
---

**Apache Spark**は、大規模なデータセットに対するETLでよく使われる分散コンピュートエンジンです。このコネクタを使うと、Spark SQLエンドポイント（通常はSpark Thrift Server）経由でデータを読み書きできます。Databricksが管理するSparkには、[Azure Databricks](../azure-databricks/)コネクタを使用することをおすすめします。

## 上流のドキュメント
[Apache Sparkのドキュメント](https://spark.apache.org/documentation.html)。

[Apacheプロジェクト](https://spark.apache.org/)。

## セットアップ

このコネクタはベンダー固有の認証フローを使用し、ワークスペースの**接続**画面から直接構成します。表示される構成フィールドは、テナント管理者がこの連携のために用意した資格情報によって異なります。

最新のセットアップの詳細については、上流の[Sparkのドキュメント](https://spark.apache.org/docs/latest/)を参照してください。

テナントでこのコネクタを設定する際にサポートが必要な場合は、アカウントチームにお問い合わせください。コネクタ固有の資格情報、環境のURL、必要な事前プロビジョニングは、通常、PlaidCloudサポートとの調整が必要です。
