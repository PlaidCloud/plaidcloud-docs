---
title: JSON_MAP_TRANSFORM_VALUES (Lakehouse v1)
description: JSON_MAP_TRANSFORM_VALUES — JSONオブジェクトの各値に変換を適用します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-transform-values.md
---

ラムダ式を使って、JSONオブジェクトの各値に変換を適用します。

## SQL構文

```sql
JSON_MAP_TRANSFORM_VALUES(<json_object>, (<key>, <value>) -> <value_transformation>)
```

## 戻り値の型

入力のJSONオブジェクトと同じキーを持ち、値が指定したラムダ式の変換に従って変更されたJSONオブジェクトを返します。

## SQLの例

次の例では、各製品の説明に「 - Special Offer」を付加します。

```sql
SELECT JSON_MAP_TRANSFORM_VALUES('{"product1":"laptop", "product2":"phone"}'::VARIANT, (k, v) -> CONCAT(v, ' - Special Offer')) AS promo_descriptions;

┌──────────────────────────────────────────────────────────────────────────┐
│                            promo_descriptions                            │
├──────────────────────────────────────────────────────────────────────────┤
│ {"product1":"laptop - Special Offer","product2":"phone - Special Offer"} │
└──────────────────────────────────────────────────────────────────────────┘
```
