---
title: "REVERSE (Array, Lakehouse v2)"
description: REVERSE — zwraca tablicę z elementami w odwrotnej kolejności.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/reverse.md
---

Zwraca tablicę z elementami w odwrotnej kolejności.

## Składnia Analyze

```python
func.reverse([1, 2, 3])
```

## Przykłady Analyze

```python
func.reverse([1, 2, 3])

┌─────────┐
│ [3,2,1] │
└─────────┘
```

## Składnia SQL

```sql
REVERSE([1, 2, 3])
```

## Przykłady SQL

```sql
SELECT ARRAY_REVERSE([1, 2, 3]);

┌─────────┐
│ [3,2,1] │
└─────────┘
```
