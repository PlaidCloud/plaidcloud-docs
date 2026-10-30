---
title: ARRAY_LENGTH (Lakehouse v2)
description: ARRAY_LENGTH — devuelve el número de elementos de una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-length.md
---

Devuelve el número de elementos de una matriz.

## Sintaxis de Analyze

```python
func.array_length([1, 2, 3])
```

## Ejemplos de Analyze

```python
func.array_length([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## Sintaxis de SQL

```sql
ARRAY_LENGTH([1, 2, 3])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_LENGTH([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
