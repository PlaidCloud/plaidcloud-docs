---
title: SAP S/4HANA Cloud RESTコネクター
description: PlaidCloudでSAP S/4HANA Cloud Public Edition接続を設定し、ODataで試算表と仕訳明細のデータをインポートして、SOAPで仕訳を転記します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/s4hana-cloud.md
---

## APIドキュメント

SAP API Business Hubにある、SAP S/4HANA Cloudの[Trial Balance API（`API_OPLACCTGDOCITEMCUBE_SRV`）](https://api.sap.com/)と[Journal Entry Item - Basic API（`API_JOURNALENTRYITEMBASIC_SRV`）](https://api.sap.com/)に、このコネクターが使用するODataエンドポイントが記載されています。また、Communication Arrangementを通じて公開されるSOAPの仕訳一括作成サービスも使用します。

## 認証の仕組み

この接続は、**OAuth2クライアント資格情報**を使用してアプリケーションとして認証します。Communication ArrangementのクライアントIDとシークレットを、テナントのOAuth2トークンエンドポイントでアクセストークンに交換します。対話型のサインインはありません。

## 設定

| フィールド | タイプ | 説明 |
|---|---|---|
| 名前 | テキスト | この接続の表示名。 |
| ホスト | テキスト | S/4HANA Cloudテナントのホスト（例：`https://yourorg.s4hana.ondemand.com`）。 |
| トークンURL | テキスト | Communication ArrangementのOAuth2トークンエンドポイント。 |
| クライアントID | テキスト | Communication ArrangementのOAuth2クライアントID。 |
| クライアントシークレット | テキスト | Communication ArrangementのOAuth2クライアントシークレット。暗号化して保存されます。 |

## インポートできるエンティティ

**Import S/4HANA Entity**ステップは、`trial_balance`（`API_OPLACCTGDOCITEMCUBE_SRV`経由の、集計された期末の総勘定元帳勘定科目残高）と`journal_entry_items`（`API_JOURNALENTRYITEMBASIC_SRV`経由の、転記済みの仕訳明細行）の2つのエンティティに対応しています。どちらも`CompanyCode`、`GLAccount`、`CostCenter`、`ProfitCenter`、`FiscalYear`、`FiscalPeriod`、`Ledger`に対するサーバー側フィルターに対応しており、`PostingDate`、`FiscalYear`、`FiscalPeriod`では`ge`/`le`の範囲の境界を指定できます。フィールドの詳細は[Import S/4HANA Entity](/ja/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/)ステップを参照してください。

## 仕訳の転記

**S/4HANA: Post Journal Entry**ステップは、PlaidCloudの共通ERP書き込みパイプラインを通じて総勘定元帳の仕訳を転記します。S/4HANA Cloudの`JournalEntryBulkCreateRequest_In` SOAPサービスで送信し、`JournalEntryBulkCreateConfirmation_Out`の確認をポーリングし、確認してから仕訳を転記済みとして報告します。訂正では、元の仕訳を編集するのではなく、借方と貸方を入れ替えた新しい取消仕訳を転記します。フィールドのリファレンスは[S/4HANA: Post Journal Entry](/ja/reference/workflow-steps/s4hana-cloud/s4hana-post/)ステップを、転記の手順全体は[SAP S/4HANA Cloudへの接続](/ja/guides/connections/s4hana-cloud/)を参照してください。

## 既知の制限事項

| 制限事項 | 意味 |
|---|---|
| 確認の待ち時間 | SOAPの一括作成サービスはリクエストを非同期で処理するため、同じサイズの同期ODataによる書き込みよりもかなり遅くなります。 |
| フィルターできるフィールドはCommunication Scenarioによって異なる | お使いのCommunication Scenarioで公開されていないコストオブジェクトやディメンションは、サーバー側でフィルターできません。取得後にワークフロー内で絞り込んでください。 |
## 関連項目

- [SAP S/4HANA Cloudへの接続（ガイド）](/ja/guides/connections/s4hana-cloud/) — 接続の作成、テスト、エンティティのインポート、仕訳の転記までの手順。
- [Import S/4HANA Entity](/ja/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/)
- [S/4HANA: Post Journal Entry](/ja/reference/workflow-steps/s4hana-cloud/s4hana-post/)
- [ERP転記履歴の確認](/ja/guides/connections/erp-post-history/)
- [SAP ECC / S/4HANAコネクター](/ja/reference/connectors/erp/sap-s4/) — オンプレミスまたはプライベートクラウドのS/4HANA向けの、RFC/エージェントベースの別のコネクター。
