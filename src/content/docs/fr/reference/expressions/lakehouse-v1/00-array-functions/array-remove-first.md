---
title: ARRAY_REMOVE_FIRST (Lakehouse v1)
description: "ARRAY_REMOVE_FIRST : supprime le premier élément du tableau."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-remove-first.md
---

Supprime le premier élément du tableau.

## Syntaxe Analyze

```python
func.array_remove_first( <array> )
```

## Exemples Analyze

```python
func.array_remove_first([1, 2, 3]) 

┌─────────────────────────────────────┐
│ func.array_remove_first([1, 2, 3])  │
├─────────────────────────────────────┤
│ [2,3]                               │
└─────────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_REMOVE_FIRST( <array> )
```

## Exemples SQL

```sql
SELECT ARRAY_REMOVE_FIRST([1, 2, 3]);

┌───────────────────────────────┐
│ array_remove_first([1, 2, 3]) │
├───────────────────────────────┤
│ [2,3]                         │
└───────────────────────────────┘
```
