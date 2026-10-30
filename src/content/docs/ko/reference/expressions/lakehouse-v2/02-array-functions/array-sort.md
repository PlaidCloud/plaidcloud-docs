---
title: ARRAY_SORT (Lakehouse v2)
description: ARRAY_SORT — 배열의 요소를 오름차순으로 정렬합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sort.md
---

배열의 요소를 오름차순으로 정렬합니다.

## Analyze 구문

```python
func.array_sort([3, 1, 4, 1, 5])
```

## Analyze 예제

```python
func.array_sort([3, 1, 4, 1, 5])

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```

## SQL 구문

```sql
ARRAY_SORT([3, 1, 4, 1, 5])
```

## SQL 예제

```sql
SELECT ARRAY_SORT([3, 1, 4, 1, 5]);

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```
