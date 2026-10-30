---
title: ARRAY_CUM_SUM (Lakehouse v2)
description: ARRAY_CUM_SUM — 배열 요소의 누적 합계를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-cum-sum.md
---

배열 요소의 누적 합계를 반환합니다.

## Analyze 구문

```python
func.array_cum_sum([1, 2, 3, 4])
```

## Analyze 예제

```python
func.array_cum_sum([1, 2, 3, 4])

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```

## SQL 구문

```sql
ARRAY_CUM_SUM([1, 2, 3, 4])
```

## SQL 예제

```sql
SELECT ARRAY_CUM_SUM([1, 2, 3, 4]);

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```
