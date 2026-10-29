---
title: ARRAY_INTERSECT (Lakehouse v2)
description: ARRAY_INTERSECT — devuelve la intersección de dos matrices.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-intersect.md
---

Devuelve la intersección de dos matrices.

## Sintaxis de Analyze

```python
func.array_intersect([1,2,3], [2,3,4])
```

## Ejemplos de Analyze

```python
func.array_intersect([1, 2, 3], [2, 3, 4])

┌───────┐
│ [2,3] │
└───────┘
```

## Sintaxis de SQL

```sql
ARRAY_INTERSECT([1,2,3], [2,3,4])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_INTERSECT([1, 2, 3], [2, 3, 4]);

┌───────┐
│ [2,3] │
└───────┘
```
