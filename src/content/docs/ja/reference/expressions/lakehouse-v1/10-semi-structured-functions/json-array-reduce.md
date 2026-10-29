---
title: JSON_ARRAY_REDUCE (Lakehouse v1)
description: JSON_ARRAY_REDUCE — 指定したラムダ式を適用して、JSON配列を1つの値に縮約します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-reduce.md
---

指定したラムダ式を適用して、JSON配列を1つの値に縮約します。ラムダ式の詳細については、ラムダ式を参照してください。

## SQL構文

```sql
JSON_ARRAY_REDUCE(<json_array>, <lambda_expression>)
```

## SQLの例

次の例では、配列のすべての要素を掛け合わせます（2 _ 3 _ 4）。

```sql
SELECT JSON_ARRAY_REDUCE(
    [2, 3, 4]::JSON,
    (acc, d) -> acc::Int * d::Int
);

-[ RECORD 1 ]-----------------------------------
json_array_reduce([2, 3, 4]::VARIANT, (acc, d) -> acc::Int32 * d::Int32): 24
```
