---
title: JSON_ARRAY_OVERLAP (Lakehouse v1)
description: JSON_ARRAY_OVERLAP — 두 JSON 배열이 겹치는지 검사하여 공통 요소가 있으면 true, 없으면 false를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-array-overlap.md
---

두 JSON 배열이 겹치는지 검사하여 공통 요소가 있으면 `true`, 없으면 `false`를 반환합니다.

## SQL Syntax

```sql
JSON_ARRAY_OVERLAP(<json_array1>, <json_array2>)
```

## 반환 타입

이 함수는 불리언 값을 반환합니다.

- 두 JSON 배열에 공통 요소가 하나 이상 있으면 `true`,
- 공통 요소가 없으면 `false`.

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
