---
title: "REVERSE (Matriz, Lakehouse v2)"
description: REVERSE — devuelve una matriz con los elementos en orden inverso.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/reverse.md
---

Devuelve una matriz con los elementos en orden inverso.

## Sintaxis de Analyze

```python
func.reverse([1, 2, 3])
```

## Ejemplos de Analyze

```python
func.reverse([1, 2, 3])

┌─────────┐
│ [3,2,1] │
└─────────┘
```

## Sintaxis de SQL

```sql
REVERSE([1, 2, 3])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_REVERSE([1, 2, 3]);

┌─────────┐
│ [3,2,1] │
└─────────┘
```
