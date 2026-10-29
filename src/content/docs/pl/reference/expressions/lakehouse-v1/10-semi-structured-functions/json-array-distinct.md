---
title: JSON_ARRAY_DISTINCT (Lakehouse v1)
description: JSON_ARRAY_DISTINCT — usuwa zduplikowane elementy z tablicy JSON i zwraca tablicę zawierającą wyłącznie unikatowe elementy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-distinct.md
---

Usuwa zduplikowane elementy z tablicy JSON i zwraca tablicę zawierającą wyłącznie unikatowe elementy.

## Składnia SQL

```sql
JSON_ARRAY_DISTINCT(<json_array>)
```

## Typ zwracany

Tablica JSON.

## Przykłady SQL

```sql
SELECT JSON_ARRAY_DISTINCT('["apple", "banana", "apple", "orange", "banana"]'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_distinct('["apple", "banana", "apple", "orange", "banana"]'::VARIANT): ["apple","banana","orange"]
```
