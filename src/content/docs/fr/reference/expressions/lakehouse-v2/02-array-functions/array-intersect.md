---
title: ARRAY_INTERSECT (Lakehouse v2)
description: ARRAY_INTERSECT — renvoie l'intersection de deux tableaux.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-intersect.md
---

Renvoie l'intersection de deux tableaux.

## Syntaxe Analyze

```python
func.array_intersect([1,2,3], [2,3,4])
```

## Exemples Analyze

```python
func.array_intersect([1, 2, 3], [2, 3, 4])

┌───────┐
│ [2,3] │
└───────┘
```

## Syntaxe SQL

```sql
ARRAY_INTERSECT([1,2,3], [2,3,4])
```

## Exemples SQL

```sql
SELECT ARRAY_INTERSECT([1, 2, 3], [2, 3, 4]);

┌───────┐
│ [2,3] │
└───────┘
```
