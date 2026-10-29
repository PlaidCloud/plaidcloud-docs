---
title: JSON_ARRAY_REDUCE (Lakehouse v1)
description: JSON_ARRAY_REDUCE — Reduziert ein JSON-Array durch Anwenden eines angegebenen Lambda-Ausdrucks auf einen einzelnen Wert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-reduce.md
---

Reduziert ein JSON-Array durch Anwenden eines angegebenen Lambda-Ausdrucks auf einen einzelnen Wert. Weitere Informationen zu Lambda-Ausdrücken finden Sie unter Lambda Expressions.

## SQL Syntax

```sql
JSON_ARRAY_REDUCE(<json_array>, <lambda_expression>)
```

## SQL Examples

Dieses Beispiel multipliziert alle Elemente des Arrays (2 _ 3 _ 4):

```sql
SELECT JSON_ARRAY_REDUCE(
    [2, 3, 4]::JSON,
    (acc, d) -> acc::Int * d::Int
);

-[ RECORD 1 ]-----------------------------------
json_array_reduce([2, 3, 4]::VARIANT, (acc, d) -> acc::Int32 * d::Int32): 24
```
