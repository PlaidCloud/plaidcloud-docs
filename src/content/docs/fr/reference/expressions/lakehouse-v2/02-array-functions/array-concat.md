---
title: ARRAY_CONCAT (Lakehouse v2)
description: ARRAY_CONCAT — concatène plusieurs tableaux en un seul tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-concat.md
---

Concatène plusieurs tableaux en un seul tableau.

## Syntaxe Analyze

```python
func.array_concat([1, 2], [3, 4])
```

## Exemples Analyze

```python
func.array_concat([1, 2], [3, 4])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## Syntaxe SQL

```sql
ARRAY_CONCAT([1, 2], [3, 4])
```

## Exemples SQL

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
