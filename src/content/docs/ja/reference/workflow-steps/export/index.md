---
title: エクスポートステップ
description: プロジェクトテーブルを外部の出力先（ファイル形式、ドキュメントアカウント、外部データベース）に書き込むワークフローステップです。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/index.md
---

プロジェクトテーブルを外部の出力先（ファイル形式、ドキュメントアカウント、外部データベース）に書き込むワークフローステップです。

## ステップ

- [テーブルのアーカイブ](/ja/reference/workflow-steps/export/archive-tables/)
- [Export External Database Tables ステップ](/ja/reference/workflow-steps/export/export-external-tables/)
- [Kafkaのエクスポート](/ja/reference/workflow-steps/export/export-kafka/)
- [MongoDBのエクスポート](/ja/reference/workflow-steps/export/export-mongodb/)
- [プロジェクトアーカイブのエクスポート](/ja/reference/workflow-steps/export/export-project-archive/)
- [Export Project Table ステップ](/ja/reference/workflow-steps/export/export-project-table/)
- [Export Quandl ステップ](/ja/reference/workflow-steps/export/export-quandl/)
- [SQLのエクスポート](/ja/reference/workflow-steps/export/export-sql/)
- [Export Templated ステップ](/ja/reference/workflow-steps/export/export-templated/)
- [Export to Avro ステップ](/ja/reference/workflow-steps/export/export-to-avro/)
- [Export To CSV ステップ](/ja/reference/workflow-steps/export/export-to-csv/)
- [Export To Excel ステップ](/ja/reference/workflow-steps/export/export-to-excel/)
- [Export To Excel Sheets ステップ](/ja/reference/workflow-steps/export/export-to-excel-sheets/)
- [Export To Google Spreadsheet ステップ](/ja/reference/workflow-steps/export/export-to-google-spreadsheet/)
- [Export To HDF ステップ](/ja/reference/workflow-steps/export/export-to-hdf/)
- [Export To JSON ステップ](/ja/reference/workflow-steps/export/export-to-json/)
- [Export to ORC ステップ](/ja/reference/workflow-steps/export/export-to-orc/)
- [Export to Parquet ステップ](/ja/reference/workflow-steps/export/export-to-parquet/)
- [Export to PDF ステップ](/ja/reference/workflow-steps/export/export-to-pdf/)
- [Export To Table Archive ステップ](/ja/reference/workflow-steps/export/export-to-table-archive/)
- [Export To XML ステップ](/ja/reference/workflow-steps/export/export-to-xml/)
- [伝票を転記 ステップ](/ja/reference/workflow-steps/export/post-documents/) — テーブルのドキュメントを、設定済みの任意のERPシステムに転記します
- [空間ファイルのエクスポート](/ja/reference/workflow-steps/spatial/spatial-file-export/)
- [Publish to Tableau ステップ](/ja/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export ステップ](/ja/reference/workflow-steps/export/export-hyper/)

## 書き込まれる列

ほとんどのエクスポートステップは、データマッパーにターゲット列が一覧表示されていない場合、つまり**列**タブの右側のテーブルが空の場合、実行時点のソーステーブルのすべての列を、テーブルの列の順序で書き込みます。そのため、設定が途中のステップでも失敗せず、テーブル全体が宛先にエクスポートされます。外部の宛先に対してエクスポートを実行する前に、データマッパーを確認してください。

マッピングされた列がなく、ソーステーブルにも列がない場合、CSV、JSON、SQL、Excel、PDF、Googleスプレッドシート、Kafkaのエクスポートは何も書き込まず、警告付きで完了します。XML、Parquet、ORC、Avro、Excel Sheets ステップなど複数テーブルのエクスポートでは、そのテーブルを、テーブル名を示す警告付きでスキップします。
