---
title: JSON_ARRAY_TRANSFORM (Lakehouse v1)
description: JSON_ARRAY_TRANSFORM — Wandelt jedes Element eines JSON-Arrays mit einem angegebenen Lambda-Ausdruck um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-transform.md
---

Wandelt jedes Element eines JSON-Arrays mit einem angegebenen Transformations-Lambda-Ausdruck um. Weitere Informationen zu Lambda-Ausdrücken finden Sie unter Lambda Expressions.

## SQL Syntax

```sql
JSON_ARRAY_TRANSFORM(<json_array>, <lambda_expression>)
```

## Aliases

- [JSON_ARRAY_APPLY](../json-array-apply)
- [JSON_ARRAY_MAP](../json-array-map)

## Return Type

JSON-Array.

## SQL Examples

In diesem Beispiel wird jedes numerische Element des Arrays mit 10 multipliziert, sodass das ursprüngliche Array in `[10, 20, 30, 40]` umgewandelt wird:

```sql
SELECT JSON_ARRAY_TRANSFORM(
    [1, 2, 3, 4]::JSON,
    data -> (data::Int * 10)
);

-[ RECORD 1 ]-----------------------------------
json_array_transform([1, 2, 3, 4]::VARIANT, data -> data::Int32 * 10): [10,20,30,40]
```
