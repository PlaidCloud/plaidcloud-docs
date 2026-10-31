---
title: ARRAY_SLICE (Lakehouse v2)
description: ARRAY_SLICE — renvoie une tranche d'un tableau à partir d'une position de départ et sur une longueur donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-slice.md
---

Renvoie une tranche d'un tableau à partir d'une position de départ et sur une longueur donnée.

## Syntaxe Analyze

```python
func.array_slice([1,2,3,4,5], 2, 3)
```

## Exemples Analyze

```python
func.array_slice([1, 2, 3, 4, 5], 2, 3)

┌─────────┐
│ [2,3,4] │
└─────────┘
```

## Syntaxe SQL

```sql
ARRAY_SLICE([1,2,3,4,5], 2, 3)
```

## Exemples SQL

```sql
SELECT ARRAY_SLICE([1, 2, 3, 4, 5], 2, 3);

┌─────────┐
│ [2,3,4] │
└─────────┘
```
