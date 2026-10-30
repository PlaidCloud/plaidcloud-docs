---
title: ARRAY_FILTER (Lakehouse v1)
description: "ARRAY_FILTER : construit un tableau à partir des éléments du tableau d'entrée pour lesquels la fonction lambda renvoie true."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-filter.md
---

Construit un tableau à partir des éléments du tableau d'entrée pour lesquels la fonction lambda renvoie true.

## Syntaxe Analyze

```python
func.array_filter( <array>, <lambda> )
```

## Exemples Analyze

```python
func.array_filter([1, 2, 3], x -> (x > 1))

┌─────────────────────────────────────────────┐
│ func.array_filter([1, 2, 3], x -> (x > 1))  │
├─────────────────────────────────────────────┤
│ [2,3]                                       │
└─────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_FILTER( <array>, <lambda> )
```

## Exemples SQL

```sql
SELECT ARRAY_FILTER([1, 2, 3], x -> x > 1);

┌───────────────────────────────────────┐
│ array_filter([1, 2, 3], x -> (x > 1)) │
├───────────────────────────────────────┤
│ [2,3]                                 │
└───────────────────────────────────────┘
```
