---
title: JSON_ARRAY_OVERLAP
description: JSON_ARRAY_OVERLAP — checks if there is any overlap between two JSON arrays and.
---

Checks if there is any overlap between two JSON arrays and returns `true` if there are common elements; otherwise, it returns `false`.

## SQL Syntax

```sql
JSON_ARRAY_OVERLAP(<json_array1>, <json_array2>)
```

## Return Type

The function returns a boolean value:

- `true` if there is at least one common element between the two JSON arrays,
- `false` if there are no common elements.

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
