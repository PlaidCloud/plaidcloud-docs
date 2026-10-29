---
title: ARRAYS_OVERLAP (Lakehouse v2)
description: ARRAYS_OVERLAP — comprueba si dos matrices tienen elementos en común.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/arrays-overlap.md
---

Comprueba si dos matrices tienen elementos en común.

## Sintaxis de Analyze

```python
func.arrays_overlap([1,2,3], [3,4,5])
```

## Ejemplos de Analyze

```python
func.arrays_overlap([1, 2, 3], [3, 4, 5])

┌───┐
│ 1 │
└───┘
```

## Sintaxis de SQL

```sql
ARRAYS_OVERLAP([1,2,3], [3,4,5])
```

## Ejemplos de SQL

```sql
SELECT ARRAYS_OVERLAP([1, 2, 3], [3, 4, 5]);

┌───┐
│ 1 │
└───┘
```
