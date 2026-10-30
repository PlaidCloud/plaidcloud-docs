---
title: ARRAYS_OVERLAP (Lakehouse v2)
description: ARRAYS_OVERLAP — 두 배열에 공통 요소가 있는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/arrays-overlap.md
---

두 배열에 공통 요소가 있는지 확인합니다.

## Analyze 구문

```python
func.arrays_overlap([1,2,3], [3,4,5])
```

## Analyze 예제

```python
func.arrays_overlap([1, 2, 3], [3, 4, 5])

┌───┐
│ 1 │
└───┘
```

## SQL 구문

```sql
ARRAYS_OVERLAP([1,2,3], [3,4,5])
```

## SQL 예제

```sql
SELECT ARRAYS_OVERLAP([1, 2, 3], [3, 4, 5]);

┌───┐
│ 1 │
└───┘
```
