---
title: ARRAY_SUM (Lakehouse v2)
description: ARRAY_SUM – gibt die Summe der Elemente eines Arrays zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sum.md
---

Gibt die Summe der Elemente eines Arrays zurück.

## Analyze-Syntax

```python
func.array_sum([1, 2, 3, 4, 5])
```

## Analyze-Beispiele

```python
func.array_sum([10, 20, 30])

┌────┐
│ 60 │
└────┘
```

## SQL-Syntax

```sql
ARRAY_SUM([1, 2, 3, 4, 5])
```

## SQL-Beispiele

```sql
SELECT ARRAY_SUM([10, 20, 30]);

┌────┐
│ 60 │
└────┘
```
