---
title: JSON_ARRAY_EXCEPT
description: JSON_ARRAY_EXCEPT — returns a new JSON array containing the elements from the.
---

Returns a new JSON array containing the elements from the first JSON array that are not present in the second JSON array.

## SQL Syntax

```sql
JSON_ARRAY_EXCEPT(<json_array1>, <json_array2>)
```

## Return Type

JSON array.

## SQL Examples

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
