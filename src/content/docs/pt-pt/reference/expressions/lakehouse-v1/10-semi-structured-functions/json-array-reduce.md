---
title: JSON_ARRAY_REDUCE (Lakehouse v1)
description: JSON_ARRAY_REDUCE — reduz uma matriz JSON a um único valor através da aplicação de uma expressão especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-reduce.md
---

Reduz uma matriz JSON a um único valor através da aplicação de uma expressão Lambda especificada. Para obter mais informações sobre expressões Lambda, consulte Expressões Lambda.

## Sintaxe SQL

```sql
JSON_ARRAY_REDUCE(<json_array>, <lambda_expression>)
```

## Exemplos de SQL

Este exemplo multiplica todos os elementos da matriz (2 _ 3 _ 4):

```sql
SELECT JSON_ARRAY_REDUCE(
    [2, 3, 4]::JSON,
    (acc, d) -> acc::Int * d::Int
);

-[ RECORD 1 ]-----------------------------------
json_array_reduce([2, 3, 4]::VARIANT, (acc, d) -> acc::Int32 * d::Int32): 24
```
