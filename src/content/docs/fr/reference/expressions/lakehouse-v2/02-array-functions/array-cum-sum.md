---
title: ARRAY_CUM_SUM (Lakehouse v2)
description: ARRAY_CUM_SUM — renvoie la somme cumulée des éléments d'un tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-cum-sum.md
---

Renvoie la somme cumulée des éléments d'un tableau.

## Syntaxe Analyze

```python
func.array_cum_sum([1, 2, 3, 4])
```

## Exemples Analyze

```python
func.array_cum_sum([1, 2, 3, 4])

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```

## Syntaxe SQL

```sql
ARRAY_CUM_SUM([1, 2, 3, 4])
```

## Exemples SQL

```sql
SELECT ARRAY_CUM_SUM([1, 2, 3, 4]);

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```
