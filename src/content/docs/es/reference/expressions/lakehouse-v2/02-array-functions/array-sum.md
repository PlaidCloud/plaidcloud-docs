---
title: ARRAY_SUM (Lakehouse v2)
description: ARRAY_SUM — devuelve la suma de los elementos de una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sum.md
---

Devuelve la suma de los elementos de una matriz.

## Sintaxis de Analyze

```python
func.array_sum([1, 2, 3, 4, 5])
```

## Ejemplos de Analyze

```python
func.array_sum([10, 20, 30])

┌────┐
│ 60 │
└────┘
```

## Sintaxis de SQL

```sql
ARRAY_SUM([1, 2, 3, 4, 5])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_SUM([10, 20, 30]);

┌────┐
│ 60 │
└────┘
```
