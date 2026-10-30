---
title: データおよびサービスコネクター
description: PlaidCloudを、データベース、ERP、REST API、クラウドストレージ、Gitリポジトリなどの外部データソースやサービスに接続します。
sidebar:
  label: コネクター
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/index.md
---

PlaidCloudは、専用のコネクターを通じて外部のデータソースやサービスに接続します。各コネクターは、1つのプロバイダーファミリーの認証、プロトコル、データ形式の仕様を処理します。

## カテゴリー

### データベースとデータレイク

リレーショナルデータベース、クラウドウェアハウス、クエリエンジン、レイクハウスフォーマット。

- [データベース](/ja/reference/connectors/databases/) — PostgreSQL、MySQL、SQL Server、Oracle、Snowflake、Redshift、BigQuery、Databricks、MongoDB、Kafka、ほか15以上
- [オープンテーブル](/ja/reference/connectors/open-tables/) — Apache Iceberg、Delta Lake、Hudi、Hiveのオープンテーブルフォーマット

### クラウドサービスとSaaSサービス

- [REST](/ja/reference/connectors/rest/) — Salesforce、NetSuite、Workday、QuickBooks、Stripe、Dynamicsなど
- [ERPシステム](/ja/reference/connectors/erp/) — SAP ECC / S/4HANA、Oracle EBS/Fusion、Infor、JD Edwards
- [クラウドサービス](/ja/reference/connectors/cloud-services/) — サードパーティのデータサービス
- [Google](/ja/reference/connectors/google/) — BigQuery、Googleスプレッドシート
- [コラボレーション](/ja/reference/connectors/collaboration/) — Slack、Microsoft Teams、Tableau
- [Singerソース](/ja/reference/connectors/singer-sources/) — 130以上のSingerタップソース：Stripe、GitHub、HubSpot、データベースなど

### 開発とソース管理

- [Gitプロバイダー](/ja/reference/connectors/git/) — PlaidCloud Git（マネージド、組み込み）、およびGitHub、GitLab、Bitbucket、Azure Repos、CodeCommit

## 関連項目

- [接続ガイド](/ja/guides/connections/) — 接続の作成と管理を行うためのタスク指向の手順
- [ワークフローステップのリファレンス](/ja/reference/workflow-steps/) — 設定した接続で何ができるか
