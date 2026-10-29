---
title: JSON_ARRAY_OVERLAP (Lakehouse v1)
description: JSON_ARRAY_OVERLAP — Prüft, ob sich zwei JSON-Arrays überschneiden, und gibt true zurück, wenn gemeinsame Elemente vorhanden sind, andernfalls false.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-overlap.md
---

Prüft, ob sich zwei JSON-Arrays überschneiden, und gibt `true` zurück, wenn gemeinsame Elemente vorhanden sind, andernfalls `false`.

## SQL Syntax

```sql
JSON_ARRAY_OVERLAP(<json_array1>, <json_array2>)
```

## Return Type

Die Funktion gibt einen Booleschen Wert zurück:

- `true`, wenn die beiden JSON-Arrays mindestens ein gemeinsames Element haben,
- `false`, wenn es keine gemeinsamen Elemente gibt.

## SQL Examples

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
