---
title: ARRAY_TOP_N (Lakehouse v2)
description: ARRAY_TOP_N – gibt die obersten N Elemente eines Arrays zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-top-n.md
---

Gibt die obersten N Elemente eines Arrays zurück.

## Analyze-Syntax

```python
func.array_top_n([3,1,4,1,5], 3)
```

## Analyze-Beispiele

```python
func.array_top_n([3, 1, 4, 1, 5], 3)

┌─────────┐
│ [5,4,3] │
└─────────┘
```

## SQL-Syntax

```sql
ARRAY_TOP_N([3,1,4,1,5], 3)
```

## SQL-Beispiele

```sql
SELECT ARRAY_TOP_N([3, 1, 4, 1, 5], 3);

┌─────────┐
│ [5,4,3] │
└─────────┘
```
