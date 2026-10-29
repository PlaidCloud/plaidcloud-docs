---
title: Export to ORC ステップ
description: PlaidCloud のプロジェクトテーブルを、選択した圧縮コーデックによる列指向の Apache ORC ファイルとして、ドキュメントアカウントにエクスポートします。
sidebar:
  order: 13.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-orc.md
---

## 説明

プロジェクトテーブルを [Apache ORC](https://orc.apache.org/) ファイルとして、テーブルごとに 1 つのファイルでドキュメントアカウントに書き込みます。ORC は Hive、Spark、ほとんどのクラウドデータプラットフォームで読み取れる列指向の形式で、スキーマはファイルに含まれます。[ORC のインポート](/ja/reference/workflow-steps/import/import-orc/)と組み合わせて使用します。

ステップのフォームには、ターゲットファイル、プレフィックス、圧縮、ファイルが存在する場合の動作を指定する **ファイルパラメーター** ページと、エクスポートするテーブルを一覧にして、テーブルごとにテーブルデータの選択とデータフィルターを設定する **パラメーターを記録** ページがあります。[移行された KNIME ワークフロー](/ja/guides/workflows/migrate-knime-workflows/)では、ORC の書き込みにこのステップが使用されます。

## 設定

* **ターゲットファイル**（`output_file`）— ファイルの書き込み先となるドキュメントアカウントとフォルダーです。
* **ターゲットファイルのプレフィックス**（`file_name`）— ファイルのプレフィックスです。各テーブルは `<prefix><table name>.orc` として書き込まれます。
* **圧縮オプション**（`compression`）— ファイル内で使用される ORC コーデックです。**Snappy**、**zlib**、**gzip**（`zlib` として書き込まれます）、**Zstandard**、**LZ4** から選択します。**なし** を選ぶと、ファイルは非圧縮で書き込まれます。
* **パラメーターを記録**（`frames`）— エクスポートするテーブルです。各フレームには独自のテーブル設定があります。フレーム内ではなくステップの先頭に置いたテーブルレベルの設定は読み取られません。
  * `id` — 警告に表示されるテーブルのラベルです。
  * `source` — エクスポートするプロジェクトテーブルです。各ファイルの名前はこのテーブルから付けられます。
  * `source_columns` と `target_columns` — 読み取る列と書き込む列です。名前の変更、型、列ごとの集計も指定できます。
  * `source_where` — ソースの行に対するフィルターです。
  * `aggregate` と `aggregation_type` — 行を集計します。`aggregation_type` は、独自の集計を設定していない列に適用される集計方法です。
  * `having` — 集計後の行に対するフィルターです。
  * `distinct` — 重複を除いた行のみを書き込みます。
  * `use_target_slicer`、`limit_target_start`、`limit_target_end` — 結果の開始位置から終了位置までの行のみを書き込みます。
  * `sort_columns` — AI アシスタントまたは REST API で設定し、書き込む行を指定したソース列の順に並べ替えます。最初のキーが優先され、各キーは `{source, ascending, nulls}` です。キー列は書き込まれる列でなくてもかまいません。`nulls` のデフォルトは、昇順では `first`、降順では `last` です。`aggregate` または `distinct` と併用することはできません。
* **ファイルが存在する場合** の **すでに存在するファイル**（`if_exists`）— **上書きする**（`overwrite`、デフォルト）は、すでにあるファイルを置き換えます。**何も書き込まずにステップを失敗させる**（`fail`）は、書き込もうとするファイルがすでに存在する場合に、何も書き込まずにステップを停止します。

## 関連項目

- [エクスポートステップ](/ja/reference/workflow-steps/export/)
- [ORC のインポート](/ja/reference/workflow-steps/import/import-orc/)
- [Export to Parquet ステップ](/ja/reference/workflow-steps/export/export-to-parquet/)
