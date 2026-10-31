---
title: ARRAY_FILTER (Lakehouse v1)
description: ARRAY_FILTER — construye un arreglo con los elementos del arreglo de entrada para los que la función lambda devuelve verdadero.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-filter.md
---

Construye un arreglo con los elementos del arreglo de entrada para los que la función lambda devuelve verdadero.

## Sintaxis de Analyze

```python
func.array_filter( <array>, <lambda> )
```

## Ejemplos de Analyze

```python
func.array_filter([1, 2, 3], x -> (x > 1))

┌─────────────────────────────────────────────┐
│ func.array_filter([1, 2, 3], x -> (x > 1))  │
├─────────────────────────────────────────────┤
│ [2,3]                                       │
└─────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_FILTER( <array>, <lambda> )
```

## Ejemplos de SQL

```sql
SELECT ARRAY_FILTER([1, 2, 3], x -> x > 1);

┌───────────────────────────────────────┐
│ array_filter([1, 2, 3], x -> (x > 1)) │
├───────────────────────────────────────┤
│ [2,3]                                 │
└───────────────────────────────────────┘
```
