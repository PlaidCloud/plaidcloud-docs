---
title: ARRAYS_OVERLAP (Lakehouse v2)
description: ARRAYS_OVERLAP — verifica se dois arrays têm elementos em comum.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/arrays-overlap.md
---

Verifica se dois arrays têm elementos em comum.

## Sintaxe do Analyze

```python
func.arrays_overlap([1,2,3], [3,4,5])
```

## Exemplos do Analyze

```python
func.arrays_overlap([1, 2, 3], [3, 4, 5])

┌───┐
│ 1 │
└───┘
```

## Sintaxe SQL

```sql
ARRAYS_OVERLAP([1,2,3], [3,4,5])
```

## Exemplos SQL

```sql
SELECT ARRAYS_OVERLAP([1, 2, 3], [3, 4, 5]);

┌───┐
│ 1 │
└───┘
```
