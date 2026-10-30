---
title: Xero ステップ
description: Xero接続を使用して Xero の読み取りと書き込みを行うワークフローステップです。Accounting API のエンティティをインポートし、手動仕訳、請求書、請求、支払、クレジットノートを転記します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/xero/index.md
---

[Xero接続](/ja/guides/connections/xero/)を使用して Xero の読み取りと書き込みを行うワークフローステップです。インポートステップは、クエリを作成せずに Xero の Accounting API のエンティティを取得します。転記ステップは、PlaidCloudの共有 ERP 書き込みパイプラインを通じて、手動仕訳、請求書、請求、支払、クレジットノートを転記します。

## ステップ

- [Xero: エンティティのインポート](/ja/reference/workflow-steps/xero/import-xero-entity/) — 勘定科目、取引先、請求書、クレジットノート、支払、手動仕訳、銀行取引、品目、トラッキングカテゴリ、税率、通貨。
- [Xero: ドキュメントの転記](/ja/reference/workflow-steps/xero/xero-post/) — 手動仕訳、請求書、請求、支払、クレジットノートを転記します。

## 関連項目

- [Xero REST コネクタ](/ja/reference/connectors/rest/xero/)
- [Xeroに接続](/ja/guides/connections/xero/)
- [ERP転記履歴の確認](/ja/guides/connections/erp-post-history/)
