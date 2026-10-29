---
title: ARRAY_DISTINCT (Lakehouse v1)
description: ARRAY_DISTINCT — elimina todos los duplicados y los valores NULL del arreglo sin conservar el orden original.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-distinct.md
---

Elimina todos los duplicados y los valores NULL del arreglo sin conservar el orden original.

## Sintaxis de Analyze

```python
func.array_distinct( <array> )
```

## Ejemplos de Analyze

```python
func.array_distinct([1, 2, 2, 4, 3])

┌───────────────────────────────────────┐
│ func.array_distinct([1, 2, 2, 4, 3])  │
├───────────────────────────────────────┤
│ [1,2,4,3]                             │
└───────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_DISTINCT( <array> )
```

## Ejemplos de SQL

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 4, 3]);

┌─────────────────────────────────┐
│ array_distinct([1, 2, 2, 4, 3]) │
├─────────────────────────────────┤
│ [1,2,4,3]                       │
└─────────────────────────────────┘
```
