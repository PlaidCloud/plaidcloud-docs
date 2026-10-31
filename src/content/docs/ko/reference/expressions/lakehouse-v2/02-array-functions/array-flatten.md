---
title: ARRAY_FLATTEN (Lakehouse v2)
description: ARRAY_FLATTEN — 중첩된 배열을 단일 수준의 배열로 평탄화합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-flatten.md
---

중첩된 배열을 단일 수준의 배열로 평탄화합니다.

## Analyze 구문

```python
func.array_flatten([[1,2],[3,4]])
```

## Analyze 예제

```python
func.array_flatten([[1, 2], [3, 4]])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQL 구문

```sql
ARRAY_FLATTEN([[1,2],[3,4]])
```

## SQL 예제

```sql
SELECT ARRAY_FLATTEN([[1, 2], [3, 4]]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
