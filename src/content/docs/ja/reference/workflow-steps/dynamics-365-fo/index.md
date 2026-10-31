---
title: D365 F&Oステップ
description: D365 F&O接続を通じてDynamics 365 Finance & Operationsの読み取りと書き込みを行うワークフローステップです。OData/DMFエンティティのインポートと、仕訳の転記ができます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dynamics-365-fo/index.md
---

[D365 F&O接続](/ja/guides/connections/dynamics-365-fo/)を通じて、Dynamics 365 Finance & Operations（D365 F&O）の読み取りと書き込みを行うワークフローステップです。インポートステップは、ODataを記述することなく、ODataエンティティまたは一括DMF抽出を取得します。転記ステップは、PlaidCloud共有のERP書き込みパイプラインを通じて、総勘定元帳の仕訳を転記します。

## ステップ

- [Import D365 F&O Entityステップ](/ja/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) — マスターデータと仕訳ヘッダーを、ODataまたはDMF一括モードで、サーバー側フィルター付きで取得します。
- [D365 F&O: Post Journal Entryステップ](/ja/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) — 総勘定元帳の仕訳を転記します。訂正には、転記済みの反対仕訳を使用します。

## 関連項目

- [Dynamics 365 F&O RESTコネクタ](/ja/reference/connectors/rest/dynamics-365-fo/)
- [Dynamics 365 Finance & Operationsに接続する](/ja/guides/connections/dynamics-365-fo/)
- [ERP転記履歴を確認する](/ja/guides/connections/erp-post-history/)
