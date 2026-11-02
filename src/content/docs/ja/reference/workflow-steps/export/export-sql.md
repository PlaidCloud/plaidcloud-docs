---
title: Export to SQLステップ
description: PlaidCloud のワークフローステップから外部の SQL データベースにデータをエクスポートし、結果を下流のデータベースシステムに読み込みます。
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## 説明



PlaidCloud のプロジェクトテーブルを、CREATE TABLE 文と INSERT 文を含む SQL ファイルとしてドキュメントアカウントに書き込みます。CSV や Parquet ではなく SQL スクリプトを取り込むシステムにデータを引き渡す場合に便利です。

リモートデータベースに直接読み込む場合は、代わりに該当するデータベースのエクスポートステップまたは[Agent Remote Import](/ja/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/)を使用してください。こちらの方が高速で、中間ファイルも不要です。

## プレビュー

**ソース**タブの**プレビュー**では、ステップを実行せずにソーステーブルの最大 100 行を表示できます。テーブルの行数がそれを超える場合は、先頭の行を表示していることが示されます。ソーステーブルがまだ存在しない場合、プレビューにはプレビューするものがないと表示されます。ロックされたプロジェクトではプレビューを使用できません。

## 追加設定

**行の順序**の**行の並べ替え**（`sort_columns`）では、書き込む行をこれらのソース列で並べ替えます。最初のキーが優先され、各キーには**列**、**昇順**、**NULL 値**の設定があります。キー列を書き込む必要はありません。**NULL 値**のデフォルトは、昇順では先頭、降順では末尾です。**集計**または**重複排除**とは併用できません。

## 例


例はまだありません...
