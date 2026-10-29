---
title: ARRAY_TOP_N (Lakehouse v2)
description: ARRAY_TOP_N — retorna os N maiores elementos de um array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-top-n.md
---

Retorna os N maiores elementos de um array.

## Sintaxe do Analyze

```python
func.array_top_n([3,1,4,1,5], 3)
```

## Exemplos do Analyze

```python
func.array_top_n([3, 1, 4, 1, 5], 3)

┌─────────┐
│ [5,4,3] │
└─────────┘
```

## Sintaxe SQL

```sql
ARRAY_TOP_N([3,1,4,1,5], 3)
```

## Exemplos SQL

```sql
SELECT ARRAY_TOP_N([3, 1, 4, 1, 5], 3);

┌─────────┐
│ [5,4,3] │
└─────────┘
```
