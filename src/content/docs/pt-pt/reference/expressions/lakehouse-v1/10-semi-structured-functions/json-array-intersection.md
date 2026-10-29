---
title: JSON_ARRAY_INTERSECTION (Lakehouse v1)
description: JSON_ARRAY_INTERSECTION — devolve os elementos comuns a duas matrizes JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-intersection.md
---

Devolve os elementos comuns a duas matrizes JSON.

## Sintaxe SQL

```sql
JSON_ARRAY_INTERSECTION(<json_array1>, <json_array2>)
```

## Tipo de retorno

Matriz JSON.

## Exemplos de SQL

```sql
-- Find the intersection of two JSON arrays
SELECT json_array_intersection('["Electronics", "Books", "Toys"]'::JSON, '["Books", "Fashion", "Electronics"]'::JSON);

-[ RECORD 1 ]-----------------------------------
json_array_intersection('["Electronics", "Books", "Toys"]'::VARIANT, '["Books", "Fashion", "Electronics"]'::VARIANT): ["Electronics","Books"]

-- Find the intersection of the result from the first query with a third JSON array using an iterative approach
SELECT json_array_intersection(
    json_array_intersection('["Electronics", "Books", "Toys"]'::JSON, '["Books", "Fashion", "Electronics"]'::JSON),
    '["Electronics", "Books", "Clothing"]'::JSON
);

-[ RECORD 1 ]-----------------------------------
json_array_intersection(json_array_intersection('["Electronics", "Books", "Toys"]'::VARIANT, '["Books", "Fashion", "Electronics"]'::VARIANT), '["Electronics", "Books", "Clothing"]'::VARIANT): ["Electronics","Books"]
```
