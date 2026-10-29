---
title: ARRAY_SLICE (Lakehouse v2)
description: ARRAY_SLICE — retorna uma fatia de um array a partir de uma posição inicial e com um comprimento determinado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-slice.md
---

Retorna uma fatia de um array a partir de uma posição inicial e com um comprimento determinado.

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
