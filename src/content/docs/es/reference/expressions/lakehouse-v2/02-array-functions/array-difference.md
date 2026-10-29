---
title: ARRAY_DIFFERENCE (Lakehouse v2)
description: ARRAY_DIFFERENCE — devuelve una matriz con las diferencias entre elementos consecutivos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-difference.md
---

Devuelve una matriz con las diferencias entre elementos consecutivos.

## Sintaxis de Analyze

```python
func.array_difference([1, 3, 6, 10])
```

## Ejemplos de Analyze

```python
func.array_difference([1, 3, 6, 10])

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```

## Sintaxis de SQL

```sql
ARRAY_DIFFERENCE([1, 3, 6, 10])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_DIFFERENCE([1, 3, 6, 10]);

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```
