---
title: ARRAY_DISTINCT (Lakehouse v2)
description: ARRAY_DISTINCT — elimina los elementos duplicados de una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-distinct.md
---

Elimina los elementos duplicados de una matriz.

## Sintaxis de Analyze

```python
func.array_distinct([1, 2, 2, 3, 3])
```

## Ejemplos de Analyze

```python
func.array_distinct([1, 2, 2, 3, 3])

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## Sintaxis de SQL

```sql
ARRAY_DISTINCT([1, 2, 2, 3, 3])
```

## Ejemplos de SQL

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 3, 3]);

┌─────────┐
│ [1,2,3] │
└─────────┘
```
