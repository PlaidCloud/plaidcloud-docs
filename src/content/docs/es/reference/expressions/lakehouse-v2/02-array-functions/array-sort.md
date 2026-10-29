---
title: ARRAY_SORT (Lakehouse v2)
description: ARRAY_SORT — ordena los elementos de una matriz de forma ascendente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sort.md
---

Ordena los elementos de una matriz de forma ascendente.

## Sintaxis de Analyze

```python
func.array_sort([3, 1, 4, 1, 5])
```

## Ejemplos de Analyze

```python
func.array_sort([3, 1, 4, 1, 5])

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_SORT([3, 1, 4, 1, 5])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_SORT([3, 1, 4, 1, 5]);

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```
