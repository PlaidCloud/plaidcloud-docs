---
title: ARRAY_REDUCE (Lakehouse v1)
description: ARRAY_REDUCE — aplica de forma iterativa la función lambda a los elementos del arreglo para reducirlo a un único valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-reduce.md
---

Aplica de forma iterativa la función lambda a los elementos del arreglo para reducirlo a un único valor.

## Sintaxis de Analyze

```python
func.array_reduce( <array>, <lambda> )
```

## Ejemplos de Analyze

```python
func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))

┌─────────────────────────────────────────────────────┐
│ func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))  │
├─────────────────────────────────────────────────────┤
│                                                  10 │
└─────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
ARRAY_REDUCE( <array>, <lambda> )
```

## Ejemplos de SQL

```sql
SELECT ARRAY_REDUCE([1, 2, 3, 4], (x,y) -> x + y);

┌───────────────────────────────────────────────┐
│ array_reduce([1, 2, 3, 4], (x, y) -> (x + y)) │
├───────────────────────────────────────────────┤
│                                            10 │
└───────────────────────────────────────────────┘
```
