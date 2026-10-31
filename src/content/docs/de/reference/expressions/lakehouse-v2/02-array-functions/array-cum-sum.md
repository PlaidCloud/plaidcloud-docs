---
title: ARRAY_CUM_SUM (Lakehouse v2)
description: ARRAY_CUM_SUM – gibt die kumulierte Summe der Elemente eines Arrays zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-cum-sum.md
---

Gibt die kumulierte Summe der Elemente eines Arrays zurück.

## Analyze-Syntax

```python
func.array_cum_sum([1, 2, 3, 4])
```

## Analyze-Beispiele

```python
func.array_cum_sum([1, 2, 3, 4])

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```

## SQL-Syntax

```sql
ARRAY_CUM_SUM([1, 2, 3, 4])
```

## SQL-Beispiele

```sql
SELECT ARRAY_CUM_SUM([1, 2, 3, 4]);

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```
