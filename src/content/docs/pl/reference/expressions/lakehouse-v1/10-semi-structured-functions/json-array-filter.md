---
title: JSON_ARRAY_FILTER (Lakehouse v1)
description: JSON_ARRAY_FILTER — filtruje elementy tablicy JSON na podstawie określonego wyrażenia Lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-filter.md
---

Filtruje elementy tablicy JSON na podstawie określonego wyrażenia Lambda i zwraca tylko te elementy, które spełniają warunek. Więcej informacji o wyrażeniach Lambda znajdziesz w sekcji Wyrażenia Lambda.

## Składnia SQL

```sql
JSON_ARRAY_FILTER(<json_array>, <lambda_expression>)
```

## Typ zwracany

Tablica JSON.

## Przykłady SQL

Ten przykład filtruje tablicę, aby zwrócić tylko ciągi znaków zaczynające się od litery `a`, co daje `["apple", "avocado"]`:

```sql
SELECT JSON_ARRAY_FILTER(
    ['apple', 'banana', 'avocado', 'grape']::JSON,
    d -> d::String LIKE 'a%'
);

-[ RECORD 1 ]-----------------------------------
json_array_filter(['apple', 'banana', 'avocado', 'grape']::VARIANT, d -> d::STRING LIKE 'a%'): ["apple","avocado"]
```
