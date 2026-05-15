---
title: JSON_ARRAY_INTERSECTION
description: JSON_ARRAY_INTERSECTION — returns the common elements between two JSON arrays.
---

Returns the common elements between two JSON arrays.

## SQL Syntax

```sql
JSON_ARRAY_INTERSECTION(<json_array1>, <json_array2>)
```

## Return Type

JSON array.

## SQL Examples

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
