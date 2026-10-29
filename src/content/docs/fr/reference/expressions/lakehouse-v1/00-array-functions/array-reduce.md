---
title: ARRAY_REDUCE (Lakehouse v1)
description: "ARRAY_REDUCE : applique itérativement la fonction lambda aux éléments du tableau afin de réduire celui-ci à une seule valeur."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-reduce.md
---

Applique itérativement la fonction lambda aux éléments du tableau afin de réduire celui-ci à une seule valeur.

## Syntaxe Analyze

```python
func.array_reduce( <array>, <lambda> )
```

## Exemples Analyze

```python
func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))

┌─────────────────────────────────────────────────────┐
│ func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))  │
├─────────────────────────────────────────────────────┤
│                                                  10 │
└─────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_REDUCE( <array>, <lambda> )
```

## Exemples SQL

```sql
SELECT ARRAY_REDUCE([1, 2, 3, 4], (x,y) -> x + y);

┌───────────────────────────────────────────────┐
│ array_reduce([1, 2, 3, 4], (x, y) -> (x + y)) │
├───────────────────────────────────────────────┤
│                                            10 │
└───────────────────────────────────────────────┘
```
