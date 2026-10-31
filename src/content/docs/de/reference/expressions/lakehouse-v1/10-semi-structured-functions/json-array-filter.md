---
title: JSON_ARRAY_FILTER (Lakehouse v1)
description: JSON_ARRAY_FILTER — Filtert Elemente eines JSON-Arrays anhand eines angegebenen Lambda-Ausdrucks.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-filter.md
---

Filtert Elemente eines JSON-Arrays anhand eines angegebenen Lambda-Ausdrucks und gibt nur die Elemente zurück, die die Bedingung erfüllen. Weitere Informationen zu Lambda-Ausdrücken finden Sie unter Lambda Expressions.

## SQL Syntax

```sql
JSON_ARRAY_FILTER(<json_array>, <lambda_expression>)
```

## Return Type

JSON-Array.

## SQL Examples

Dieses Beispiel filtert das Array so, dass nur die Zeichenfolgen zurückgegeben werden, die mit dem Buchstaben `a` beginnen. Das Ergebnis ist `["apple", "avocado"]`:

```sql
SELECT JSON_ARRAY_FILTER(
    ['apple', 'banana', 'avocado', 'grape']::JSON,
    d -> d::String LIKE 'a%'
);

-[ RECORD 1 ]-----------------------------------
json_array_filter(['apple', 'banana', 'avocado', 'grape']::VARIANT, d -> d::STRING LIKE 'a%'): ["apple","avocado"]
```
