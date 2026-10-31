---
title: ARRAY_SLICE (Lakehouse v2)
description: ARRAY_SLICE – gibt einen Ausschnitt eines Arrays ab einer Startposition mit einer bestimmten Länge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-slice.md
---

Gibt einen Ausschnitt eines Arrays ab einer Startposition mit einer bestimmten Länge zurück.

## Analyze-Syntax

```python
func.array_slice([1,2,3,4,5], 2, 3)
```

## Analyze-Beispiele

```python
func.array_slice([1, 2, 3, 4, 5], 2, 3)

┌─────────┐
│ [2,3,4] │
└─────────┘
```

## SQL-Syntax

```sql
ARRAY_SLICE([1,2,3,4,5], 2, 3)
```

## SQL-Beispiele

```sql
SELECT ARRAY_SLICE([1, 2, 3, 4, 5], 2, 3);

┌─────────┐
│ [2,3,4] │
└─────────┘
```
