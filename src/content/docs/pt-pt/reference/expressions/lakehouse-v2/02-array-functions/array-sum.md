---
title: ARRAY_SUM (Lakehouse v2)
description: ARRAY_SUM — devolve a soma dos elementos de uma matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sum.md
---

Devolve a soma dos elementos de uma matriz.

## Sintaxe do Analyze

```python
func.array_sum([1, 2, 3, 4, 5])
```

## Exemplos do Analyze

```python
func.array_sum([10, 20, 30])

┌────┐
│ 60 │
└────┘
```

## Sintaxe SQL

```sql
ARRAY_SUM([1, 2, 3, 4, 5])
```

## Exemplos SQL

```sql
SELECT ARRAY_SUM([10, 20, 30]);

┌────┐
│ 60 │
└────┘
```
