---
title: ARRAY_REMOVE (Lakehouse v2)
description: ARRAY_REMOVE – entfernt alle Vorkommen eines angegebenen Elements aus einem Array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-remove.md
---

Entfernt alle Vorkommen eines angegebenen Elements aus einem Array.

## Analyze-Syntax

```python
func.array_remove([1, 2, 3, 2, 1], 2)
```

## Analyze-Beispiele

```python
func.array_remove([1, 2, 3, 2, 1], 2)

┌─────────┐
│ [1,3,1] │
└─────────┘
```

## SQL-Syntax

```sql
ARRAY_REMOVE([1, 2, 3, 2, 1], 2)
```

## SQL-Beispiele

```sql
SELECT ARRAY_REMOVE([1, 2, 3, 2, 1], 2);

┌─────────┐
│ [1,3,1] │
└─────────┘
```
