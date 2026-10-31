---
title: ALL_MATCH (Lakehouse v2)
description: ALL_MATCH — renvoie TRUE si tous les éléments d'un tableau satisfont le prédicat donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/all-match.md
---

Renvoie TRUE si tous les éléments d'un tableau satisfont le prédicat donné.

## Syntaxe Analyze

```python
func.all_match(get_column(table, 'arr'), lambda x: x > 0)
```

## Exemples Analyze

```python
func.all_match([1, 2, 3], lambda x: x > 0)

┌───┐
│ 1 │
└───┘
```

## Syntaxe SQL

```sql
ALL_MATCH(<arr>, lambda x: x > 0)
```

## Exemples SQL

```sql
SELECT ALL_MATCH([1, 2, 3], x -> x > 0);

┌───┐
│ 1 │
└───┘
```
