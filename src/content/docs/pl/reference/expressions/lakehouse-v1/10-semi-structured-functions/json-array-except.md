---
title: JSON_ARRAY_EXCEPT (Lakehouse v1)
description: JSON_ARRAY_EXCEPT — zwraca nową tablicę JSON zawierającą elementy z pierwszej tablicy JSON, których nie ma w drugiej tablicy JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-except.md
---

Zwraca nową tablicę JSON zawierającą elementy z pierwszej tablicy JSON, których nie ma w drugiej tablicy JSON.

## Składnia SQL

```sql
JSON_ARRAY_EXCEPT(<json_array1>, <json_array2>)
```

## Typ zwracany

Tablica JSON.

## Przykłady SQL

```sql
SELECT JSON_ARRAY_EXCEPT(
    '["apple", "banana", "orange"]'::JSON,  
    '["banana", "grapes"]'::JSON         
);

-[ RECORD 1 ]-----------------------------------
json_array_except('["apple", "banana", "orange"]'::VARIANT, '["banana", "grapes"]'::VARIANT): ["apple","orange"]

-- Return an empty array because all elements in the first array are present in the second array.
SELECT json_array_except('["apple", "banana", "orange"]'::VARIANT, '["apple", "banana", "orange"]'::VARIANT)

-[ RECORD 1 ]-----------------------------------
json_array_except('["apple", "banana", "orange"]'::VARIANT, '["apple", "banana", "orange"]'::VARIANT): []
```
