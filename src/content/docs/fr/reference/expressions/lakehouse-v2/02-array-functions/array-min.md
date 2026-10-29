---
title: ARRAY_MIN (Lakehouse v2)
description: ARRAY_MIN — renvoie l'élément minimal d'un tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-min.md
---

Renvoie l'élément minimal d'un tableau.

## Syntaxe Analyze

```python
func.array_min([3, 1, 4, 1, 5])
```

## Exemples Analyze

```python
func.array_min([3, 1, 4, 1, 5])

┌───┐
│ 1 │
└───┘
```

## Syntaxe SQL

```sql
ARRAY_MIN([3, 1, 4, 1, 5])
```

## Exemples SQL

```sql
SELECT ARRAY_MIN([3, 1, 4, 1, 5]);

┌───┐
│ 1 │
└───┘
```
