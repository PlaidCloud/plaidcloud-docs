---
title: Agent Remote Import Table into SQL Database
description: PlaidLinkエージェントを通じてPlaidCloudのテーブルデータをリモートのSQLデータベースにインポートし、ファイアウォールの内側にデータを安全にロードします。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database.md
---

## 説明



PlaidLinkエージェント経由でのみ到達できるデータベースに、PlaidCloudのプロジェクトテーブルをプッシュします。エージェントがPlaidCloudからデータを受け取り、ロードをローカルで実行します。オンプレミスの業務データベースをPlaidCloudの分析と同期させておくのに便利です。

典型的な使い方: PlaidCloudが更新された予測や配賦の結果を生成し、エージェントがそれをオンプレミスのERP、データマート、または業務レポート用データベースにロードします。


## データがエージェントに届く仕組み

バージョン1.2.33以降のPlaidLinkエージェントは、テーブルの行を1つのParquetファイルとして受け取ります。数値、日付、タイムスタンプ、真偽値は、それぞれの型のまま届きます。時刻、インターバル、JSONの列などその他の列は、テキストとして届きます。空のテキスト値は、これまでどおり、空（NULL）として届きます。

それより古いエージェントは、これまでどおり、zip圧縮されたタブ区切りファイルとして行を受け取ります。Parquetで受け取るには、[エージェントをアップグレード](/ja/reference/cli/plaidlink/upgrade/)してください。

## 例

まだ例はありません...
