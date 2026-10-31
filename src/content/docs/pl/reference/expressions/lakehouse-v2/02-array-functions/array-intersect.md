---
title: ARRAY_INTERSECT (Lakehouse v2)
description: ARRAY_INTERSECT — zwraca część wspólną dwóch tablic.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-intersect.md
---

Zwraca część wspólną dwóch tablic.

## Składnia Analyze

```python
func.array_intersect([1,2,3], [2,3,4])
```

## Przykłady Analyze

```python
func.array_intersect([1, 2, 3], [2, 3, 4])

┌───────┐
│ [2,3] │
└───────┘
```

## Składnia SQL

```sql
ARRAY_INTERSECT([1,2,3], [2,3,4])
```

## Przykłady SQL

```sql
SELECT ARRAY_INTERSECT([1, 2, 3], [2, 3, 4]);

┌───────┐
│ [2,3] │
└───────┘
```
