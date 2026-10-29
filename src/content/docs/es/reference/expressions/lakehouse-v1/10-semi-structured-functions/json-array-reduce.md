---
title: JSON_ARRAY_REDUCE (Lakehouse v1)
description: JSON_ARRAY_REDUCE — reduce un arreglo JSON a un único valor aplicando una expresión Lambda especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-reduce.md
---

Reduce un arreglo JSON a un único valor aplicando una expresión Lambda especificada. Para obtener más información sobre las expresiones Lambda, consulte Expresiones Lambda.

## Sintaxis SQL

```sql
JSON_ARRAY_REDUCE(<json_array>, <lambda_expression>)
```

## Ejemplos de SQL

Este ejemplo multiplica todos los elementos del arreglo (2 _ 3 _ 4):

```sql
SELECT JSON_ARRAY_REDUCE(
    [2, 3, 4]::JSON,
    (acc, d) -> acc::Int * d::Int
);

-[ RECORD 1 ]-----------------------------------
json_array_reduce([2, 3, 4]::VARIANT, (acc, d) -> acc::Int32 * d::Int32): 24
```
