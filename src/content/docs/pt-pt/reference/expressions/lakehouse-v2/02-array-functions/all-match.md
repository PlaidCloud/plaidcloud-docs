---
title: ALL_MATCH (Lakehouse v2)
description: ALL_MATCH — devolve TRUE se todos os elementos de uma matriz satisfizerem o predicado indicado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/all-match.md
---

Devolve TRUE se todos os elementos de uma matriz satisfizerem o predicado indicado.

## Sintaxe do Analyze

```python
func.all_match(get_column(table, 'arr'), lambda x: x > 0)
```

## Exemplos do Analyze

```python
func.all_match([1, 2, 3], lambda x: x > 0)

┌───┐
│ 1 │
└───┘
```

## Sintaxe SQL

```sql
ALL_MATCH(<arr>, lambda x: x > 0)
```

## Exemplos SQL

```sql
SELECT ALL_MATCH([1, 2, 3], x -> x > 0);

┌───┐
│ 1 │
└───┘
```
