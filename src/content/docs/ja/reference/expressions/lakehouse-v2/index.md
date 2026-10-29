---
title: Lakehouse v2 の式
description: StarRocks 4.1 の SQL 関数をベースにした Lakehouse v2 の式です。SQLAlchemy での記述方法も掲載しています。
sidebar:
  label: Lakehouse v2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/index.md
---

Lakehouse v2 は [StarRocks](https://www.starrocks.io/) 4.1 をベースに構築されています。以下の各関数について、このサイトでは PlaidCloud 向けの構文と例を提供しています。すべてのエッジケースと引数のバリエーションを含む公式のリファレンスについては、**[StarRocks SQL function reference](https://docs.starrocks.io/docs/sql-reference/sql-functions/)** を参照してください。

## 集計関数

- [集計関数](./01-aggregate-functions) — 合計、平均、件数などの集計値を計算します
- [パーセンタイル関数](./15-percentile-functions) — パーセンタイル値を計算し、パーセンタイルの状態を管理します

## スカラー関数

- [配列関数](./02-array-functions) — 配列に対する操作を行います
- [バイナリ関数](./03-binary-functions) — バイナリと文字列の形式を相互に変換します
- [ビット関数](./04-bit-functions) — ビット演算を行います
- [ビットマップ関数](./05-bitmap-functions) — ビットマップの操作と加工を行います
- [条件関数](./06-condition-functions) — 条件ロジックと CASE 文を実装します
- [暗号関数](./07-cryptographic-functions) — データの暗号化、復号、ハッシュ化を行います
- [日付と時刻の関数](./08-date-time-functions) — 日付と時刻の操作と書式設定を行います
- [ディクショナリ関数](./09-dictionary-functions) — ディクショナリテーブルから値を検索します
- [ハッシュ関数](./10-hash-functions) — MurmurHash と xxHash を使ってハッシュ値を生成します
- [JSON 関数](./11-json-functions) — JSON データの作成、クエリ、操作を行います
- [マップ関数](./12-map-functions) — マップデータ構造の作成と操作を行います
- [数学関数](./13-math-functions) — 計算と数値演算を行います
- [パターンマッチング関数](./14-pattern-matching-functions) — LIKE と正規表現で文字列を照合します
- [スカラー関数（HLL）](./16-scalar-functions) — HyperLogLog によるカーディナリティ推定関数です
- [空間関数](./17-spatial-functions) — 地理空間データの処理と操作を行います
- [文字列関数](./18-string-functions) — 文字列の操作とテキスト処理を行います
- [構造体関数](./19-struct-functions) — 構造体データ型の作成と操作を行います
- [バリアント関数](./22-variant-functions) — VARIANT データ型のクエリと確認を行います

## テーブル関数

- [テーブル関数](./20-table-functions) — 結果を表形式で返します

## ユーティリティ関数とメタ関数

- [ユーティリティ関数](./21-utility-functions) — システム情報とセッションユーティリティにアクセスします
- [メタ関数](./23-meta-functions) — マテリアライズドビュー、メモリ、診断情報を確認します

## Lakehouse の管理

- [Lakehouse の管理](./lakehouse-management/) — クエリの実行、カタログの参照、ウェアハウスの管理、コンピュートの監視を行います
