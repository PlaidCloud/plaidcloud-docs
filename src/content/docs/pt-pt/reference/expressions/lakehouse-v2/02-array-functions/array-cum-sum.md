---
title: ARRAY_CUM_SUM (Lakehouse v2)
description: ARRAY_CUM_SUM — devolve a soma cumulativa dos elementos de uma matriz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-cum-sum.md
---

Devolve a soma cumulativa dos elementos de uma matriz.

## Sintaxe do Analyze

```python
func.array_cum_sum([1, 2, 3, 4])
```

## Exemplos do Analyze

```python
func.array_cum_sum([1, 2, 3, 4])

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```

## Sintaxe SQL

```sql
ARRAY_CUM_SUM([1, 2, 3, 4])
```

## Exemplos SQL

```sql
SELECT ARRAY_CUM_SUM([1, 2, 3, 4]);

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```
