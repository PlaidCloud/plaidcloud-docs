---
title: ARRAY_DIFFERENCE (Lakehouse v2)
description: ARRAY_DIFFERENCE — zwraca tablicę różnic między kolejnymi elementami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-difference.md
---

Zwraca tablicę różnic między kolejnymi elementami.

## Składnia Analyze

```python
func.array_difference([1, 3, 6, 10])
```

## Przykłady Analyze

```python
func.array_difference([1, 3, 6, 10])

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```

## Składnia SQL

```sql
ARRAY_DIFFERENCE([1, 3, 6, 10])
```

## Przykłady SQL

```sql
SELECT ARRAY_DIFFERENCE([1, 3, 6, 10]);

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```
