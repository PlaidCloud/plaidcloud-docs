---
title: MULTI_DISTINCT_SUM (Lakehouse v2)
description: MULTI_DISTINCT_SUM – gibt die Summe der eindeutigen Werte zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-sum.md
---

Gibt die Summe der eindeutigen Werte zurück.

## Analyze-Syntax

```python
func.multi_distinct_sum(get_column(table, 'bonus'))
```

## Analyze-Beispiele

```python
func.multi_distinct_sum(get_column(table, 'bonus'))

┌───────┐
│ 25000 │
└───────┘
```

## SQL-Syntax

```sql
MULTI_DISTINCT_SUM(<bonus>)
```

## SQL-Beispiele

```sql
SELECT MULTI_DISTINCT_SUM(bonus) FROM employees;

┌───────┐
│ 25000 │
└───────┘
```
