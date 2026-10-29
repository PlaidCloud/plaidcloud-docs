---
title: ARRAY_INDEXOF (Lakehouse v1)
description: "ARRAY_INDEXOF : renvoie l'indice (base 1) d'un élément si le tableau contient cet élément."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-indexof.md
---

Renvoie l'indice (base 1) d'un élément si le tableau contient cet élément.

## Syntaxe Analyze

```python
func.array_indexof( <array>, <element> )
```

## Exemples Analyze

```python
func.array_indexof([1, 2, 9], 9)

┌───────────────────────────────────┐
│ func.array_indexof([1, 2, 9], 9)  │
├───────────────────────────────────┤
│                                 3 │
└───────────────────────────────────┘
```

## Syntaxe SQL

```sql
ARRAY_INDEXOF( <array>, <element> )
```

## Exemples SQL

```sql
SELECT ARRAY_INDEXOF([1, 2, 9], 9);

┌─────────────────────────────┐
│ array_indexof([1, 2, 9], 9) │
├─────────────────────────────┤
│                           3 │
└─────────────────────────────┘
```
