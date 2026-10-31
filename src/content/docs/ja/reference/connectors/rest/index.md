---
title: REST接続
description: PlaidCloudをSalesforce、NetSuite、Workday、Dynamicsなど、RESTAPIを提供するクラウドベースのプラットフォームに接続します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/index.md
---

PlaidCloudは、標準的な認証パターン（OAuth、APIキー、基本認証）を使用してREST APIサービスに接続します。プロバイダーごとに、トークンフロー、スコープの扱い、ページングに独自の癖があります。以下の専用コネクターがそれらの詳細をカプセル化しているため、ユーザーが意識する必要はありません。

専用のコネクターがないRESTサービスには、ほとんどの認証およびレスポンス解析パターンに合わせて設定できる汎用RESTコネクターが用意されています。

## 汎用コネクター

- [汎用REST接続](/ja/reference/connectors/rest/generic-rest/) — 任意のHTTP APIを設定します。認証なし/基本/APIキー/ベアラー/OAuth 2.0の各認証、デフォルトヘッダー、リダイレクト処理、リクエストテストに対応しています。

## CRMと営業

- [Salesforce](/ja/reference/connectors/rest/salesforce/)
- [Dynamics](/ja/reference/connectors/rest/dynamics/) — Microsoft Dynamics 365

## 財務と会計

- [NetSuite](/ja/reference/connectors/rest/netsuite/)
- [HFM / FCCS](/ja/reference/connectors/rest/hfm-fccs/) — Oracle EPM Cloud（Financial Consolidation and Close）
- [TM1](/ja/reference/connectors/rest/tm1/) — IBM TM1 / Planning Analytics
- [Acumatica](/ja/reference/connectors/rest/acumatica/)
- [Business Central](/ja/reference/connectors/rest/business-central/)
- [Dynamics 365 Finance & Operations](/ja/reference/connectors/rest/dynamics-365-fo/)
- [Workday Financials](/ja/reference/connectors/rest/workday-financials/)
- [SAP S/4HANA Cloud](/ja/reference/connectors/rest/s4hana-cloud/)
- [QuickBooks](/ja/reference/connectors/rest/quickbooks/)
- [Xero](/ja/reference/connectors/rest/xero/)
- [Sage Intacct](/ja/reference/connectors/rest/sage-intacct/)
- [Stripe](/ja/reference/connectors/rest/stripe/)
- [Ramp](/ja/reference/connectors/rest/ramp/)

## 人事と給与

- [Workday](/ja/reference/connectors/rest/workday/)
- [Paycor](/ja/reference/connectors/rest/paycor/)
- [Gusto](/ja/reference/connectors/rest/gusto/)

## 統合プラットフォーム

- [MuleSoft](/ja/reference/connectors/rest/mulesoft/)
