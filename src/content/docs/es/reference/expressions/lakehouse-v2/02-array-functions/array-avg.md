---
title: ARRAY_AVG (Lakehouse v2)
description: ARRAY_AVG — devuelve el promedio de los elementos de una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-avg.md
---

Devuelve el promedio de los elementos de una matriz.

## Sintaxis de Analyze

```python
func.array_avg([1, 2, 3, 4])
```

## Ejemplos de Analyze

```python
func.array_avg([10, 20, 30])

┌──────┐
│ 20.0 │
└──────┘
```

## Sintaxis de SQL

```sql
ARRAY_AVG([1, 2, 3, 4])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_AVG([10, 20, 30]);

┌──────┐
│ 20.0 │
└──────┘
```
