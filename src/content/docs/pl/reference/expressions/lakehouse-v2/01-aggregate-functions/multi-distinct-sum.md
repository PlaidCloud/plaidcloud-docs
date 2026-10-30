---
title: MULTI_DISTINCT_SUM (Lakehouse v2)
description: MULTI_DISTINCT_SUM — zwraca sumę różnych wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-sum.md
---

Zwraca sumę różnych wartości.

## Składnia Analyze

```python
func.multi_distinct_sum(get_column(table, 'bonus'))
```

## Przykłady Analyze

```python
func.multi_distinct_sum(get_column(table, 'bonus'))

┌───────┐
│ 25000 │
└───────┘
```

## Składnia SQL

```sql
MULTI_DISTINCT_SUM(<bonus>)
```

## Przykłady SQL

```sql
SELECT MULTI_DISTINCT_SUM(bonus) FROM employees;

┌───────┐
│ 25000 │
└───────┘
```
