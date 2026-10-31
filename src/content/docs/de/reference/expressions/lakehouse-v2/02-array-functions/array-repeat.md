---
title: ARRAY_REPEAT (Lakehouse v2)
description: ARRAY_REPEAT – erstellt ein Array, das ein angegebenes Element N-mal wiederholt enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-repeat.md
---

Erstellt ein Array, das ein angegebenes Element N-mal wiederholt enthält.

## Analyze-Syntax

```python
func.array_repeat('x', 3)
```

## Analyze-Beispiele

```python
func.array_repeat('x', 3)

┌───────────────┐
│ ['x','x','x'] │
└───────────────┘
```

## SQL-Syntax

```sql
ARRAY_REPEAT('x', 3)
```

## SQL-Beispiele

```sql
SELECT ARRAY_REPEAT('x', 3);

┌───────────────┐
│ ["x","x","x"] │
└───────────────┘
```
