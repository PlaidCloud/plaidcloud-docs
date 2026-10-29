---
title: ARRAY_SORT (Lakehouse v2)
description: ARRAY_SORT – sortiert die Elemente eines Arrays in aufsteigender Reihenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sort.md
---

Sortiert die Elemente eines Arrays in aufsteigender Reihenfolge.

## Analyze-Syntax

```python
func.array_sort([3, 1, 4, 1, 5])
```

## Analyze-Beispiele

```python
func.array_sort([3, 1, 4, 1, 5])

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```

## SQL-Syntax

```sql
ARRAY_SORT([3, 1, 4, 1, 5])
```

## SQL-Beispiele

```sql
SELECT ARRAY_SORT([3, 1, 4, 1, 5]);

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```
