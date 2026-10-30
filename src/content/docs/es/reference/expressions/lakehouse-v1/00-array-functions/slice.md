---
title: SLICE (Lakehouse v1)
description: SLICE — extrae un segmento del arreglo según el índice (base 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/slice.md
---

Extrae un segmento del arreglo según el índice (base 1).

## Sintaxis de Analyze

```python
func.slice( <array>, <start>[, <end>] )
```

## Ejemplos de Analyze

```python
func.slice([1, 21, 32, 4], 2, 3)

┌──────────────────────────────────┐
│ func.slice([1, 21, 32, 4], 2, 3) │
├──────────────────────────────────┤
│ [21,32]                          │ 
└──────────────────────────────────┘
```

## Sintaxis de SQL

```sql
SLICE( <array>, <start>[, <end>] )
```

## Alias

- [ARRAY_SLICE](../array-slice)

## Ejemplos de SQL

```sql
SELECT ARRAY_SLICE([1, 21, 32, 4], 2, 3), SLICE([1, 21, 32, 4], 2, 3);

┌─────────────────────────────────────────────────────────────────┐
│ array_slice([1, 21, 32, 4], 2, 3) │ slice([1, 21, 32, 4], 2, 3) │
├───────────────────────────────────┼─────────────────────────────┤
│ [21,32]                           │ [21,32]                     │
└─────────────────────────────────────────────────────────────────┘
```
