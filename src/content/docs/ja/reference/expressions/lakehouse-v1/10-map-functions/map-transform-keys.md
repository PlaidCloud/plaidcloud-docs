---
title: MAP_TRANSFORM_KEYS（Lakehouse v1）
description: MAP_TRANSFORM_KEYS — ラムダ式を使用して、マップ内の各キーに変換を適用します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-keys.md
---

ラムダ式を使用して、マップ内の各キーに変換を適用します。

## SQL Syntax

```sql
MAP_TRANSFORM_KEYS(<map>, (<key>, <value>) -> <key_transformation>)
```

## 戻り値の型

入力マップと同じ値を持ち、キーが指定したラムダ変換に従って変更されたマップを返します。

## SQL Examples

この例では、各商品IDに1,000を加算し、関連する価格はそのままで、キーが更新された新しいマップを作成します。

```sql
SELECT MAP_TRANSFORM_KEYS({101: 29.99, 102: 45.50, 103: 15.00}, (product_id, price) -> product_id + 1000) AS updated_product_ids;

┌────────────────────────────────────┐
│         updated_product_ids        │
├────────────────────────────────────┤
│ {1101:29.99,1102:45.50,1103:15.00} │
└────────────────────────────────────┘
```
