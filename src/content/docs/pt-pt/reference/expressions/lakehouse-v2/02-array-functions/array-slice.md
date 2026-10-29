---
title: ARRAY_SLICE (Lakehouse v2)
description: ARRAY_SLICE — devolve um segmento de uma matriz a partir de uma posição inicial e com um determinado comprimento.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-slice.md
---

Devolve um segmento de uma matriz a partir de uma posição inicial e com um determinado comprimento.

## Sintaxe do Analyze

```python
func.array_slice([1,2,3,4,5], 2, 3)
```

## Exemplos do Analyze

```python
func.array_slice([1, 2, 3, 4, 5], 2, 3)

┌─────────┐
│ [2,3,4] │
└─────────┘
```

## Sintaxe SQL

```sql
ARRAY_SLICE([1,2,3,4,5], 2, 3)
```

## Exemplos SQL

```sql
SELECT ARRAY_SLICE([1, 2, 3, 4, 5], 2, 3);

┌─────────┐
│ [2,3,4] │
└─────────┘
```
