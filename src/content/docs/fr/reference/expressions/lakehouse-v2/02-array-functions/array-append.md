---
title: ARRAY_APPEND (Lakehouse v2)
description: ARRAY_APPEND — ajoute un élément à la fin d'un tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-append.md
---

Ajoute un élément à la fin d'un tableau.

## Syntaxe Analyze

```python
func.array_append([1, 2, 3], 4)
```

## Exemples Analyze

```python
func.array_append([1, 2, 3], 4)

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## Syntaxe SQL

```sql
ARRAY_APPEND([1, 2, 3], 4)
```

## Exemples SQL

```sql
SELECT ARRAY_APPEND([1, 2, 3], 4);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
