---
title: ANY_MATCH (Lakehouse v2)
description: ANY_MATCH — renvoie TRUE si au moins un élément d'un tableau satisfait le prédicat donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/any-match.md
---

Renvoie TRUE si au moins un élément d'un tableau satisfait le prédicat donné.

## Syntaxe Analyze

```python
func.any_match(get_column(table, 'arr'), lambda x: x > 5)
```

## Exemples Analyze

```python
func.any_match([1, 2, 8], lambda x: x > 5)

┌───┐
│ 1 │
└───┘
```

## Syntaxe SQL

```sql
ANY_MATCH(<arr>, lambda x: x > 5)
```

## Exemples SQL

```sql
SELECT ANY_MATCH([1, 2, 8], x -> x > 5);

┌───┐
│ 1 │
└───┘
```
