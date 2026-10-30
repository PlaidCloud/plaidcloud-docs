---
title: ARRAY_FLATTEN (Lakehouse v1)
description: ARRAY_FLATTEN — aplana arreglos anidados y los convierte en un arreglo de un solo nivel.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-flatten.md
---

Aplana arreglos anidados y los convierte en un arreglo de un solo nivel.

## Sintaxis de Analyze

```python
func.array_flatten( <array> )
```

## Ejemplos de Analyze

```python
func.array_flatten([[1, 2], [3, 4, 5]]) 

┌──────────────────────────────────────────┐
│ func.array_flatten([[1, 2], [3, 4, 5]])  │
├──────────────────────────────────────────┤
│ [1,2,3,4,5]                              │
└──────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_FLATTEN( <array> )
```

## Ejemplos de SQL

```sql
SELECT ARRAY_FLATTEN([[1,2], [3,4,5]]);

┌────────────────────────────────────┐
│ array_flatten([[1, 2], [3, 4, 5]]) │
├────────────────────────────────────┤
│ [1,2,3,4,5]                        │
└────────────────────────────────────┘
```
