---
title: ARRAY_INTERSECT (Lakehouse v2)
description: ARRAY_INTERSECT — 두 배열의 교집합을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-intersect.md
---

두 배열의 교집합을 반환합니다.

## Analyze 구문

```python
func.array_intersect([1,2,3], [2,3,4])
```

## Analyze 예제

```python
func.array_intersect([1, 2, 3], [2, 3, 4])

┌───────┐
│ [2,3] │
└───────┘
```

## SQL 구문

```sql
ARRAY_INTERSECT([1,2,3], [2,3,4])
```

## SQL 예제

```sql
SELECT ARRAY_INTERSECT([1, 2, 3], [2, 3, 4]);

┌───────┐
│ [2,3] │
└───────┘
```
