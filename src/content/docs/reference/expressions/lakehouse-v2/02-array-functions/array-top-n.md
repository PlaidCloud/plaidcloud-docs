---
title: ARRAY_TOP_N (Lakehouse v2)
description: ARRAY_TOP_N — returns the top N elements from an array.
---

Returns the top N elements from an array.

## Analyze Syntax

```python
func.array_top_n([3,1,4,1,5], 3)
```

## Analyze Examples

```python
func.array_top_n([3, 1, 4, 1, 5], 3)

┌─────────┐
│ [5,4,3] │
└─────────┘
```

## SQL Syntax

```sql
ARRAY_TOP_N([3,1,4,1,5], 3)
```

## SQL Examples

```sql
SELECT ARRAY_TOP_N([3, 1, 4, 1, 5], 3);

┌─────────┐
│ [5,4,3] │
└─────────┘
```
