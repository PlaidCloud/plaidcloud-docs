---
title: JSON_ARRAY_OVERLAP (Lakehouse v1)
description: JSON_ARRAY_OVERLAP — vérifie si deux tableaux JSON ont des éléments en commun et renvoie true si c'est le cas, sinon false.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-overlap.md
---

Vérifie si deux tableaux JSON ont des éléments en commun et renvoie `true` si c'est le cas, sinon `false`.

## Syntaxe SQL

```sql
JSON_ARRAY_OVERLAP(<json_array1>, <json_array2>)
```

## Type de retour

La fonction renvoie une valeur booléenne :

- `true` s'il existe au moins un élément commun aux deux tableaux JSON,
- `false` s'il n'existe aucun élément commun.

## Exemples SQL

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
