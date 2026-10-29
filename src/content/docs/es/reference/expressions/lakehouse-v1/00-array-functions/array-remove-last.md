---
title: ARRAY_REMOVE_LAST (Lakehouse v1)
description: ARRAY_REMOVE_LAST — elimina el último elemento del arreglo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-remove-last.md
---

Elimina el último elemento del arreglo.

## Sintaxis de Analyze

```python
func.array_remove_last( <array> )
```

## Ejemplos de Analyze

```python
func.array_remove_last([1, 2, 3]) 

┌────────────────────────────────────┐
│ func.array_remove_last([1, 2, 3])  │
├────────────────────────────────────┤
│ [1,2]                              │
└────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_REMOVE_LAST( <array> )
```

## Ejemplos de SQL

```sql
SELECT ARRAY_REMOVE_LAST([1, 2, 3]);

┌──────────────────────────────┐
│ array_remove_last([1, 2, 3]) │
├──────────────────────────────┤
│ [1,2]                        │
└──────────────────────────────┘
```
