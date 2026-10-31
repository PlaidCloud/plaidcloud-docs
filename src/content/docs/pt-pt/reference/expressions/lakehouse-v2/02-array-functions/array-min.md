---
title: ARRAY_MIN (Lakehouse v2)
description: ARRAY_MIN — devolve o elemento mínimo de uma matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-min.md
---

Devolve o elemento mínimo de uma matriz.

## Sintaxe do Analyze

```python
func.array_min([3, 1, 4, 1, 5])
```

## Exemplos do Analyze

```python
func.array_min([3, 1, 4, 1, 5])

┌───┐
│ 1 │
└───┘
```

## Sintaxe SQL

```sql
ARRAY_MIN([3, 1, 4, 1, 5])
```

## Exemplos SQL

```sql
SELECT ARRAY_MIN([3, 1, 4, 1, 5]);

┌───┐
│ 1 │
└───┘
```
