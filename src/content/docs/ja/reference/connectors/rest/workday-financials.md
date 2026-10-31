---
title: Workday Financialsコネクタ
description: PlaidCloudで、統合システムユーザーを使用してWorkday Financialsへの接続を設定し、RaaSレポートによるデータのインポートと、SOAPによる仕訳の転記を行います。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday-financials.md
---

## APIドキュメント

このコネクタが使用するインターフェースについては、Workdayの[SOAP Webサービス](https://community.workday.com/sites/default/files/file-hosting/productionapi/)と[Report-as-a-Service（RaaS）](https://doc.workday.com/)のドキュメントを参照してください。

## 認証の仕組み

この接続は、**統合システムユーザー（ISU）** で認証します。ISUは、システム間の連携用に用意されたWorkdayのユーザータイプで、このコネクタに必要なアクセス権（読み取りにはレポートへのアクセス、転記にはSubmit Accounting Journalビジネスプロセス）だけを付与する統合システムセキュリティグループによって保護されます。リクエストにはISUのユーザー名とパスワードが付与されます。対話型のサインインはありません。

## 設定

| フィールド | 種類 | 説明 |
|---|---|---|
| 名前 | テキスト | この接続の表示名です。 |
| テナントホスト | テキスト | WorkdayのホストのURLです。例：`wd5-impl.workday.com`。 |
| テナント名 | テキスト | Workdayのテナント名です。 |
| ISUユーザー名 | テキスト | 統合システムユーザーのユーザー名です。 |
| ISUパスワード | テキスト | 統合システムユーザーのパスワードです。暗号化して保存されます。 |

## データのインポート

Workday Financialsには、あらかじめ用意された固定のエンティティはありません。代わりに、Import Workday Entityステップが、Workdayで作成し、Webサービスアクセスを有効にして公開した**Report-as-a-Service（RaaS）レポート**を呼び出します。そのレポートのURLを指定します。このステップでは、`company`、`ledger`、`period`、`accounting_date`（範囲）、`ledger_account`（範囲）、`cost_center`でフィルターでき、それぞれレポートのパラメーターとしてそのまま渡されます。そのため、一致するプロンプトがレポートに定義されている場合にのみ、フィルターが機能します。フィールドの詳細は、[Import Workday Entityステップ](/ja/reference/workflow-steps/workday-financials/import-workday-entity/)を参照してください。

## 仕訳の転記

Workday Financials: Post Journal Entryステップは、PlaidCloudの共通ERP書き込みパイプラインを通じて会計仕訳を転記します。WorkdayのSOAPオペレーション`Submit_Accounting_Journal`を使用し、仕訳のビジネスプロセスのステータスが終了状態になるまでポーリングしてから、転記済みと報告します。訂正の場合は、元の仕訳を編集せず、借方と貸方を入れ替えた新しい取消仕訳を転記します。フィールドの詳細は[Workday Financials: Post Journal Entryステップ](/ja/reference/workflow-steps/workday-financials/workday-post/)を、転記の手順全体は[Workday Financialsに接続する](/ja/guides/connections/workday-financials/)を参照してください。

## 既知の制限事項

| 制限事項 | 内容 |
|---|---|
| インポートの形状はRaaSレポートに依存する | PlaidCloudには、Workday Financials用にあらかじめ用意されたエンティティはありません。レポートのフィールド、プロンプト、アクセス制御はすべてWorkday側にあります。Workday側でレポートを変更すると、PlaidCloud側で何も変更しなくても、インポートの形状が変わることがあります。 |
| ビジネスプロセスの承認により遅延が生じる | Submit Accounting Journalビジネスプロセスに承認ステップがある場合、承認ステップを経由する仕訳は、Workdayで承認されるまで`pending`のままになります。終了状態のポーリングは、その承認を待ちます。 |

## 関連情報

- [Workday Financialsに接続する（ガイド）](/ja/guides/connections/workday-financials/)：接続の作成、テスト、レポートのインポート、仕訳の転記を、順を追って説明します。
- [Import Workday Entityステップ](/ja/reference/workflow-steps/workday-financials/import-workday-entity/)
- [Workday Financials: Post Journal Entryステップ](/ja/reference/workflow-steps/workday-financials/workday-post/)
- [ERP転記履歴の確認](/ja/guides/connections/erp-post-history/)
- [Workday RESTコネクタ](/ja/reference/connectors/rest/workday/)：人事／給与のRESTデータ向けの、別の汎用Workdayコネクタです。
