---
title: ARRAY_SORT (Lakehouse v2)
description: ARRAY_SORT — ordena os elementos de uma matriz por ordem crescente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sort.md
---

Ordena os elementos de uma matriz por ordem crescente.

## Sintaxe do Analyze

```python
func.array_sort([3, 1, 4, 1, 5])
```

## Exemplos do Analyze

```python
func.array_sort([3, 1, 4, 1, 5])

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```

## Sintaxe SQL

```sql
ARRAY_SORT([3, 1, 4, 1, 5])
```

## Exemplos SQL

```sql
SELECT ARRAY_SORT([3, 1, 4, 1, 5]);

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```
