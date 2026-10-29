---
title: ARRAY_REDUCE (Lakehouse v1)
description: ARRAY_REDUCE — iteracyjnie stosuje funkcję lambda do elementów tablicy, aby zredukować tablicę do jednej wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-reduce.md
---

Iteracyjnie stosuje funkcję lambda do elementów tablicy, aby zredukować tablicę do jednej wartości.

## Składnia Analyze

```python
func.array_reduce( <array>, <lambda> )
```

## Przykłady Analyze

```python
func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))

┌─────────────────────────────────────────────────────┐
│ func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))  │
├─────────────────────────────────────────────────────┤
│                                                  10 │
└─────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
ARRAY_REDUCE( <array>, <lambda> )
```

## Przykłady SQL

```sql
SELECT ARRAY_REDUCE([1, 2, 3, 4], (x,y) -> x + y);

┌───────────────────────────────────────────────┐
│ array_reduce([1, 2, 3, 4], (x, y) -> (x + y)) │
├───────────────────────────────────────────────┤
│                                            10 │
└───────────────────────────────────────────────┘
```
