---
title: ARRAY_SORT (Lakehouse v2)
description: ARRAY_SORT — trie les éléments d'un tableau par ordre croissant.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sort.md
---

Trie les éléments d'un tableau par ordre croissant.

## Syntaxe Analyze

```python
func.array_sort([3, 1, 4, 1, 5])
```

## Exemples Analyze

```python
func.array_sort([3, 1, 4, 1, 5])

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```

## Syntaxe SQL

```sql
ARRAY_SORT([3, 1, 4, 1, 5])
```

## Exemples SQL

```sql
SELECT ARRAY_SORT([3, 1, 4, 1, 5]);

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```
