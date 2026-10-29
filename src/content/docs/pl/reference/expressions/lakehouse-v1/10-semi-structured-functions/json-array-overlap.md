---
title: JSON_ARRAY_OVERLAP (Lakehouse v1)
description: JSON_ARRAY_OVERLAP — sprawdza, czy dwie tablice JSON mają część wspólną, i zwraca true, jeśli istnieją elementy wspólne; w przeciwnym razie zwraca false.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-overlap.md
---

Sprawdza, czy dwie tablice JSON mają część wspólną, i zwraca `true`, jeśli istnieją elementy wspólne; w przeciwnym razie zwraca `false`.

## Składnia SQL

```sql
JSON_ARRAY_OVERLAP(<json_array1>, <json_array2>)
```

## Typ zwracany

Funkcja zwraca wartość logiczną:

- `true`, jeśli obie tablice JSON mają co najmniej jeden element wspólny,
- `false`, jeśli nie mają elementów wspólnych.

## Przykłady SQL

```sql
SELECT json_array_overlap(
    '["apple", "banana", "cherry"]'::JSON,  
    '["banana", "kiwi", "mango"]'::JSON
);

-[ RECORD 1 ]-----------------------------------
json_array_overlap('["apple", "banana", "cherry"]'::VARIANT, '["banana", "kiwi", "mango"]'::VARIANT): true


SELECT json_array_overlap(
    '["grape", "orange"]'::JSON,  
    '["apple", "kiwi"]'::JSON     
);

-[ RECORD 1 ]-----------------------------------
json_array_overlap('["grape", "orange"]'::VARIANT, '["apple", "kiwi"]'::VARIANT): false
```
