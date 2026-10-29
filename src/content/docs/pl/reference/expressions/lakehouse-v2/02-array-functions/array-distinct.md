---
title: ARRAY_DISTINCT (Lakehouse v2)
description: ARRAY_DISTINCT — usuwa zduplikowane elementy z tablicy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-distinct.md
---

Usuwa zduplikowane elementy z tablicy.

## Składnia Analyze

```python
func.array_distinct([1, 2, 2, 3, 3])
```

## Przykłady Analyze

```python
func.array_distinct([1, 2, 2, 3, 3])

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## Składnia SQL

```sql
ARRAY_DISTINCT([1, 2, 2, 3, 3])
```

## Przykłady SQL

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 3, 3]);

┌─────────┐
│ [1,2,3] │
└─────────┘
```
