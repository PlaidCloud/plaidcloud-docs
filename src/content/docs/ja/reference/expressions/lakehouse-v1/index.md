---
title: Lakehouse v1の式
description: Databend SQL関数に基づくLakehouse v1の式。SQLAlchemyのリファレンスでは func. プレフィックスを使用します。
sidebar:
  label: Lakehouse v1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/index.md
---

Lakehouse v1は、[Databend](https://databend.com/) SQLエンジンをベースに構築されています。以下の各関数について、このサイトではPlaidCloud向けの構文と例を提供しています。エッジケースや引数のバリエーションをすべて網羅した正式なアップストリームのリファレンスについては、**[DatabendのSQL関数リファレンス](https://docs.databend.com/sql/sql-functions/)** を参照してください。

## スカラー関数

- [配列関数](./00-array-functions) — 配列に対する操作を実行します
- [ビット演算式関数](./01-bitmap-functions) — ビット演算と操作を実行します
- [条件式関数](./03-conditional-functions) — 条件ロジックとCASE文を実装します
- [コンテキスト関数](./15-context-functions) — 現在のSQL実行コンテキストに関する情報を提供します
- [変換関数](./02-conversion-functions) — データ型の変換と値のキャストを行います
- [日付・時刻関数](./05-datetime-functions) — 日付と時刻の操作と書式設定を行います
- [地理空間関数](./09-geo-functions) — 地理空間データを処理および操作します
- [ジオメトリ関数](./09-geometry-functions) — 地理空間のジオメトリデータを処理および操作します
- [インターバル関数](./05-interval-functions) — 時間間隔を作成および操作します
- [マップ関数](./10-map-functions) — マップデータ構造を作成および操作します
- [数値関数](./04-numeric-functions) — 計算と数値演算を実行します
- [検索関数](./10-search-functions) — 式を使用して値を検索します
- [半構造化・構造化データ関数](./10-semi-structured-functions) — JSONなどの構造化データ形式を扱います
- [文字列関数](./06-string-functions) — 文字列を操作し、正規表現による処理を実行します

## 集計関数

- [集計関数](./07-aggregate-functions) — 合計、平均、件数などの集計値を計算します
- [ウィンドウ関数](./08-window-functions) — 指定した行の範囲に対する集計計算を提供します

## AI関数

- [AI関数](./11-ai-functions) — AIと機械学習の機能を活用します

## 特殊関数

- [ハッシュ関数](./12-hash-functions) — データのセキュリティや比較のためのハッシュ値を生成します
- [IPアドレス関数](./14-ip-address-functions) — IPアドレスデータを操作および分析します
- [UUID関数](./13-uuid-functions) — UUIDを生成および操作します

## システム関数とテーブル関数

- [シーケンス関数](./18-sequence-functions) — 連続した値を生成します
- [システム関数](./16-system-functions) — システムレベルの情報にアクセスし、制御操作を実行します
- [テーブル関数](./17-table-functions) — 結果を表形式で返します

## その他の関数

- [ディクショナリ関数](./19-dictionary-functions) — ディクショナリデータ構造を扱います
- [その他の各種関数](./20-other-functions) — その他のさまざまな関数をまとめたものです
- [テスト関数](./19-test-functions) — テスト目的で使用する関数です
