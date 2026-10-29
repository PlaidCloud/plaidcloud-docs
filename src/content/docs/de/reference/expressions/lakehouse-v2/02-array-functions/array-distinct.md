---
title: ARRAY_DISTINCT (Lakehouse v2)
description: ARRAY_DISTINCT – entfernt doppelte Elemente aus einem Array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-distinct.md
---

Entfernt doppelte Elemente aus einem Array.

## Analyze-Syntax

```python
func.array_distinct([1, 2, 2, 3, 3])
```

## Analyze-Beispiele

```python
func.array_distinct([1, 2, 2, 3, 3])

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## SQL-Syntax

```sql
ARRAY_DISTINCT([1, 2, 2, 3, 3])
```

## SQL-Beispiele

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 3, 3]);

┌─────────┐
│ [1,2,3] │
└─────────┘
```
