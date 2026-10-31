---
title: JSON_ARRAY_FILTER (Lakehouse v1)
description: JSON_ARRAY_FILTER — 指定したラムダ式に基づいて、JSON配列の要素をフィルターします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-filter.md
---

指定したラムダ式に基づいてJSON配列の要素をフィルターし、条件を満たす要素だけを返します。ラムダ式の詳細については、ラムダ式を参照してください。

## SQL構文

```sql
JSON_ARRAY_FILTER(<json_array>, <lambda_expression>)
```

## 戻り値の型

JSON配列。

## SQLの例

次の例では、配列をフィルターして文字 `a` で始まる文字列だけを返し、`["apple", "avocado"]` が得られます。

```sql
SELECT JSON_ARRAY_FILTER(
    ['apple', 'banana', 'avocado', 'grape']::JSON,
    d -> d::String LIKE 'a%'
);

-[ RECORD 1 ]-----------------------------------
json_array_filter(['apple', 'banana', 'avocado', 'grape']::VARIANT, d -> d::STRING LIKE 'a%'): ["apple","avocado"]
```
