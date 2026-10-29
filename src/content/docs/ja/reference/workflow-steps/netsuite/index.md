---
title: NetSuite ステップ
description: NetSuite のワークフローステップです。残高、GL明細、マスターデータ、または独自の SuiteQL クエリをインポートし、NetSuite 接続を使用して仕訳を転記します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/netsuite/index.md
---

[NetSuite 接続](/ja/guides/connections/netsuite/)を使用して NetSuite の読み取りと書き込みを行うワークフローステップです。あらかじめ用意されたインポートステップは、一般的な財務データや参照データを取得する最も簡単な方法です。接続、ターゲットテーブル、日付範囲またはレコードタイプを選択するだけで、SuiteQL を書く必要はありません。

## インポートステップ

- [NetSuite: 残高のインポート](/ja/reference/workflow-steps/netsuite/import-balances/) — 日付範囲と子会社を指定した勘定科目残高（試算表）。
- [NetSuite: GL明細のインポート](/ja/reference/workflow-steps/netsuite/import-gl-detail/) — 日付範囲と子会社を指定した総勘定元帳のトランザクション明細行。
- [NetSuite: マスターデータのインポート](/ja/reference/workflow-steps/netsuite/import-master-data/) — マスターリスト（勘定科目、子会社、部門、クラス、場所、仕入先、顧客）。
- [NetSuite: SuiteQL クエリのインポート](/ja/reference/workflow-steps/netsuite/import-suiteql-query/) — 独自の SuiteQL クエリを実行し、結果を型付きテーブルに読み込みます。日付ウィンドウとページングは自動で処理されます。

## 転記ステップ

- [Post NetSuite Journal Entry ステップ](/ja/reference/workflow-steps/netsuite/post-netsuite-journal-entry/) — ヘッダー／明細形式の仕訳を NetSuite に転記します。

## カスタム取得

あらかじめ用意されたインポートステップでは対応できないデータ（独自のクエリや、専用ステップのない NetSuite レコード）には、独自の SuiteQL を指定して [NetSuite: SuiteQL クエリのインポート](/ja/reference/workflow-steps/netsuite/import-suiteql-query/)を使用します。出発点としては、[NetSuite SuiteQL クエリの例](/ja/guides/connections/netsuite-financial-queries/)を参照してください。

## 関連項目

- [NetSuite REST コネクター](/ja/reference/connectors/rest/netsuite/)
- [NetSuite への接続](/ja/guides/connections/netsuite/)
- [NetSuite 財務データのインポート](/ja/guides/connections/import-netsuite-financials/)
