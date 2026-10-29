---
title: JSON_ARRAY_DISTINCT (Lakehouse v1)
description: JSON_ARRAY_DISTINCT — remove os elementos duplicados de uma matriz JSON e devolve uma matriz apenas com elementos distintos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-distinct.md
---

Remove os elementos duplicados de uma matriz JSON e devolve uma matriz apenas com elementos distintos.

## Sintaxe SQL

```sql
JSON_ARRAY_DISTINCT(<json_array>)
```

## Tipo de retorno

Matriz JSON.

## Exemplos de SQL

```sql
SELECT JSON_ARRAY_DISTINCT('["apple", "banana", "apple", "orange", "banana"]'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_distinct('["apple", "banana", "apple", "orange", "banana"]'::VARIANT): ["apple","banana","orange"]
```
