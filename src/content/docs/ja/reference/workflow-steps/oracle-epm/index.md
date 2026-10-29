---
title: Oracle EPM (HFM / FCCS) ステップ
description: HFM/FCCS 接続を使用して Oracle FCCS からアドホックなデータスライスをセルフサービスで取得するワークフローステップです。ポイントオブビューを組み立てて実行し、結果をテーブルとして格納します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/index.md
---

[HFM/FCCS 接続](/ja/guides/connections/hfm-fccs/)を使用して、Oracle **FCCS**（Financial Consolidation and Close、EPM Cloud）から読み取るワークフローステップです。財務ユーザーがステップフォームでポイントオブビューを組み立てて実行すると、返されたグリッドが自動的にプロジェクトテーブルとして格納されます。HFM チームへのチケットも、連結に関する知識も不要です。

## ステップ

- [HFM/FCCS: データの読み取り（アドホック）](/ja/reference/workflow-steps/oracle-epm/hfm-fccs-read/) — ポイントオブビューの選択でデータスライスをセルフサービスで取得します。同じ取得はキャッシュされ、行レベルセキュリティに対応しており、スケジュールされた定期ロードに昇格できます。

## 関連項目

- [HFM / FCCS からの抽出（ガイド）](/ja/guides/connections/hfm-fccs/)
- [HFM / FCCS コネクター](/ja/reference/connectors/rest/hfm-fccs/)
