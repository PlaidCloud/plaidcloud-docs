---
title: ARRAY_REMOVE_FIRST (Lakehouse v1)
description: ARRAY_REMOVE_FIRST — elimina el primer elemento del arreglo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-remove-first.md
---

Elimina el primer elemento del arreglo.

## Sintaxis de Analyze

```python
func.array_remove_first( <array> )
```

## Ejemplos de Analyze

```python
func.array_remove_first([1, 2, 3]) 

┌─────────────────────────────────────┐
│ func.array_remove_first([1, 2, 3])  │
├─────────────────────────────────────┤
│ [2,3]                               │
└─────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_REMOVE_FIRST( <array> )
```

## Ejemplos de SQL

```sql
SELECT ARRAY_REMOVE_FIRST([1, 2, 3]);

┌───────────────────────────────┐
│ array_remove_first([1, 2, 3]) │
├───────────────────────────────┤
│ [2,3]                         │
└───────────────────────────────┘
```
