---
title: インポートステップ
description: 外部ソースのデータをプロジェクトのテーブルに取り込むワークフローステップです。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/index.md
---

外部ソースのデータをプロジェクトのテーブルに取り込むワークフローステップです。

ファイルのインポートでは、実行前に、ターゲットテーブルを読み込むクエリが検査されます。型付き列に対する単純なSQL文以外を含むクエリは、ターゲットテーブルが作成、置換、読み込みされる前に拒否されるため、テーブルは元の状態のまま保たれます。

ソースファイルが存在しなくてもエラーにはなりません。インポートはパスを示す警告を出し、ターゲットテーブルを宣言済みの列を持つ空の状態のまま残すため、後続のステップは0行を読み取ります。これは、CSV、Excel、JSON、固定幅、YXDB、dBASE、ORC、Avro、Parquet、XML、Db2抽出のインポートに適用されます。タグ付きのXMLインポートでは、フィールドを宣言しているタグごとにのみ空のテーブルが作成されます。アーカイブとAccessのインポートも警告を出しますが、列を宣言しないため、テーブルは作成されません。ドキュメント検索でファイルを見つけるアーカイブのインポートでは、ファイルが存在しない場合の警告は出ません。

ステップの実行前でも同様です。ファイルのインポートのマッピングでの**取り込み**や、REST APIまたはAIアシスタントによるファイルの列の読み取りは、ファイルが存在しない場合や空の場合、エラーではなく、パスを示す警告とともに*取り込む列がありません*（APIでは空の列リスト）と応答します。存在しないファイルを、ドキュメントから新しいテーブルまたはステップにインポートしても何も作成されず、そのファイルは**スキップ**としてマークされ、パスを示す警告が表示されます。

## ステップ

- [Accessのインポート](/ja/reference/workflow-steps/import/import-access/)
- [Alteryx YXDBのインポート](/ja/reference/workflow-steps/import/import-alteryx-yxdb/)
- [アーカイブのインポート](/ja/reference/workflow-steps/import/import-archive/)
- [Avroのインポート](/ja/reference/workflow-steps/import/import-avro/)
- [CSVのインポート](/ja/reference/workflow-steps/import/import-csv/)
- [Delta Lake のインポート](/ja/reference/workflow-steps/import/import-delta/)
- [DB2抽出のインポート](/ja/reference/workflow-steps/import/import-db2-extract/)
- [Import dBASE ステップ](/ja/reference/workflow-steps/import/import-dbf/)
- [Excelのインポート](/ja/reference/workflow-steps/import/import-excel/)
- [Import Delimited ステップ](/ja/reference/workflow-steps/import/import-delimited/)
- [外部データベーステーブルのインポート](/ja/reference/workflow-steps/import/import-external-database-tables/)
- [固定幅のインポート](/ja/reference/workflow-steps/import/import-fixed-width/)
- [Import Google Bigquery ステップ](/ja/reference/workflow-steps/import/import-google-bigquery/)
- [Googleスプレッドシートのインポート](/ja/reference/workflow-steps/import/import-google-spreadsheet/)
- [Import HDF ステップ](/ja/reference/workflow-steps/import/import-hdf/)
- [JSONのインポート](/ja/reference/workflow-steps/import/import-json/)
- [Kafkaのインポート](/ja/reference/workflow-steps/import/import-kafka/)
- [Mondayのインポート](/ja/reference/workflow-steps/import/import-monday/)
- [MongoDBのインポート](/ja/reference/workflow-steps/import/import-mongodb/)
- [ORC のインポート](/ja/reference/workflow-steps/import/import-orc/)
- [Parquetのインポート](/ja/reference/workflow-steps/import/import-parquet/)
- [Import Project Table ステップ](/ja/reference/workflow-steps/import/import-project-table/)
- [Import Quandl ステップ](/ja/reference/workflow-steps/import/import-quandl/)
- [Import Singer Source ステップ](/ja/reference/workflow-steps/import/import-singer/)
- [Import SPSS ステップ](/ja/reference/workflow-steps/import/import-spss/)
- [SQLのインポート](/ja/reference/workflow-steps/import/import-sql/)
- [Import Stata ステップ](/ja/reference/workflow-steps/import/import-stata/)
- [XMLのインポート](/ja/reference/workflow-steps/import/import-xml/)
- [テーブルの復元](/ja/reference/workflow-steps/import/restore-tables/)
