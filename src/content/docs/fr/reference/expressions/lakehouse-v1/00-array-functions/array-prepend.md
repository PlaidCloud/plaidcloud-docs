---
title: ARRAY_PREPEND (Lakehouse v1)
description: "ARRAY_PREPEND : ajoute un élément au début du tableau."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-prepend.md
---

Ajoute un élément au début du tableau.

## Syntaxe Analyze

```python
func.array_prepend( <element>, <array> )
```

## Exemples Analyze

```python
func.array_prepend(1, [3, 4])

┌────────────────────────────────┐
│ func.array_prepend(1, [3, 4])  │
├────────────────────────────────┤
│ [1,3,4]                        │
└────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_PREPEND( <element>, <array> )
```

## Exemples SQL

```sql
SELECT ARRAY_PREPEND(1, [3, 4]);

┌──────────────────────────┐
│ array_prepend(1, [3, 4]) │
├──────────────────────────┤
│ [1,3,4]                  │
└──────────────────────────┘
```
