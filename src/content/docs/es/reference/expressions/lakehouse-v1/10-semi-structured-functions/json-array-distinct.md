---
title: JSON_ARRAY_DISTINCT (Lakehouse v1)
description: JSON_ARRAY_DISTINCT — elimina los elementos duplicados de un arreglo JSON y devuelve un arreglo con solo elementos distintos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-distinct.md
---

Elimina los elementos duplicados de un arreglo JSON y devuelve un arreglo con solo elementos distintos.

## Sintaxis SQL

```sql
JSON_ARRAY_DISTINCT(<json_array>)
```

## Tipo de retorno

Arreglo JSON.

## Ejemplos de SQL

```sql
SELECT JSON_ARRAY_DISTINCT('["apple", "banana", "apple", "orange", "banana"]'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_distinct('["apple", "banana", "apple", "orange", "banana"]'::VARIANT): ["apple","banana","orange"]
```
