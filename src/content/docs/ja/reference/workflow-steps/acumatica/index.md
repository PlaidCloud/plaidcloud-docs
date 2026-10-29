---
title: Acumaticaステップ
description: Acumatica接続を通じてAcumaticaの読み取りと書き込みを行うワークフローステップです。コントラクトベース RESTエンティティのインポートと、仕訳トランザクション、請求書、請求、支払の転記ができます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/acumatica/index.md
---

[Acumatica接続](/ja/guides/connections/acumatica/)を通じて、Acumaticaの読み取りと書き込みを行うワークフローステップです。インポートステップは、ODataを書かずにAcumaticaのコントラクトベース RESTエンティティを取得します。転記ステップは、PlaidCloudの共有ERP書き込みパイプラインを通じて、仕訳トランザクション、売上請求書、請求、支払を転記します。

## ステップ

- [Import Acumatica Entity](/ja/reference/workflow-steps/acumatica/import-acumatica-entity/) — マスターデータとトランザクションのエンティティを、サーバー側フィルターで取得します。
- [Acumatica: Post Documents](/ja/reference/workflow-steps/acumatica/acumatica-post/) — 仕訳トランザクション、売上請求書、請求、支払を転記します。

## 関連情報

- [Acumatica RESTコネクター](/ja/reference/connectors/rest/acumatica/)
- [Acumaticaへの接続](/ja/guides/connections/acumatica/)
- [ERP転記履歴の確認](/ja/guides/connections/erp-post-history/)
