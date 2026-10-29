---
title: Export to SQLステップ
description: PlaidCloudのワークフローステップで外部のSQLデータベースにデータをエクスポートし、結果を下流のデータベースシステムに読み込みます。
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## 説明



PlaidCloudのプロジェクトテーブルを、CREATE TABLE文とINSERT文を含むSQLファイルとして、ドキュメントアカウントに書き込みます。CSVやParquetではなく、SQLスクリプトを取り込むシステムにデータを引き渡す場合に便利です。

リモートデータベースに直接読み込む場合は、代わりに、該当するデータベースのエクスポートステップ、または[Agent Remote Import](/ja/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/)を使用してください。これらのほうが高速で、中間ファイルも不要です。

## 追加設定

**行の順序**の**行の並べ替え**（`sort_columns`）では、書き込まれる行を、これらのソース列で並べ替えます。最初のキーが優先され、それぞれに**列**、**昇順**、**NULL 値**の設定があります。キー列は書き込まなくてもかまいません。**NULL 値**は、昇順では先頭、降順では末尾がデフォルトです。**集計**または**重複排除**とは併用できません。

## 例


例はまだありません...
