---
title: ARRAY_DIFFERENCE (Lakehouse v2)
description: ARRAY_DIFFERENCE — 연속한 요소 간 차이로 이루어진 배열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-difference.md
---

연속한 요소 간 차이로 이루어진 배열을 반환합니다.

## Analyze 구문

```python
func.array_difference([1, 3, 6, 10])
```

## Analyze 예제

```python
func.array_difference([1, 3, 6, 10])

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```

## SQL 구문

```sql
ARRAY_DIFFERENCE([1, 3, 6, 10])
```

## SQL 예제

```sql
SELECT ARRAY_DIFFERENCE([1, 3, 6, 10]);

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```
