---
title: ARRAY_SORT
description: "Learn how to use the ARRAY_SORT array function in PlaidCloud Lakehouse. Sorts the elements of an array in ascending order - with syntax and examples."
---

Sorts the elements of an array in ascending order.

## Analyze Syntax

```python
func.array_sort([3, 1, 4, 1, 5])
```

## Analyze Examples

```python
func.array_sort([3, 1, 4, 1, 5])

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```

## SQL Syntax

```sql
ARRAY_SORT([3, 1, 4, 1, 5])
```

## SQL Examples

```sql
SELECT ARRAY_SORT([3, 1, 4, 1, 5]);

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```
