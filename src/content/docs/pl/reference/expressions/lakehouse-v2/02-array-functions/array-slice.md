---
title: ARRAY_SLICE (Lakehouse v2)
description: ARRAY_SLICE — zwraca fragment tablicy od pozycji początkowej o podanej długości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-slice.md
---

Zwraca fragment tablicy od pozycji początkowej o podanej długości.

## Składnia Analyze

```python
func.array_slice([1,2,3,4,5], 2, 3)
```

## Przykłady Analyze

```python
func.array_slice([1, 2, 3, 4, 5], 2, 3)

┌─────────┐
│ [2,3,4] │
└─────────┘
```

## Składnia SQL

```sql
ARRAY_SLICE([1,2,3,4,5], 2, 3)
```

## Przykłady SQL

```sql
SELECT ARRAY_SLICE([1, 2, 3, 4, 5], 2, 3);

┌─────────┐
│ [2,3,4] │
└─────────┘
```
