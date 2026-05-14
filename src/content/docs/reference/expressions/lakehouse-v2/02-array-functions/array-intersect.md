---
title: ARRAY_INTERSECT
description: "Learn how to use the ARRAY_INTERSECT array function in PlaidCloud Lakehouse. Returns the intersection of two arrays - see syntax, examples, and output."
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
