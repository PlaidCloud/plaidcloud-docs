---
title: ARRAY_DIFFERENCE (Lakehouse v2)
description: ARRAY_DIFFERENCE — devolve uma matriz com as diferenças entre elementos consecutivos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-difference.md
---

Devolve uma matriz com as diferenças entre elementos consecutivos.

## Sintaxe do Analyze

```python
func.array_difference([1, 3, 6, 10])
```

## Exemplos do Analyze

```python
func.array_difference([1, 3, 6, 10])

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```

## Sintaxe SQL

```sql
ARRAY_DIFFERENCE([1, 3, 6, 10])
```

## Exemplos SQL

```sql
SELECT ARRAY_DIFFERENCE([1, 3, 6, 10]);

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```
