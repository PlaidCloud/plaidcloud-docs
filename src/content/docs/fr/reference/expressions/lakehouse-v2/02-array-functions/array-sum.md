---
title: ARRAY_SUM (Lakehouse v2)
description: ARRAY_SUM — renvoie la somme des éléments d'un tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sum.md
---

Renvoie la somme des éléments d'un tableau.

## Syntaxe Analyze

```python
func.array_sum([1, 2, 3, 4, 5])
```

## Exemples Analyze

```python
func.array_sum([10, 20, 30])

┌────┐
│ 60 │
└────┘
```

## Syntaxe SQL

```sql
ARRAY_SUM([1, 2, 3, 4, 5])
```

## Exemples SQL

```sql
SELECT ARRAY_SUM([10, 20, 30]);

┌────┐
│ 60 │
└────┘
```
