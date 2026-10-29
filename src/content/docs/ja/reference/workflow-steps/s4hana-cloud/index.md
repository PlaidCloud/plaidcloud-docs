---
title: SAP S/4HANA Cloudステップ
description: S/4HANA Cloud接続を使用して SAP S/4HANA Cloud Public Edition の読み取りと書き込みを行うワークフローステップです。試算表と仕訳明細のインポート、および仕訳の転記に対応します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/s4hana-cloud/index.md
---

[S/4HANA Cloud接続](/ja/guides/connections/s4hana-cloud/)を使用して SAP S/4HANA Cloud Public Edition の読み取りと書き込みを行うワークフローステップです。インポートステップは、OData を記述することなく試算表または仕訳明細データを取得します。転記ステップは、PlaidCloud 共通の ERP 書き込みパイプラインを通じて仕訳を転記します。

## ステップ

- [Import S/4HANA Entity](/ja/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/) — 試算表と仕訳明細データを、サーバー側のフィルターで取得します。
- [S/4HANA: Post Journal Entry](/ja/reference/workflow-steps/s4hana-cloud/s4hana-post/) — SOAP 経由で仕訳を転記します。訂正には転記済みの取消仕訳を使用します。

## 関連項目

- [SAP S/4HANA Cloud RESTコネクター](/ja/reference/connectors/rest/s4hana-cloud/)
- [SAP S/4HANA Cloudに接続する](/ja/guides/connections/s4hana-cloud/)
- [ERP転記履歴を確認する](/ja/guides/connections/erp-post-history/)
