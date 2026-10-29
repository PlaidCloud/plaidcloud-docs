---
title: ARRAYS_OVERLAP (Lakehouse v2)
description: ARRAYS_OVERLAP — vérifie si deux tableaux ont des éléments en commun.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/arrays-overlap.md
---

Vérifie si deux tableaux ont des éléments en commun.

## Syntaxe Analyze

```python
func.arrays_overlap([1,2,3], [3,4,5])
```

## Exemples Analyze

```python
func.arrays_overlap([1, 2, 3], [3, 4, 5])

┌───┐
│ 1 │
└───┘
```

## Syntaxe SQL

```sql
ARRAYS_OVERLAP([1,2,3], [3,4,5])
```

## Exemples SQL

```sql
SELECT ARRAYS_OVERLAP([1, 2, 3], [3, 4, 5]);

┌───┐
│ 1 │
└───┘
```
