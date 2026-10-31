---
title: JSON_ARRAY_REDUCE (Lakehouse v1)
description: JSON_ARRAY_REDUCE — réduit un tableau JSON à une valeur unique en appliquant une expression Lambda donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-reduce.md
---

Réduit un tableau JSON à une valeur unique en appliquant une expression Lambda donnée. Pour en savoir plus sur les expressions Lambda, consultez Lambda Expressions.

## Syntaxe SQL

```sql
JSON_ARRAY_REDUCE(<json_array>, <lambda_expression>)
```

## Exemples SQL

Cet exemple multiplie tous les éléments du tableau (2 _ 3 _ 4) :

```sql
SELECT JSON_ARRAY_REDUCE(
    [2, 3, 4]::JSON,
    (acc, d) -> acc::Int * d::Int
);

-[ RECORD 1 ]-----------------------------------
json_array_reduce([2, 3, 4]::VARIANT, (acc, d) -> acc::Int32 * d::Int32): 24
```
