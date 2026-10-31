---
title: Business Centralステップ
description: Business Central接続を通じてMicrosoft Dynamics 365 Business Centralの読み取りと書き込みを行うワークフローステップです。ODataエンティティのインポートと、総勘定元帳仕訳明細の転記ができます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/business-central/index.md
---

[Business Central接続](/ja/guides/connections/business-central/)を通じてBusiness Centralの読み取りと書き込みを行うワークフローステップです。インポートステップは、クエリを記述せずにBusiness Centralの標準的なOData v2.0エンティティを取得します。転記ステップは、PlaidCloudの共有ERP書き込みパイプラインを通じて総勘定元帳仕訳明細を転記します。

## ステップ

- [Import Business Central Entity](/ja/reference/workflow-steps/business-central/import-business-central-entity/)ステップ — 勘定科目、元帳エントリ、顧客、仕入先、品目、仕訳を、サーバー側フィルター付きで取得します。
- [Business Central: Post General Journal Lines](/ja/reference/workflow-steps/business-central/business-central-post/) — 既存の仕訳バッチに明細を追加し、そのバッチを転記します。

## 関連項目

- [Business Central RESTコネクター](/ja/reference/connectors/rest/business-central/)
- [Business Centralへの接続](/ja/guides/connections/business-central/)
- [ERP転記履歴の確認](/ja/guides/connections/erp-post-history/)
