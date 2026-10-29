---
title: ARRAY_MAX (Lakehouse v2)
description: ARRAY_MAX — devuelve el elemento máximo de una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-max.md
---

Devuelve el elemento máximo de una matriz.

## Sintaxis de Analyze

```python
func.array_max([3, 1, 4, 1, 5])
```

## Ejemplos de Analyze

```python
func.array_max([3, 1, 4, 1, 5])

┌───┐
│ 5 │
└───┘
```

## Sintaxis de SQL

```sql
ARRAY_MAX([3, 1, 4, 1, 5])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_MAX([3, 1, 4, 1, 5]);

┌───┐
│ 5 │
└───┘
```
