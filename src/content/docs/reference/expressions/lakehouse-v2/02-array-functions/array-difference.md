---
title: ARRAY_DIFFERENCE (Lakehouse v2)
description: ARRAY_DIFFERENCE — returns an array of differences between consecutive elements.
---

Returns an array of differences between consecutive elements.

## Analyze Syntax

```python
func.array_difference([1, 3, 6, 10])
```

## Analyze Examples

```python
func.array_difference([1, 3, 6, 10])

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```

## SQL Syntax

```sql
ARRAY_DIFFERENCE([1, 3, 6, 10])
```

## SQL Examples

```sql
SELECT ARRAY_DIFFERENCE([1, 3, 6, 10]);

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```
