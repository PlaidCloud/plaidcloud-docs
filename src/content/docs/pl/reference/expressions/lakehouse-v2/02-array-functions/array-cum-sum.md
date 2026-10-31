---
title: ARRAY_CUM_SUM (Lakehouse v2)
description: ARRAY_CUM_SUM — zwraca sumę skumulowaną elementów tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-cum-sum.md
---

Zwraca sumę skumulowaną elementów tablicy.

## Składnia Analyze

```python
func.array_cum_sum([1, 2, 3, 4])
```

## Przykłady Analyze

```python
func.array_cum_sum([1, 2, 3, 4])

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```

## Składnia SQL

```sql
ARRAY_CUM_SUM([1, 2, 3, 4])
```

## Przykłady SQL

```sql
SELECT ARRAY_CUM_SUM([1, 2, 3, 4]);

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```
