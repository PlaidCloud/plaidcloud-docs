---
title: JSON_ARRAY_EXCEPT (Lakehouse v1)
description: JSON_ARRAY_EXCEPT — Gibt ein neues JSON-Array mit den Elementen des ersten JSON-Arrays zurück, die im zweiten JSON-Array nicht enthalten sind.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-except.md
---

Gibt ein neues JSON-Array mit den Elementen des ersten JSON-Arrays zurück, die im zweiten JSON-Array nicht enthalten sind.

## SQL Syntax

```sql
JSON_ARRAY_EXCEPT(<json_array1>, <json_array2>)
```

## Return Type

JSON-Array.

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
