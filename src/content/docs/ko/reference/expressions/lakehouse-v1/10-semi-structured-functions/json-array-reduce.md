---
title: JSON_ARRAY_REDUCE (Lakehouse v1)
description: JSON_ARRAY_REDUCE — 지정한 람다 식을 적용하여 JSON 배열을 단일 값으로 축소합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-reduce.md
---

지정한 람다 식을 적용하여 JSON 배열을 단일 값으로 축소합니다. 람다 식에 대한 자세한 내용은 람다 식을 참조하십시오.

## SQL Syntax

```sql
JSON_ARRAY_REDUCE(<json_array>, <lambda_expression>)
```

## SQL Examples

이 예제는 배열의 모든 요소를 곱합니다(2 _ 3 _ 4).

```sql
SELECT JSON_ARRAY_REDUCE(
    [2, 3, 4]::JSON,
    (acc, d) -> acc::Int * d::Int
);

-[ RECORD 1 ]-----------------------------------
json_array_reduce([2, 3, 4]::VARIANT, (acc, d) -> acc::Int32 * d::Int32): 24
```
