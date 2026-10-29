---
title: ARRAY_TOP_N (Lakehouse v2)
description: ARRAY_TOP_N — zwraca N największych elementów tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-top-n.md
---

Zwraca N największych elementów tablicy.

## Składnia Analyze

```python
func.array_top_n([3,1,4,1,5], 3)
```

## Przykłady Analyze

```python
func.array_top_n([3, 1, 4, 1, 5], 3)

┌─────────┐
│ [5,4,3] │
└─────────┘
```

## Składnia SQL

```sql
ARRAY_TOP_N([3,1,4,1,5], 3)
```

## Przykłady SQL

```sql
SELECT ARRAY_TOP_N([3, 1, 4, 1, 5], 3);

┌─────────┐
│ [5,4,3] │
└─────────┘
```
