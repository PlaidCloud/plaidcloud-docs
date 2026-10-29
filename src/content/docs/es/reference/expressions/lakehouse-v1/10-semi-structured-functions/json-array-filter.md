---
title: JSON_ARRAY_FILTER (Lakehouse v1)
description: JSON_ARRAY_FILTER — filtra los elementos de un arreglo JSON según una expresión Lambda especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-filter.md
---

Filtra los elementos de un arreglo JSON según una expresión Lambda especificada y devuelve solo los elementos que cumplen la condición. Para obtener más información sobre las expresiones Lambda, consulte Expresiones Lambda.

## Sintaxis SQL

```sql
JSON_ARRAY_FILTER(<json_array>, <lambda_expression>)
```

## Tipo de retorno

Arreglo JSON.

## Ejemplos de SQL

Este ejemplo filtra el arreglo para devolver solo las cadenas que empiezan por la letra `a`, con el resultado `["apple", "avocado"]`:

```sql
SELECT JSON_ARRAY_FILTER(
    ['apple', 'banana', 'avocado', 'grape']::JSON,
    d -> d::String LIKE 'a%'
);

-[ RECORD 1 ]-----------------------------------
json_array_filter(['apple', 'banana', 'avocado', 'grape']::VARIANT, d -> d::STRING LIKE 'a%'): ["apple","avocado"]
```
