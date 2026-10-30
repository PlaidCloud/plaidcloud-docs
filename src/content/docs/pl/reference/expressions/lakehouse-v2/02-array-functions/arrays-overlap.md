---
title: ARRAYS_OVERLAP (Lakehouse v2)
description: ARRAYS_OVERLAP — sprawdza, czy dwie tablice mają jakiekolwiek wspólne elementy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/arrays-overlap.md
---

Sprawdza, czy dwie tablice mają jakiekolwiek wspólne elementy.

## Składnia Analyze

```python
func.arrays_overlap([1,2,3], [3,4,5])
```

## Przykłady Analyze

```python
func.arrays_overlap([1, 2, 3], [3, 4, 5])

┌───┐
│ 1 │
└───┘
```

## Składnia SQL

```sql
ARRAYS_OVERLAP([1,2,3], [3,4,5])
```

## Przykłady SQL

```sql
SELECT ARRAYS_OVERLAP([1, 2, 3], [3, 4, 5]);

┌───┐
│ 1 │
└───┘
```
