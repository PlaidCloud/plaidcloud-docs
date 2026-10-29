---
title: ARRAY_REMOVE_LAST (Lakehouse v1)
description: "ARRAY_REMOVE_LAST : supprime le dernier élément du tableau."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-remove-last.md
---

Supprime le dernier élément du tableau.

## Syntaxe Analyze

```python
func.array_remove_last( <array> )
```

## Exemples Analyze

```python
func.array_remove_last([1, 2, 3]) 

┌────────────────────────────────────┐
│ func.array_remove_last([1, 2, 3])  │
├────────────────────────────────────┤
│ [1,2]                              │
└────────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_REMOVE_LAST( <array> )
```

## Exemples SQL

```sql
SELECT ARRAY_REMOVE_LAST([1, 2, 3]);

┌──────────────────────────────┐
│ array_remove_last([1, 2, 3]) │
├──────────────────────────────┤
│ [1,2]                        │
└──────────────────────────────┘
```
