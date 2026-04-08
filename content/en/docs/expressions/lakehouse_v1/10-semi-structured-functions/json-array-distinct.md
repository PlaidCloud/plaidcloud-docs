---
title: JSON_ARRAY_DISTINCT
description: "Learn how to use the JSON_ARRAY_DISTINCT semi-structured data function in PlaidCloud Lakehouse. Removes duplicate elements from a JSON array and returns an..."
---

Removes duplicate elements from a JSON array and returns an array with only distinct elements.

## SQL Syntax

```sql
JSON_ARRAY_DISTINCT(<json_array>)
```

## Return Type

JSON array.

## SQL Examples

```sql
SELECT JSON_ARRAY_DISTINCT('["apple", "banana", "apple", "orange", "banana"]'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_distinct('["apple", "banana", "apple", "orange", "banana"]'::VARIANT): ["apple","banana","orange"]
```
