---
title: JSON_ARRAY_OVERLAP (Lakehouse v1)
description: JSON_ARRAY_OVERLAP — comprueba si hay solapamiento entre dos arreglos JSON y devuelve true si hay elementos comunes; en caso contrario, devuelve false.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-overlap.md
---

Comprueba si hay solapamiento entre dos arreglos JSON y devuelve `true` si hay elementos comunes; en caso contrario, devuelve `false`.

## Sintaxis SQL

```sql
JSON_ARRAY_OVERLAP(<json_array1>, <json_array2>)
```

## Tipo de retorno

La función devuelve un valor booleano:

- `true` si hay al menos un elemento común entre los dos arreglos JSON,
- `false` si no hay elementos comunes.

## Ejemplos de SQL

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
