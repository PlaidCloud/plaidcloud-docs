---
title: ARRAY_SLICE (Lakehouse v2)
description: ARRAY_SLICE — devuelve un fragmento de una matriz a partir de una posición inicial y con una longitud determinada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-slice.md
---

Devuelve un fragmento de una matriz a partir de una posición inicial y con una longitud determinada.

## Sintaxis de Analyze

```python
func.array_slice([1,2,3,4,5], 2, 3)
```

## Ejemplos de Analyze

```python
func.array_slice([1, 2, 3, 4, 5], 2, 3)

┌─────────┐
│ [2,3,4] │
└─────────┘
```

## Sintaxis de SQL

```sql
ARRAY_SLICE([1,2,3,4,5], 2, 3)
```

## Ejemplos de SQL

```sql
SELECT ARRAY_SLICE([1, 2, 3, 4, 5], 2, 3);

┌─────────┐
│ [2,3,4] │
└─────────┘
```
