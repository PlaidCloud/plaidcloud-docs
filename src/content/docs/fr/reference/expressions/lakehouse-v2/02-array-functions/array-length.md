---
title: ARRAY_LENGTH (Lakehouse v2)
description: ARRAY_LENGTH — renvoie le nombre d'éléments d'un tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-length.md
---

Renvoie le nombre d'éléments d'un tableau.

## Syntaxe Analyze

```python
func.array_length([1, 2, 3])
```

## Exemples Analyze

```python
func.array_length([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## Syntaxe SQL

```sql
ARRAY_LENGTH([1, 2, 3])
```

## Exemples SQL

```sql
SELECT ARRAY_LENGTH([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
