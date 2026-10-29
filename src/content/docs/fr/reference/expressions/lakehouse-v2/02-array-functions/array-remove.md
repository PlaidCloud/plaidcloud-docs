---
title: ARRAY_REMOVE (Lakehouse v2)
description: ARRAY_REMOVE — supprime toutes les occurrences d'un élément donné d'un tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-remove.md
---

Supprime toutes les occurrences d'un élément donné d'un tableau.

## Syntaxe Analyze

```python
func.array_remove([1, 2, 3, 2, 1], 2)
```

## Exemples Analyze

```python
func.array_remove([1, 2, 3, 2, 1], 2)

┌─────────┐
│ [1,3,1] │
└─────────┘
```

## Syntaxe SQL

```sql
ARRAY_REMOVE([1, 2, 3, 2, 1], 2)
```

## Exemples SQL

```sql
SELECT ARRAY_REMOVE([1, 2, 3, 2, 1], 2);

┌─────────┐
│ [1,3,1] │
└─────────┘
```
