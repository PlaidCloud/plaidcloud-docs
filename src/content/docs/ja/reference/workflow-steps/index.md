---
title: ワークフローステップ
description: PlaidCloudのすべてのワークフローステップタイプ：インポート、エクスポート、変換、配賦、ディメンション、ドキュメント、通知など。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/index.md
---

ワークフローステップは、PlaidCloudの自動化を構成する基本要素です。各ステップは1つの操作（CSVのインポート、2つのテーブルの結合、通知の送信など）を実行し、ステップを組み合わせたワークフローは、順次、並列、条件付き、またはループで実行されます。

## カテゴリ

### データ移動

- [インポート](/ja/reference/workflow-steps/import/) — CSV、Excel、Parquet、JSON、ORC、Delta Lake、SQL、BigQuery、MongoDB、Kafka、SPSS、Singerソースなどからデータを取り込みます
- [エクスポート](/ja/reference/workflow-steps/export/) — CSV、XML、SQL、Excel、Googleスプレッドシート、Parquet、ORC、MongoDB、Kafka、テーブルアーカイブなどにデータを書き出します

### テーブル変換

- [テーブル](/ja/reference/workflow-steps/tables/) — 結合、ユニオン、フィルター、ルックアップ、ピボット、メルト、対象を絞った更新、ソーステーブルからの行アクセスの付与、特定時点への復元
- [共通操作](/ja/reference/workflow-steps/common/) — 共有されるデータマッピングとフィルターのパターン

### 地理空間

- [地理空間](/ja/reference/workflow-steps/spatial/) — 空間ファイルのインポートとエクスポート、バッファー、照合、計測、再投影、ジオメトリの構築。Alteryxの空間ツールを完全にカバーします

### モデリング

- [配賦](/ja/reference/workflow-steps/allocation/) — ドライバーベースの配分、分割配賦、ルールベースのタグ付け
- [ディメンション](/ja/reference/workflow-steps/dimensions/) — 階層のロード、並べ替え、クリア、エクスポート、管理
- [最適化](/ja/reference/workflow-steps/optimization/) — 線形および混合整数ソルバーのステップ
- [機械学習](/ja/reference/workflow-steps/machine-learning/) — XGBoostやKNIMEの学習器を含むモデルの学習と、それらによるテーブルのスコアリング

### ドキュメントとファイル

- [ドキュメント](/ja/reference/workflow-steps/document/) — ファイル操作、ディレクトリ一覧、暗号化、PDF操作、画像処理、エンコード変換、Excelセルの更新
- [テキストとドキュメント](/ja/reference/workflow-steps/text-documents/) — PDFテキスト抽出、画像OCR、ブロブの読み取りと書き込み、センチメント、トピックモデリング、ワードクラウド

### コミュニケーション

- [通知](/ja/reference/workflow-steps/notifications/) — メール、Slack、Teams、SMS、Webhook、Twitter、ログ
- [レポート](/ja/reference/workflow-steps/reports/) — RMLテンプレートから単一または一括のPDFレポートを生成します

### ワークフロー制御

- [ワークフロー制御](/ja/reference/workflow-steps/workflow-control/) — 変数、ループ、サブワークフロー、マクロ、エラー処理、行数アサーション
- [一般](/ja/reference/workflow-steps/general/) — LLMステップ、パス、待機、ユーザー定義変換、リモートPythonの実行、Alteryx実行
- [パッケージ化マクロ](/ja/reference/workflow-steps/macros/) — Alteryxのパッケージ化マクロに相当するもの：Create Samples、DateTime Now、Heat Map、Pie Wedge Trade Area

### エンタープライズ統合

- [エージェント](/ja/reference/workflow-steps/agent/) — オンプレミスリソース向けのPlaidLinkエージェント操作
- [NetSuite](/ja/reference/workflow-steps/netsuite/) — 残高、GL明細、マスターデータ、または独自の[SuiteQLクエリ](/ja/reference/workflow-steps/netsuite/import-suiteql-query/)をインポートし、仕訳をNetSuiteに転記します
- [Acumatica](/ja/reference/workflow-steps/acumatica/) — マスターエンティティとトランザクションエンティティをインポートし、仕訳トランザクション、請求書、買掛金、支払を転記します
- [Business Central](/ja/reference/workflow-steps/business-central/) — ODataエンティティをインポートし、総勘定元帳の仕訳明細を転記します
- [Xero](/ja/reference/workflow-steps/xero/) — Accounting APIエンティティをインポートし、手動仕訳、請求書、買掛金、支払、クレジットノートを転記します
- [Dynamics 365 F&O](/ja/reference/workflow-steps/dynamics-365-fo/) — OData/DMFエンティティをインポートし、仕訳を転記します
- [Oracle Fusion](/ja/reference/workflow-steps/oracle-fusion/) — GL残高と仕訳バッチをインポートし、FBDI経由で仕訳を転記します
- [Oracle EPM（HFM / FCCS）](/ja/reference/workflow-steps/oracle-epm/) — POV（視点）ピッカーを使って、Oracle FCCSからアドホックなデータスライスをセルフサービスで取得します。定期的なスケジュールロードも任意で設定できます
- [Oracle Essbase](/ja/reference/workflow-steps/essbase/) — キューブに対してライブMDXクエリを実行するか、ディメンションアウトラインをPlaidCloudディメンションとしてロードします。クラウドダイレクト
- [IBM TM1 / Planning Analytics](/ja/reference/workflow-steps/ibm-planning-analytics/) — 保存済みビューまたはMDXでキューブを読み取るか、ディメンション階層を読み取ります。クラウドダイレクト、またはオンプレミスのエージェント経由
- [Anaplan](/ja/reference/workflow-steps/anaplan/) — 保存済みビューの読み取り、既存のエクスポートアクションの実行、1つ以上のリストのPlaidCloudディメンションへのロード。クラウドダイレクト、読み取り専用
- [OneStream](/ja/reference/workflow-steps/onestream/) — データアダプターを連結メンバーごとに1回の呼び出しでテーブルに読み取ります。読み取り専用
- [Workday Financials](/ja/reference/workflow-steps/workday-financials/) — RaaSレポートをインポートし、会計仕訳を転記します
- [Salesforce](/ja/reference/workflow-steps/salesforce/) — 組織から読み取ったオブジェクトとフィールドの一覧に基づき、標準またはカスタムのCRMオブジェクトをBulk API 2.0でプロジェクトのテーブルに抽出します
- [Sage Intacct](/ja/reference/workflow-steps/sage-intacct/) — 残高、買掛金請求書、アドホッククエリ、GL/ディメンションオブジェクトをインポートし、仕訳を転記します
- [SAP S/4HANA Cloud](/ja/reference/workflow-steps/s4hana-cloud/) — ODataで試算表と仕訳明細をインポートし、SOAP経由で仕訳を転記します
- [SAP](/ja/reference/workflow-steps/sap/) — SAP ECC / S/4HANAのRFC呼び出し
- [SAP-PCM](/ja/reference/workflow-steps/sap-pcm/) — SAP Profitability and Cost Managementモデルの制御
