---
title: "REVERSE (tableau, Lakehouse v2)"
description: REVERSE — renvoie un tableau dont les éléments sont dans l'ordre inverse.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/reverse.md
---

Renvoie un tableau dont les éléments sont dans l'ordre inverse.

## Syntaxe Analyze

```python
func.reverse([1, 2, 3])
```

## Exemples Analyze

```python
func.reverse([1, 2, 3])

┌─────────┐
│ [3,2,1] │
└─────────┘
```

## Syntaxe SQL

```sql
REVERSE([1, 2, 3])
```

## Exemples SQL

```sql
SELECT ARRAY_REVERSE([1, 2, 3]);

┌─────────┐
│ [3,2,1] │
└─────────┘
```
