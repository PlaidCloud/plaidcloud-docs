---
title: ARRAY_MAX (Lakehouse v2)
description: ARRAY_MAX — renvoie l'élément maximal d'un tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-max.md
---

Renvoie l'élément maximal d'un tableau.

## Syntaxe Analyze

```python
func.array_max([3, 1, 4, 1, 5])
```

## Exemples Analyze

```python
func.array_max([3, 1, 4, 1, 5])

┌───┐
│ 5 │
└───┘
```

## Syntaxe SQL

```sql
ARRAY_MAX([3, 1, 4, 1, 5])
```

## Exemples SQL

```sql
SELECT ARRAY_MAX([3, 1, 4, 1, 5]);

┌───┐
│ 5 │
└───┘
```
