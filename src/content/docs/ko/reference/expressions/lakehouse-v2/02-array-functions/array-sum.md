---
title: ARRAY_SUM (Lakehouse v2)
description: ARRAY_SUM — 배열 요소의 합계를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sum.md
---

배열 요소의 합계를 반환합니다.

## Analyze 구문

```python
func.array_sum([1, 2, 3, 4, 5])
```

## Analyze 예제

```python
func.array_sum([10, 20, 30])

┌────┐
│ 60 │
└────┘
```

## SQL 구문

```sql
ARRAY_SUM([1, 2, 3, 4, 5])
```

## SQL 예제

```sql
SELECT ARRAY_SUM([10, 20, 30]);

┌────┐
│ 60 │
└────┘
```
