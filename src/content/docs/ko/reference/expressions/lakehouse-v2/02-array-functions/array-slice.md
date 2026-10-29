---
title: ARRAY_SLICE (Lakehouse v2)
description: ARRAY_SLICE — 시작 위치부터 지정한 길이만큼 배열의 일부를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-slice.md
---

시작 위치부터 지정한 길이만큼 배열의 일부를 반환합니다.

## Analyze 구문

```python
func.array_slice([1,2,3,4,5], 2, 3)
```

## Analyze 예제

```python
func.array_slice([1, 2, 3, 4, 5], 2, 3)

┌─────────┐
│ [2,3,4] │
└─────────┘
```

## SQL 구문

```sql
ARRAY_SLICE([1,2,3,4,5], 2, 3)
```

## SQL 예제

```sql
SELECT ARRAY_SLICE([1, 2, 3, 4, 5], 2, 3);

┌─────────┐
│ [2,3,4] │
└─────────┘
```
