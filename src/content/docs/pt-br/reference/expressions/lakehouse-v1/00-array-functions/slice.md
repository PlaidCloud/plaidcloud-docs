---
title: SLICE (Lakehouse v1)
description: SLICE extrai uma fatia do array pelo índice (base 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/slice.md
---

Extrai uma fatia do array pelo índice (base 1).

## Sintaxe do Analyze

```python
func.slice( <array>, <start>[, <end>] )
```

## Exemplos do Analyze

```python
func.slice([1, 21, 32, 4], 2, 3)

┌──────────────────────────────────┐
│ func.slice([1, 21, 32, 4], 2, 3) │
├──────────────────────────────────┤
│ [21,32]                          │ 
└──────────────────────────────────┘
```

## Sintaxe SQL

```sql
SLICE( <array>, <start>[, <end>] )
```

## Aliases

- [ARRAY_SLICE](../array-slice)

## Exemplos de SQL

```sql
SELECT ARRAY_SLICE([1, 21, 32, 4], 2, 3), SLICE([1, 21, 32, 4], 2, 3);

┌─────────────────────────────────────────────────────────────────┐
│ array_slice([1, 21, 32, 4], 2, 3) │ slice([1, 21, 32, 4], 2, 3) │
├───────────────────────────────────┼─────────────────────────────┤
│ [21,32]                           │ [21,32]                     │
└─────────────────────────────────────────────────────────────────┘
```
