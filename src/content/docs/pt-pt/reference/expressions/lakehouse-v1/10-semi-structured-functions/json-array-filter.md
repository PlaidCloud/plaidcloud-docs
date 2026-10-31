---
title: JSON_ARRAY_FILTER (Lakehouse v1)
description: JSON_ARRAY_FILTER — filtra elementos de uma matriz JSON com base numa expressão Lambda especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-filter.md
---

Filtra elementos de uma matriz JSON com base numa expressão Lambda especificada, devolvendo apenas os elementos que satisfazem a condição. Para obter mais informações sobre expressões Lambda, consulte Expressões Lambda.

## Sintaxe SQL

```sql
JSON_ARRAY_FILTER(<json_array>, <lambda_expression>)
```

## Tipo de retorno

Matriz JSON.

## Exemplos de SQL

Este exemplo filtra a matriz para devolver apenas as cadeias que começam pela letra `a`, resultando em `["apple", "avocado"]`:

```sql
SELECT JSON_ARRAY_FILTER(
    ['apple', 'banana', 'avocado', 'grape']::JSON,
    d -> d::String LIKE 'a%'
);

-[ RECORD 1 ]-----------------------------------
json_array_filter(['apple', 'banana', 'avocado', 'grape']::VARIANT, d -> d::STRING LIKE 'a%'): ["apple","avocado"]
```
