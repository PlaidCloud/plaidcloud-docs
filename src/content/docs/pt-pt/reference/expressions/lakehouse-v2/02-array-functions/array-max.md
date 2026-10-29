---
title: ARRAY_MAX (Lakehouse v2)
description: ARRAY_MAX — devolve o elemento máximo de uma matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-max.md
---

Devolve o elemento máximo de uma matriz.

## Sintaxe do Analyze

```python
func.array_max([3, 1, 4, 1, 5])
```

## Exemplos do Analyze

```python
func.array_max([3, 1, 4, 1, 5])

┌───┐
│ 5 │
└───┘
```

## Sintaxe SQL

```sql
ARRAY_MAX([3, 1, 4, 1, 5])
```

## Exemplos SQL

```sql
SELECT ARRAY_MAX([3, 1, 4, 1, 5]);

┌───┐
│ 5 │
└───┘
```
