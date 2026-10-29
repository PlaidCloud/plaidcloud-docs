---
title: ARRAY_AVG (Lakehouse v2)
description: ARRAY_AVG – gibt den Durchschnitt der Elemente eines Arrays zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-avg.md
---

Gibt den Durchschnitt der Elemente eines Arrays zurück.

## Analyze-Syntax

```python
func.array_avg([1, 2, 3, 4])
```

## Analyze-Beispiele

```python
func.array_avg([10, 20, 30])

┌──────┐
│ 20.0 │
└──────┘
```

## SQL-Syntax

```sql
ARRAY_AVG([1, 2, 3, 4])
```

## SQL-Beispiele

```sql
SELECT ARRAY_AVG([10, 20, 30]);

┌──────┐
│ 20.0 │
└──────┘
```
