---
title: ARRAY_MAP (Lakehouse v2)
description: ARRAY_MAP — aplica una expresión lambda a cada elemento de una matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-map.md
---

Aplica una expresión lambda a cada elemento de una matriz.

## Sintaxis de Analyze

```python
func.array_map(get_column(table, 'arr'), lambda x: x * 2)
```

## Ejemplos de Analyze

```python
func.array_map([1, 2, 3], lambda x: x * 2)

┌─────────┐
│ [2,4,6] │
└─────────┘
```

## Sintaxis de SQL

```sql
ARRAY_MAP(<arr>, lambda x: x * 2)
```

## Ejemplos de SQL

```sql
SELECT ARRAY_MAP([1, 2, 3], x -> x * 2);

┌─────────┐
│ [2,4,6] │
└─────────┘
```
