---
title: ARRAY_MIN (Lakehouse v2)
description: ARRAY_MIN – gibt das kleinste Element eines Arrays zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-min.md
---

Gibt das kleinste Element eines Arrays zurück.

## Analyze-Syntax

```python
func.array_min([3, 1, 4, 1, 5])
```

## Analyze-Beispiele

```python
func.array_min([3, 1, 4, 1, 5])

┌───┐
│ 1 │
└───┘
```

## SQL-Syntax

```sql
ARRAY_MIN([3, 1, 4, 1, 5])
```

## SQL-Beispiele

```sql
SELECT ARRAY_MIN([3, 1, 4, 1, 5]);

┌───┐
│ 1 │
└───┘
```
