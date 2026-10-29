---
title: ARRAY_MAP (Lakehouse v2)
description: ARRAY_MAP — aplica uma expressão lambda a cada elemento de uma matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-map.md
---

Aplica uma expressão lambda a cada elemento de uma matriz.

## Sintaxe do Analyze

```python
func.array_map(get_column(table, 'arr'), lambda x: x * 2)
```

## Exemplos do Analyze

```python
func.array_map([1, 2, 3], lambda x: x * 2)

┌─────────┐
│ [2,4,6] │
└─────────┘
```

## Sintaxe SQL

```sql
ARRAY_MAP(<arr>, lambda x: x * 2)
```

## Exemplos SQL

```sql
SELECT ARRAY_MAP([1, 2, 3], x -> x * 2);

┌─────────┐
│ [2,4,6] │
└─────────┘
```
