---
title: ARRAY_APPEND (Lakehouse v1)
description: "ARRAY_APPEND : ajoute un élément au début du tableau."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-append.md
---

Ajoute un élément au début du tableau.

## Syntaxe Analyze

```python
func.array_append( <array>, <element>)
```

## Exemples Analyze

```python
func.array_append([3, 4], 5)

┌──────────────────────────────┐
│ func.array_append([3, 4], 5) │
├──────────────────────────────┤
│ [3,4,5]                      │
└──────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_APPEND( <array>, <element>)
```

## Exemples SQL

```sql
SELECT ARRAY_APPEND([3, 4], 5);

┌─────────────────────────┐
│ array_append([3, 4], 5) │
├─────────────────────────┤
│ [3,4,5]                 │
└─────────────────────────┘
```
