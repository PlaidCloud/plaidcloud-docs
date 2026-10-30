---
title: ARRAY_CONCAT (Lakehouse v2)
description: ARRAY_CONCAT — Łączy wiele tablic w jedną tablicę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-concat.md
---

Łączy wiele tablic w jedną tablicę.

## Składnia Analyze

```python
func.array_concat([1, 2], [3, 4])
```

## Przykłady Analyze

```python
func.array_concat([1, 2], [3, 4])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## Składnia SQL

```sql
ARRAY_CONCAT([1, 2], [3, 4])
```

## Przykłady SQL

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
