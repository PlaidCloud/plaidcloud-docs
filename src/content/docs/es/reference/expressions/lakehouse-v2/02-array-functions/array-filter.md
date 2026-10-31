---
title: ARRAY_FILTER (Lakehouse v2)
description: ARRAY_FILTER — filtra los elementos de una matriz mediante una expresión lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-filter.md
---

Filtra los elementos de una matriz mediante una expresión lambda.

## Sintaxis de Analyze

```python
func.array_filter(get_column(table, 'arr'), lambda x: x > 2)
```

## Ejemplos de Analyze

```python
func.array_filter([1, 2, 3, 4, 5], lambda x: x > 2)

┌─────────┐
│ [3,4,5] │
└─────────┘
```

## Sintaxis de SQL

```sql
ARRAY_FILTER(<arr>, lambda x: x > 2)
```

## Ejemplos de SQL

```sql
SELECT ARRAY_FILTER([1, 2, 3, 4, 5], x -> x > 2);

┌─────────┐
│ [3,4,5] │
└─────────┘
```
