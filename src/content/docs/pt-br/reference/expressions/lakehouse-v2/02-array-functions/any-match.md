---
title: ANY_MATCH (Lakehouse v2)
description: ANY_MATCH — retorna TRUE se algum elemento de um array satisfaz o predicado informado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/any-match.md
---

Retorna TRUE se algum elemento de um array satisfaz o predicado informado.

## Sintaxe do Analyze

```python
func.any_match(get_column(table, 'arr'), lambda x: x > 5)
```

## Exemplos do Analyze

```python
func.any_match([1, 2, 8], lambda x: x > 5)

┌───┐
│ 1 │
└───┘
```

## Sintaxe SQL

```sql
ANY_MATCH(<arr>, lambda x: x > 5)
```

## Exemplos SQL

```sql
SELECT ANY_MATCH([1, 2, 8], x -> x > 5);

┌───┐
│ 1 │
└───┘
```
