---
title: MAP_TRANSFORM_VALUES（Lakehouse v1）
description: MAP_TRANSFORM_VALUES — ラムダ式を使用して、マップ内の各値に変換を適用します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-values.md
---

ラムダ式を使用して、マップ内の各値に変換を適用します。

## SQL Syntax

```sql
MAP_TRANSFORM_VALUES(<map>, (<key>, <value>) -> <value_transformation>)
```

## 戻り値の型

入力マップと同じキーを持ち、値が指定したラムダ変換に従って変更されたマップを返します。

## SQL Examples

この例では、各商品の価格を10%引き下げ、商品ID（キー）はそのままにします。

```sql
SELECT MAP_TRANSFORM_VALUES({101: 100.0, 102: 150.0, 103: 200.0}, (product_id, price) -> price * 0.9) AS discounted_prices;

┌───────────────────────────────────┐
│         discounted_prices         │
├───────────────────────────────────┤
│ {101:90.00,102:135.00,103:180.00} │
└───────────────────────────────────┘
```
