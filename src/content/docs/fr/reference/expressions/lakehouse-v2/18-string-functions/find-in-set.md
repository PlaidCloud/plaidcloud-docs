---
title: FIND_IN_SET (Lakehouse v2)
description: FIND_IN_SET — renvoie la position d'une chaîne dans une liste séparée par des virgules.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/find-in-set.md
---

Renvoie la position d'une chaîne dans une liste séparée par des virgules.

## Syntaxe Analyze

```python
func.find_in_set(<str>, <strlist>)
```

## Exemples Analyze

```python
func.find_in_set('b', 'a,b,c')

┌───┐
│ 2  │
└───┘
```

## Syntaxe SQL

```sql
FIND_IN_SET(<str>, <strlist>)
```

## Exemples SQL

```sql
SELECT FIND_IN_SET('b', 'a,b,c');

┌───┐
│ 2  │
└───┘
```
