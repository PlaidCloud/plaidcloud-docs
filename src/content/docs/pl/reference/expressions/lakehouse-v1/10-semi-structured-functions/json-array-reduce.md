---
title: JSON_ARRAY_REDUCE (Lakehouse v1)
description: JSON_ARRAY_REDUCE — redukuje tablicę JSON do pojedynczej wartości przez zastosowanie określonego wyrażenia Lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-reduce.md
---

Redukuje tablicę JSON do pojedynczej wartości przez zastosowanie określonego wyrażenia Lambda. Więcej informacji o wyrażeniach Lambda znajdziesz w sekcji Wyrażenia Lambda.

## Składnia SQL

```sql
JSON_ARRAY_REDUCE(<json_array>, <lambda_expression>)
```

## Przykłady SQL

Ten przykład mnoży wszystkie elementy tablicy (2 _ 3 _ 4):

```sql
SELECT JSON_ARRAY_REDUCE(
    [2, 3, 4]::JSON,
    (acc, d) -> acc::Int * d::Int
);

-[ RECORD 1 ]-----------------------------------
json_array_reduce([2, 3, 4]::VARIANT, (acc, d) -> acc::Int32 * d::Int32): 24
```
