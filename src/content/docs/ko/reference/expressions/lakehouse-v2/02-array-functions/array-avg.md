---
title: ARRAY_AVG (Lakehouse v2)
description: ARRAY_AVG — 배열 요소의 평균을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-avg.md
---

배열 요소의 평균을 반환합니다.

## Analyze 구문

```python
func.array_avg([1, 2, 3, 4])
```

## Analyze 예제

```python
func.array_avg([10, 20, 30])

┌──────┐
│ 20.0 │
└──────┘
```

## SQL 구문

```sql
ARRAY_AVG([1, 2, 3, 4])
```

## SQL 예제

```sql
SELECT ARRAY_AVG([10, 20, 30]);

┌──────┐
│ 20.0 │
└──────┘
```
