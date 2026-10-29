---
title: ARRAY_SORTBY (Lakehouse v2)
description: ARRAY_SORTBY — ordena os elementos de um array pelos elementos correspondentes de outro array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sortby.md
---

Ordena os elementos de um array pelos elementos correspondentes de outro array.

## Sintaxe do Analyze

```python
func.array_sortby(get_column(table, 'names'), get_column(table, 'scores'))
```

## Exemplos do Analyze

```python
func.array_sortby(['c','a','b'], [3,1,2])

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## Sintaxe SQL

```sql
ARRAY_SORTBY(<names>, <scores>)
```

## Exemplos SQL

```sql
SELECT ARRAY_SORTBY(['c','a','b'], [3,1,2]);

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
