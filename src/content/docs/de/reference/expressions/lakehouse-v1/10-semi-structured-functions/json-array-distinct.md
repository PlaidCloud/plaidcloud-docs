---
title: JSON_ARRAY_DISTINCT (Lakehouse v1)
description: JSON_ARRAY_DISTINCT — Entfernt doppelte Elemente aus einem JSON-Array und gibt ein Array mit ausschließlich eindeutigen Elementen zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-distinct.md
---

Entfernt doppelte Elemente aus einem JSON-Array und gibt ein Array mit ausschließlich eindeutigen Elementen zurück.

## SQL Syntax

```sql
JSON_ARRAY_DISTINCT(<json_array>)
```

## Return Type

JSON-Array.

## SQL Examples

```sql
SELECT JSON_ARRAY_DISTINCT('["apple", "banana", "apple", "orange", "banana"]'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_distinct('["apple", "banana", "apple", "orange", "banana"]'::VARIANT): ["apple","banana","orange"]
```
