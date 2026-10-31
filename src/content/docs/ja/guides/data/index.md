---
title: データ管理 - 表形式データ
description: テーブル、ビュー、あらゆる規模のデータ処理に対応する高性能な Lakehouse エンジンを使って、PlaidCloud で表形式データを管理します。
sidebar:
  label: 概要
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/index.md
---

PlaidCloud のデータレイヤーは、**テーブル**（行と列からなる構造化データ）と**ビュー**（テーブルに対する保存済みクエリ）を中心に構築されています。どちらもプロジェクト内に存在し、Lakehouse エンジンによって動作します。このエンジンは、小さな参照テーブルから数十億行規模の分析データセットまで、設定を変更することなく拡張できます。

## このセクションの内容

- [テーブルとビュー](/ja/guides/data/tables-views/) - それぞれの概要、使い分け、相互の関係
- [テーブルエクスプローラー](/ja/guides/data/table-explorer/) - プロジェクト内のテーブルを参照して確認します
- [Currency データ型](/ja/guides/data/currency-data-type/) - 金額の値に使う、正確で半角の列データ型と、Numeric よりもこちらを選ぶべき場面
- [Vector データ型](/ja/guides/data/vector-data-type/) - 事前に計算した埋め込みをプロジェクトのテーブルに保存し、想定する幅を宣言して、最も近い行を検索します
- [テーブルのスナップショット](/ja/guides/data/table-snapshots/) - スナップショットの履歴を参照し、過去のスナップショット時点のデータを表示して、テーブルを巻き戻しまたは復元します
- [データの公開](/ja/guides/data/publish/) - プロジェクトのテーブルをダッシュボード、BI ツール、下流のシステムで利用できるようにし、パフォーマンスに関するガイダンスを確認します
- [大規模な履歴テーブルから最新のレコードを選択する](/ja/guides/data/selecting-latest-record-in-large-history-table/) - パフォーマンスを考慮した解決方法がある、よくあるパターン
- [ジオコーディング API](/ja/guides/data/geocoding-api/) - Google または Mapbox のジオコーディング連携を PlaidCloud の REST ジオコーディングエンドポイントに移行します
- [ドライブタイムルーティング API](/ja/guides/data/drive-time-routing-api/) - オプトインのプレビュー：REST による、ドライブタイムの等時間圏と、ドライブタイム順の最寄り検索

## データの入手元

テーブルには通常、**ワークフロー**がデータを入力します。ワークフローは、データのインポート、変換、結果の書き戻しを行う自動化されたパイプラインです。ワークフローの作り方は[ワークフロー](/ja/guides/workflows/)を、使用できるすべてのステップの種類は[ワークフローステップのリファレンス](/ja/reference/workflow-steps/)を参照してください。

外部システムをデータソースとして接続する方法については、[接続（ガイド）](/ja/guides/connections/)と[コネクター（リファレンス）](/ja/reference/connectors/)を参照してください。

## 関連情報

- [コンセプト](/ja/get-started/concepts/) - テーブルがワークフロー、ディメンション、より広いデータモデルとどのように関係するか
- [プロジェクト](/ja/guides/projects/) - テーブルはプロジェクトが所有します。テーブルはプロジェクトの外には存在しません
- [ダッシュボード](/ja/guides/dashboards/) - 公開されたテーブルを可視化に利用します
