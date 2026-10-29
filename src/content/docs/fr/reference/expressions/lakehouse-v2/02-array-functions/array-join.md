---
title: ARRAY_JOIN (Lakehouse v2)
description: ARRAY_JOIN — concatène les éléments d'un tableau en une chaîne avec un séparateur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-join.md
---

Concatène les éléments d'un tableau en une chaîne avec un séparateur.

## Syntaxe Analyze

```python
func.array_join([1,2,3], '-')
```

## Exemples Analyze

```python
func.array_join(['a', 'b', 'c'], '-')

┌─────────┐
│ 'a-b-c' │
└─────────┘
```

## Syntaxe SQL

```sql
ARRAY_JOIN([1,2,3], '-')
```

## Exemples SQL

```sql
SELECT ARRAY_JOIN(['a', 'b', 'c'], '-');

┌───────┐
│ a-b-c │
└───────┘
```
