---
title: ARRAY_SORT (Lakehouse v2)
description: ARRAY_SORT — sortuje elementy tablicy w kolejności rosnącej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sort.md
---

Sortuje elementy tablicy w kolejności rosnącej.

## Składnia Analyze

```python
func.array_sort([3, 1, 4, 1, 5])
```

## Przykłady Analyze

```python
func.array_sort([3, 1, 4, 1, 5])

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```

## Składnia SQL

```sql
ARRAY_SORT([3, 1, 4, 1, 5])
```

## Przykłady SQL

```sql
SELECT ARRAY_SORT([3, 1, 4, 1, 5]);

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```
