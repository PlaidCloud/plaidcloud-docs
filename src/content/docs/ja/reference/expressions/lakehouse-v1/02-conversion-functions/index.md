---
title: 変換関数（Lakehouse v1）
description: "Lakehouse v1のSQL変換関数：CAST、TRY_CAST、パース、書式設定のヘルパーなど、型の間で値をキャストします。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/index.md
---

このセクションでは、PlaidCloud Lakehouseの変換関数のリファレンス情報を説明します。

## 関数

- [BUILD_BITMAP](build-bitmap/)
- [CAST, ::](cast/)
- [TO_BINARY](to-binary/)
- [TO_BITMAP](to-bitmap/)
- [TO_BOOLEAN](to-boolean/)
- [TO_FLOAT32](to-float32/)
- [TO_FLOAT64](to-float64/)
- [TO_HEX](to-hex/)
- [TO_INT16](to-int16/)
- [TO_INT32](to-int32/)
- [TO_INT64](to-int64/)
- [TO_INT8](to-int8/)
- [TO_STRING（変換、Lakehouse v1）](to-string/)
- [TO_TEXT](to-text/)
- [TO_UINT16](to-uint16/)
- [TO_UINT32](to-uint32/)
- [TO_UINT64](to-uint64/)
- [TO_UINT8](to-uint8/)
- [TO_VARCHAR](to-varchar/)
- [TO_VARIANT](to-variant/)
- [TRY_CAST](try-cast/)
- [TRY_TO_BINARY](try-to-binary/)

ある型から別の型に値を変換する際は、次の点にご注意ください。

- 浮動小数点数、10進数、または文字列を、整数または小数部を持つ10進数に変換する場合、PlaidCloud Lakehouseは値を最も近い整数に丸めます。この動作は、数値のキャスト操作の動作を制御する設定`numeric_cast_option`（デフォルトは'rounding'）によって決まります。`numeric_cast_option`を明示的に'truncating'に設定すると、PlaidCloud Lakehouseは小数部を切り捨て、端数の値を破棄します。

    ```sql
    SELECT CAST('0.6' AS DECIMAL(10, 0)), CAST(0.6 AS DECIMAL(10, 0)), CAST(1.5 AS INT);

    ┌──────────────────────────────────────────────────────────────────────────────────┐
    │ cast('0.6' as decimal(10, 0)) │ cast(0.6 as decimal(10, 0)) │ cast(1.5 as int32) │
    ├───────────────────────────────┼─────────────────────────────┼────────────────────┤
    │                             1 │                           1 │                  2 │
    └──────────────────────────────────────────────────────────────────────────────────┘

    SET numeric_cast_option = 'truncating';

    SELECT CAST('0.6' AS DECIMAL(10, 0)), CAST(0.6 AS DECIMAL(10, 0)), CAST(1.5 AS INT);

    ┌──────────────────────────────────────────────────────────────────────────────────┐
    │ cast('0.6' as decimal(10, 0)) │ cast(0.6 as decimal(10, 0)) │ cast(1.5 as int32) │
    ├───────────────────────────────┼─────────────────────────────┼────────────────────┤
    │                             0 │                           0 │                  1 │
    └──────────────────────────────────────────────────────────────────────────────────┘
    ```

    次の表は、数値のキャスト操作をまとめたもので、ソースとターゲットの数値データ型の間で可能なキャストを示しています。文字列から整数へのキャストでは、ソースの文字列に整数値が含まれている必要があるので、ご注意ください。

    | ソースタイプ    | ターゲットタイプ |
    |----------------|-------------|
    | String         | Decimal     |
    | Float          | Decimal     |
    | Decimal        | Decimal     |
    | Float          | Int         |
    | Decimal        | Int         |
    | String (Int)   | Int         |


- PlaidCloud Lakehouseには、式をさまざまな日付と時刻の形式に変換するための関数も用意されています。詳細については、[日付・時刻関数](../05-datetime-functions)を参照してください。
