---
title: Workday Financialsのステップ
description: Workday Financials接続を通じてWorkday Financialsとの間でデータを読み書きするワークフローステップです。RaaSレポートによるデータのインポートと、会計仕訳の転記があります。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workday-financials/index.md
---

[Workday Financials接続](/ja/guides/connections/workday-financials/)を通じて、Workday Financialsとの間でデータを読み書きするワークフローステップです。インポートステップは、お客様が用意したReport-as-a-Service（RaaS）レポートを取り込みます。転記ステップは、PlaidCloudの共有ERP書き込みパイプラインを通じて会計仕訳を転記します。

## ステップ

- [Import Workday Entityステップ](/ja/reference/workflow-steps/workday-financials/import-workday-entity/) — レポートパラメーターのフィルターを使ってRaaSレポートを取り込みます。
- [Workday Financials: Post Journal Entryステップ](/ja/reference/workflow-steps/workday-financials/workday-post/) — `Submit_Accounting_Journal` を使って会計仕訳を転記します。修正には、転記済みの反対仕訳を使用します。

## 関連項目

- [Workday Financialsコネクタ](/ja/reference/connectors/rest/workday-financials/)
- [Workday Financialsへの接続](/ja/guides/connections/workday-financials/)
- [ERP転記履歴のレビュー](/ja/guides/connections/erp-post-history/)
