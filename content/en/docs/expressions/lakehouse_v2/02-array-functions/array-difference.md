---
title: ARRAY_DIFFERENCE
description: "Learn how to use the ARRAY_DIFFERENCE array function in PlaidCloud Lakehouse. Returns an array of differences between consecutive elements."
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
