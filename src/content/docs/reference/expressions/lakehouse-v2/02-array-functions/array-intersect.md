---
title: ARRAY_INTERSECT (Lakehouse v2)
description: ARRAY_INTERSECT — returns the intersection of two arrays.
---

Returns the intersection of two arrays.

## Analyze Syntax

```python
func.array_intersect([1,2,3], [2,3,4])
```

## Analyze Examples

```python
func.array_intersect([1, 2, 3], [2, 3, 4])

┌───────┐
│ [2,3] │
└───────┘
```

## SQL Syntax

```sql
ARRAY_INTERSECT([1,2,3], [2,3,4])
```

## SQL Examples

```sql
SELECT ARRAY_INTERSECT([1, 2, 3], [2, 3, 4]);

┌───────┐
│ [2,3] │
└───────┘
```
