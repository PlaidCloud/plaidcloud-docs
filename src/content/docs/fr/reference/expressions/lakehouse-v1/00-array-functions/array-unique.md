---
title: ARRAY_UNIQUE (Lakehouse v1)
description: "ARRAY_UNIQUE : compte les éléments uniques du tableau (hors NULL)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-unique.md
---

Compte les éléments uniques du tableau (hors NULL).

## Syntaxe Analyze

```python
func.array_unique( <array> )
```

## Exemples Analyze

```python
func.array_unique([1, 2, 3, 3, 4])

┌─────────────────────────────────────┐
│ func.array_unique([1, 2, 3, 3, 4])  │
├─────────────────────────────────────┤
│                                   4 │
└─────────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_UNIQUE( <array> )
```

## Exemples SQL

```sql
SELECT ARRAY_UNIQUE([1, 2, 3, 3, 4]);

┌───────────────────────────────┐
│ array_unique([1, 2, 3, 3, 4]) │
├───────────────────────────────┤
│                             4 │
└───────────────────────────────┘
```
