---
title: ARRAY_MIN (Lakehouse v2)
description: ARRAY_MIN — devuelve el elemento mínimo de una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-min.md
---

Devuelve el elemento mínimo de una matriz.

## Sintaxis de Analyze

```python
func.array_min([3, 1, 4, 1, 5])
```

## Ejemplos de Analyze

```python
func.array_min([3, 1, 4, 1, 5])

┌───┐
│ 1 │
└───┘
```

## Sintaxis de SQL

```sql
ARRAY_MIN([3, 1, 4, 1, 5])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_MIN([3, 1, 4, 1, 5]);

┌───┐
│ 1 │
└───┘
```
