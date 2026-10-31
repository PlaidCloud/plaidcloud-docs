---
title: JSON_ARRAY_DISTINCT (Lakehouse v1)
description: JSON_ARRAY_DISTINCT — JSON 배열에서 중복된 요소를 제거하고 고유한 요소만 담은 배열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-distinct.md
---

JSON 배열에서 중복된 요소를 제거하고 고유한 요소만 담은 배열을 반환합니다.

## SQL Syntax

```sql
JSON_ARRAY_DISTINCT(<json_array>)
```

## 반환 타입

JSON 배열.

## SQL Examples

```sql
SELECT JSON_ARRAY_DISTINCT('["apple", "banana", "apple", "orange", "banana"]'::VARIANT);

-[ RECORD 1 ]-----------------------------------
json_array_distinct('["apple", "banana", "apple", "orange", "banana"]'::VARIANT): ["apple","banana","orange"]
```
