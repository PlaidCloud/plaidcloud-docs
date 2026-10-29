---
title: ARRAY_REMOVE (Lakehouse v2)
description: ARRAY_REMOVE — usuwa z tablicy wszystkie wystąpienia wskazanego elementu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-remove.md
---

Usuwa z tablicy wszystkie wystąpienia wskazanego elementu.

## Składnia Analyze

```python
func.array_remove([1, 2, 3, 2, 1], 2)
```

## Przykłady Analyze

```python
func.array_remove([1, 2, 3, 2, 1], 2)

┌─────────┐
│ [1,3,1] │
└─────────┘
```

## Składnia SQL

```sql
ARRAY_REMOVE([1, 2, 3, 2, 1], 2)
```

## Przykłady SQL

```sql
SELECT ARRAY_REMOVE([1, 2, 3, 2, 1], 2);

┌─────────┐
│ [1,3,1] │
└─────────┘
```
