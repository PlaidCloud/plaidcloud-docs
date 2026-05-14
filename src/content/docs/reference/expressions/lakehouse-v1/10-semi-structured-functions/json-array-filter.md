---
title: JSON_ARRAY_FILTER
description: "Learn how to use the JSON_ARRAY_FILTER semi-structured data function in PlaidCloud Lakehouse. Filters elements from a JSON array based on a specified Lambda..."
---

Filters elements from a JSON array based on a specified Lambda expression, returning only the elements that satisfy the condition. For more information about Lambda expression, see Lambda Expressions.

## SQL Syntax

```sql
JSON_ARRAY_FILTER(<json_array>, <lambda_expression>)
```

## Return Type

JSON array.

## SQL Examples

This example filters the array to return only the strings that start with the letter `a`, resulting in `["apple", "avocado"]`:

```sql
SELECT JSON_ARRAY_FILTER(
    ['apple', 'banana', 'avocado', 'grape']::JSON,
    d -> d::String LIKE 'a%'
);

-[ RECORD 1 ]-----------------------------------
json_array_filter(['apple', 'banana', 'avocado', 'grape']::VARIANT, d -> d::STRING LIKE 'a%'): ["apple","avocado"]
```
