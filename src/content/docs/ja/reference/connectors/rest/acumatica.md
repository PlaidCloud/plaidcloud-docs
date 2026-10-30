---
title: Acumatica RESTコネクター
description: PlaidCloudでAcumaticaのコントラクトベースREST API接続を設定し、マスターデータとトランザクションデータをインポートして、仕訳トランザクション、請求書、請求、支払を転記します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/acumatica.md
---

## APIドキュメント

Acumaticaの[コントラクトベースREST API](https://help.acumatica.com/Help?ScreenId=ShowWiki&pageid=e0dea52d-0339-4f34-a6c0-9615ce6a25c2)に、このコネクターが使用するエンドポイントとクエリオプションが記載されています。

## 認証の仕組み

この接続は**セッションベース**です。PlaidCloudは、処理の区切りとなる単位ごとに1回ログインし（ユーザー名、パスワード、会社、任意のブランチを指定して`POST <instance>/entity/auth/login`）、その単位内のすべての呼び出しで得られたセッションCookieを再利用し、完了時にログアウトします。ベアラートークンやOAuthのフローではありません。セッションはAcumaticaライセンスの同時セッション数の上限にカウントされ、トライアルや下位ティアのインスタンスでは上限が2程度に制限される場合があります。そのため、1つの接続で多数のAcumaticaステップを並列実行することは避けてください。

## 設定

| フィールド | タイプ | 説明 |
|---|---|---|
| 名前 | テキスト | この接続の表示名。 |
| インスタンスのベースURL | テキスト | AcumaticaインスタンスのURL（例：`https://yourcompany.acumatica.com`）。 |
| エンドポイント名 | テキスト | コントラクトエンドポイント名。カスタムエンドポイントを公開していない限り`Default`です。 |
| エンドポイントのバージョン | テキスト | 任意（例：`25.200.001`）。空白のままにすると、エンドポイントの最新の公開バージョンを使用します。 |
| 会社/テナント | テキスト | この接続がログインするAcumaticaの会社IDそのもの。 |
| ブランチ | テキスト | 任意。空白のままにすると、ログインユーザーのデフォルトブランチを使用します。 |
| ユーザー名 | テキスト | PlaidCloud APIユーザーのログイン名。 |
| パスワード | テキスト | PlaidCloud APIユーザーのパスワード。暗号化して保存されます。 |

## インポートできるエンティティ

**Import Acumatica Entity**ステップは、コントラクトベースの18のエンティティに対応しています。

**マスターデータと参照データ** — `account`、`subaccount`、`ledger`、`financial_period`、`branch`、`currency`、`currency_rate`、`customer`、`vendor`、`stock_item`、`warehouse`、`employee`、`tax_category`、`project`

**トランザクションデータ** — `sales_invoice`、`bill`、`sales_order`、`shipment`

各取得では、`Active Only`トグル、`Updated After`のカットオフ、エンティティごとのサーバー側フィルターを使用できます。フィールドの詳細は[Import Acumatica Entity](/ja/reference/workflow-steps/acumatica/import-acumatica-entity/)ステップを参照してください。

## ドキュメントの転記

**Acumatica Post**ステップは、PlaidCloudの共通ERP書き込みパイプラインを通じて、**JournalTransaction**、**SalesInvoice**、**Bill**、**Payment**の各ドキュメントを転記します。保留状態で作成し、リリース（非同期アクション）し、リリースを確認してからドキュメントを転記済みとして報告します。フィールドのリファレンスは[Acumatica: Post Documents](/ja/reference/workflow-steps/acumatica/acumatica-post/)ステップを、転記の手順全体は[Acumaticaへの接続](/ja/guides/connections/acumatica/)を参照してください。

## 既知の制限事項

| 制限事項 | 意味 |
|---|---|
| GIに依存する読み取りは対象外 | 試算表、総勘定元帳のトランザクション明細、手持在庫、予算、会社間データは、上記18のコントラクトベースのエンティティではなく、AcumaticaのGeneric Inquiryの背後にあります。Acumaticaでそのインクワイアリを作成し、[汎用REST接続](/ja/reference/connectors/rest/generic-rest/)で取得してください。 |
| 書き込みにネイティブの冪等性キーがない | AcumaticaのPUTベースの書き込みAPIには冪等性フィールドがありません。二重転記に対する唯一の防御策は、PlaidCloud自身の台帳による確保です。 |
| 取り消しは手動 | 無効化や取り消しのアクションが文書化されているドキュメントタイプはありません。転記済みのドキュメントはPlaidCloudから取り消せません。Acumatica上で直接訂正してください。 |
| 支払の突合フィールドがない | Acumaticaには、結果が不明確になった後に支払をPlaidCloudのリクエストと突き合わせるための、文書化されたフィールドがありません。結果が不明な支払は隔離され、手動で解決します。 |
| 明細のフィルタリングはサーバー側では行われない | `$filter`形式のフィルターはエンティティとヘッダーのフィールドには適用されますが、ドキュメントの明細ディメンション（たとえば明細レベルのコストセンター）には適用されません。取得後にワークフロー内で明細を絞り込んでください。 |
## 関連項目

- [Acumaticaへの接続（ガイド）](/ja/guides/connections/acumatica/) — 接続の作成、テスト、エンティティのインポート、バッチの転記までの手順。
- [Import Acumatica Entity](/ja/reference/workflow-steps/acumatica/import-acumatica-entity/)
- [Acumatica: Post Documents](/ja/reference/workflow-steps/acumatica/acumatica-post/)
- [ERP転記履歴の確認](/ja/guides/connections/erp-post-history/)
