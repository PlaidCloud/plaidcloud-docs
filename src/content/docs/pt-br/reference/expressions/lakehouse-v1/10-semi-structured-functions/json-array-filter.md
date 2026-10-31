---
title: JSON_ARRAY_FILTER (Lakehouse v1)
description: JSON_ARRAY_FILTER — filtra elementos de um array JSON com base em uma expressão Lambda especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-filter.md
---

Filtra elementos de um array JSON com base em uma expressão Lambda especificada, retornando apenas os elementos que satisfazem a condição. Para obter mais informações sobre expressões Lambda, consulte Expressões Lambda.

## Sintaxe SQL

```sql
JSON_ARRAY_FILTER(<json_array>, <lambda_expression>)
```

## Tipo de retorno

Array JSON.

## Exemplos de SQL

Este exemplo filtra o array para retornar apenas as strings que começam com a letra `a`, resultando em `["apple", "avocado"]`:

```sql
SELECT JSON_ARRAY_FILTER(
    ['apple', 'banana', 'avocado', 'grape']::JSON,
    d -> d::String LIKE 'a%'
);

-[ RECORD 1 ]-----------------------------------
json_array_filter(['apple', 'banana', 'avocado', 'grape']::VARIANT, d -> d::STRING LIKE 'a%'): ["apple","avocado"]
```
