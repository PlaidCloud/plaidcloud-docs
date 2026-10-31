---
title: ARRAY_TOP_N (Lakehouse v2)
description: ARRAY_TOP_N — devuelve los N elementos principales de una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-top-n.md
---

Devuelve los N elementos principales de una matriz.

## Sintaxis de Analyze

```python
func.array_top_n([3,1,4,1,5], 3)
```

## Ejemplos de Analyze

```python
func.array_top_n([3, 1, 4, 1, 5], 3)

┌─────────┐
│ [5,4,3] │
└─────────┘
```

## Sintaxis de SQL

```sql
ARRAY_TOP_N([3,1,4,1,5], 3)
```

## Ejemplos de SQL

```sql
SELECT ARRAY_TOP_N([3, 1, 4, 1, 5], 3);

┌─────────┐
│ [5,4,3] │
└─────────┘
```
