---
title: ARRAY_DIFFERENCE (Lakehouse v2)
description: ARRAY_DIFFERENCE — renvoie un tableau des différences entre éléments consécutifs.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-difference.md
---

Renvoie un tableau des différences entre éléments consécutifs.

## Syntaxe Analyze

```python
func.array_difference([1, 3, 6, 10])
```

## Exemples Analyze

```python
func.array_difference([1, 3, 6, 10])

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```

## Syntaxe SQL

```sql
ARRAY_DIFFERENCE([1, 3, 6, 10])
```

## Exemples SQL

```sql
SELECT ARRAY_DIFFERENCE([1, 3, 6, 10]);

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```
