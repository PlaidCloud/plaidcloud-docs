---
title: Oracle Fusionステップ
description: Oracle Fusion接続を使用して Oracle Fusion Cloud の読み取りと書き込みを行うワークフローステップです。OData/BIP または FBDI 一括抽出による総勘定元帳残高と仕訳バッチのインポート、および仕訳の転記に対応します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-fusion/index.md
---

[Oracle Fusion接続](/ja/guides/connections/oracle-fusion/)を使用して Oracle Fusion Cloud の読み取りと書き込みを行うワークフローステップです。インポートステップは取得規模に応じて 2 種類あります。通常の取得には OData/BIP の直接呼び出し、大規模な取得には非同期の FBDI/BIP 一括抽出を使用します。転記ステップは、PlaidCloud 共通の ERP 書き込みパイプラインを通じて仕訳バッチを転記します。

## ステップ

- [Import Fusion Entity](/ja/reference/workflow-steps/oracle-fusion/import-fusion-entity/) — 総勘定元帳残高と仕訳バッチを、サーバー側の日付、期間、数値範囲フィルターで取得します。
- [Import Fusion Bulk Extract](/ja/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) — 同じエンティティを、大規模な取得向けの非同期 FBDI/BIP エクスポートジョブで取得します。
- [Oracle Fusion: Post Journal Entry](/ja/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) — FBDI GL インターフェースを通じて総勘定元帳の仕訳バッチを転記します。訂正には転記済みの取消仕訳を使用します。

## 関連項目

- [Oracle Fusionコネクター](/ja/reference/connectors/erp/oracle-fusion/)
- [Oracle Fusionに接続する](/ja/guides/connections/oracle-fusion/)
- [ERP転記履歴を確認する](/ja/guides/connections/erp-post-history/)
