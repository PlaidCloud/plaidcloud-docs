---
title: ARRAY_SORTBY (Lakehouse v2)
description: ARRAY_SORTBY — trie les éléments d'un tableau selon les éléments correspondants d'un autre tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sortby.md
---

Trie les éléments d'un tableau selon les éléments correspondants d'un autre tableau.

## Syntaxe Analyze

```python
func.array_sortby(get_column(table, 'names'), get_column(table, 'scores'))
```

## Exemples Analyze

```python
func.array_sortby(['c','a','b'], [3,1,2])

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## Syntaxe SQL

```sql
ARRAY_SORTBY(<names>, <scores>)
```

## Exemples SQL

```sql
SELECT ARRAY_SORTBY(['c','a','b'], [3,1,2]);

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
