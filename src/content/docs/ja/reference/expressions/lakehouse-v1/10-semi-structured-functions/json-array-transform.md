---
title: JSON_ARRAY_TRANSFORM (Lakehouse v1)
description: JSON_ARRAY_TRANSFORM — 指定した変換用のラムダ式を使って、JSON配列の各要素を変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-transform.md
---

指定した変換用のラムダ式を使って、JSON配列の各要素を変換します。ラムダ式の詳細については、ラムダ式を参照してください。

## SQL構文

```sql
JSON_ARRAY_TRANSFORM(<json_array>, <lambda_expression>)
```

## エイリアス

- [JSON_ARRAY_APPLY](../json-array-apply)
- [JSON_ARRAY_MAP](../json-array-map)

## 戻り値の型

JSON配列。

## SQLの例

次の例では、配列内の各数値要素に10を掛けて、元の配列を `[10, 20, 30, 40]` に変換します。

```sql
SELECT JSON_ARRAY_TRANSFORM(
    [1, 2, 3, 4]::JSON,
    data -> (data::Int * 10)
);

-[ RECORD 1 ]-----------------------------------
json_array_transform([1, 2, 3, 4]::VARIANT, data -> data::Int32 * 10): [10,20,30,40]
```
