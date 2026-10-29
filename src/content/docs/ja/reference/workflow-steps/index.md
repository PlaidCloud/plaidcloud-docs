---
title: ワークフローステップ
description: PlaidCloudのすべてのワークフローステップの種類（インポート、エクスポート、変換、配賦、ディメンション、ドキュメント、通知など）です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/index.md
---

ワークフローステップは、PlaidCloudによる自動化の構成要素です。各ステップは1つの操作（CSVのインポート、2つのテーブルの結合、通知の送信など）を実行し、ステップを組み合わせたワークフローは、順次、並列、条件付き、またはループで実行されます。

## カテゴリー

### データの移動

- [インポート](/ja/reference/workflow-steps/import/) — CSV、Excel、Parquet、JSON、ORC、Delta Lake、SQL、BigQuery、MongoDB、Kafka、SPSS、Singerソースなどからデータを取り込みます
- [エクスポート](/ja/reference/workflow-steps/export/) — CSV、XML、SQL、Excel、Googleスプレッドシート、Parquet、ORC、MongoDB、Kafka、テーブルアーカイブなどにデータを書き出します

### テーブルの変換

- [テーブル](/ja/reference/workflow-steps/tables/) — 結合、ユニオン、フィルター、ルックアップ、ピボット、メルト、対象を絞った更新、ソーステーブルからの行アクセスの付与、特定時点への復元
- [共通の操作](/ja/reference/workflow-steps/common/) — 共通のデータマッピングとフィルターのパターン

### 地理空間

- [地理空間](/ja/reference/workflow-steps/spatial/) — 空間ファイルのインポートとエクスポート、バッファー、照合、計測、再投影、ジオメトリの構築。Alteryxの空間ツールを完全にカバーしています

### モデリング

- [配賦](/ja/reference/workflow-steps/allocation/) — ドライバーベースの按分、分割配賦、ルールベースのタグ付け
- [ディメンション](/ja/reference/workflow-steps/dimensions/) — 階層のロード、並べ替え、クリア、エクスポート、管理
- [最適化](/ja/reference/workflow-steps/optimization/) — 線形および混合整数のソルバーステップ
- [機械学習](/ja/reference/workflow-steps/machine-learning/) — XGBoostやKNIMEの学習器を含むモデルの学習と、それらによるテーブルのスコアリング

### ドキュメントとファイル

- [ドキュメント](/ja/reference/workflow-steps/document/) — ファイル操作、ディレクトリ一覧、暗号化、PDF操作、画像処理、エンコーディング変換、Excelセルの更新
- [テキストとドキュメント](/ja/reference/workflow-steps/text-documents/) — PDFのテキスト抽出、画像OCR、BLOBの読み取りと書き込み、感情分析、トピックモデリング、ワードクラウド

### コミュニケーション

- [通知](/ja/reference/workflow-steps/notifications/) — メール、Slack、Teams、SMS、Webhook、Twitter、ログ
- [レポート](/ja/reference/workflow-steps/reports/) — RMLテンプレートから、単一または一括のPDFレポートを生成します

### ワークフロー制御

- [ワークフロー制御](/ja/reference/workflow-steps/workflow-control/) — 変数、ループ、サブワークフロー、マクロ、エラー処理、行数アサーション
- [一般](/ja/reference/workflow-steps/general/) — LLMステップ、Pass、待機、User Defined Transform、Run Remote Python、Alteryx実行
- [パッケージ化マクロ](/ja/reference/workflow-steps/macros/) — Alteryxのパッケージ化マクロに相当するもの: Create Samples、DateTime Now、Heat Map、Pie Wedge Trade Area

### エンタープライズ連携

- [エージェント](/ja/reference/workflow-steps/agent/) — オンプレミスのリソース向けのPlaidLinkエージェント操作
- [NetSuite](/ja/reference/workflow-steps/netsuite/) — 残高、GL明細、マスターデータ、または独自の[SuiteQLクエリ](/ja/reference/workflow-steps/netsuite/import-suiteql-query/)をインポートし、NetSuiteに仕訳を転記します
- [Acumatica](/ja/reference/workflow-steps/acumatica/) — マスターおよびトランザクションのエンティティをインポートし、仕訳トランザクション、請求書、買掛金請求書、支払を転記します
- [Business Central](/ja/reference/workflow-steps/business-central/) — ODataエンティティをインポートし、総勘定元帳の仕訳明細行を転記します
- [Xero](/ja/reference/workflow-steps/xero/) — Accounting APIのエンティティをインポートし、手動仕訳、請求書、買掛金請求書、支払、クレジットノートを転記します
- [Dynamics 365 F&O](/ja/reference/workflow-steps/dynamics-365-fo/) — OData/DMFエンティティをインポートし、仕訳を転記します
- [Oracle Fusion](/ja/reference/workflow-steps/oracle-fusion/) — GL残高と仕訳バッチをインポートし、FBDIを通じて仕訳を転記します
- [Oracle EPM (HFM / FCCS)](/ja/reference/workflow-steps/oracle-epm/) — POVピッカーを使って、Oracle FCCSからアドホックなデータスライスをセルフサービスで取得します。オプションで定期的なスケジュールロードも可能です
- [Oracle Essbase](/ja/reference/workflow-steps/essbase/) — キューブに対してライブのMDXクエリを実行するか、ディメンションのアウトラインをPlaidCloudのディメンションとしてロードします。クラウド直接接続です
- [IBM TM1 / Planning Analytics](/ja/reference/workflow-steps/ibm-planning-analytics/) — 保存済みビューまたはMDXでキューブを読み取るか、ディメンション階層を読み取ります。クラウド直接接続、またはオンプレミスのエージェント経由です
- [Anaplan](/ja/reference/workflow-steps/anaplan/) — 保存済みビューの読み取り、既存のエクスポートアクションの実行、1つ以上のリストのPlaidCloudディメンションへのロードを行います。クラウド直接接続の読み取り専用です
- [Workday Financials](/ja/reference/workflow-steps/workday-financials/) — RaaSレポートをインポートし、会計仕訳を転記します
- [Salesforce](/ja/reference/workflow-steps/salesforce/) — Bulk API 2.0を介して、標準またはカスタムのCRMオブジェクトをプロジェクトのテーブルに抽出します。オブジェクトとフィールドのリストは組織から読み取られます
- [Sage Intacct](/ja/reference/workflow-steps/sage-intacct/) — 残高、買掛金請求書、アドホッククエリ、GL/ディメンションオブジェクトをインポートし、仕訳を転記します
- [SAP S/4HANA Cloud](/ja/reference/workflow-steps/s4hana-cloud/) — ODataを介して試算表と仕訳明細をインポートし、SOAPを介して仕訳を転記します
- [SAP](/ja/reference/workflow-steps/sap/) — SAP ECC / S/4HANAのRFC呼び出し
- [SAP-PCM](/ja/reference/workflow-steps/sap-pcm/) — SAP Profitability and Cost Managementモデルの制御
