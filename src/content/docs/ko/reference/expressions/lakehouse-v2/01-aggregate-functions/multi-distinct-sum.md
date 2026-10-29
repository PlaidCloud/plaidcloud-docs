---
title: MULTI_DISTINCT_SUM (Lakehouse v2)
description: MULTI_DISTINCT_SUM — 고유 값의 합계를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-sum.md
---

고유 값의 합계를 반환합니다.

## Analyze 구문

```python
func.multi_distinct_sum(get_column(table, 'bonus'))
```

## Analyze 예제

```python
func.multi_distinct_sum(get_column(table, 'bonus'))

┌───────┐
│ 25000 │
└───────┘
```

## SQL 구문

```sql
MULTI_DISTINCT_SUM(<bonus>)
```

## SQL 예제

```sql
SELECT MULTI_DISTINCT_SUM(bonus) FROM employees;

┌───────┐
│ 25000 │
└───────┘
```
