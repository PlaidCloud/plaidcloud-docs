---
title: ARRAY_REMOVE (Lakehouse v2)
description: ARRAY_REMOVE — elimina todas las apariciones de un elemento específico de una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-remove.md
---

Elimina todas las apariciones de un elemento específico de una matriz.

## Sintaxis de Analyze

```python
func.array_remove([1, 2, 3, 2, 1], 2)
```

## Ejemplos de Analyze

```python
func.array_remove([1, 2, 3, 2, 1], 2)

┌─────────┐
│ [1,3,1] │
└─────────┘
```

## Sintaxis de SQL

```sql
ARRAY_REMOVE([1, 2, 3, 2, 1], 2)
```

## Ejemplos de SQL

```sql
SELECT ARRAY_REMOVE([1, 2, 3, 2, 1], 2);

┌─────────┐
│ [1,3,1] │
└─────────┘
```
