---
title: ARRAY_CUM_SUM (Lakehouse v2)
description: ARRAY_CUM_SUM — devuelve la suma acumulada de los elementos de una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-cum-sum.md
---

Devuelve la suma acumulada de los elementos de una matriz.

## Sintaxis de Analyze

```python
func.array_cum_sum([1, 2, 3, 4])
```

## Ejemplos de Analyze

```python
func.array_cum_sum([1, 2, 3, 4])

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_CUM_SUM([1, 2, 3, 4])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_CUM_SUM([1, 2, 3, 4]);

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```
