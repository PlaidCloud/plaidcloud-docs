---
title: ARRAY_DISTINCT (Lakehouse v2)
description: ARRAY_DISTINCT — supprime les éléments en double d'un tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-distinct.md
---

Supprime les éléments en double d'un tableau.

## Syntaxe Analyze

```python
func.array_distinct([1, 2, 2, 3, 3])
```

## Exemples Analyze

```python
func.array_distinct([1, 2, 2, 3, 3])

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## Syntaxe SQL

```sql
ARRAY_DISTINCT([1, 2, 2, 3, 3])
```

## Exemples SQL

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 3, 3]);

┌─────────┐
│ [1,2,3] │
└─────────┘
```
