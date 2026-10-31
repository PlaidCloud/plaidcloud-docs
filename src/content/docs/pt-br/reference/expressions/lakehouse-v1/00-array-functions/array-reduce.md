---
title: ARRAY_REDUCE (Lakehouse v1)
description: ARRAY_REDUCE aplica iterativamente a função lambda aos elementos do array para reduzi-lo a um único valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-reduce.md
---

Aplica iterativamente a função lambda aos elementos do array para reduzi-lo a um único valor.

## Sintaxe do Analyze

```python
func.array_reduce( <array>, <lambda> )
```

## Exemplos do Analyze

```python
func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))

┌─────────────────────────────────────────────────────┐
│ func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))  │
├─────────────────────────────────────────────────────┤
│                                                  10 │
└─────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
ARRAY_REDUCE( <array>, <lambda> )
```

## Exemplos de SQL

```sql
SELECT ARRAY_REDUCE([1, 2, 3, 4], (x,y) -> x + y);

┌───────────────────────────────────────────────┐
│ array_reduce([1, 2, 3, 4], (x, y) -> (x + y)) │
├───────────────────────────────────────────────┤
│                                            10 │
└───────────────────────────────────────────────┘
```
