---
title: ARRAY_FLATTEN
description: ARRAY_FLATTEN — Flattens nested arrays into a single-level array.
---

Flattens nested arrays into a single-level array.

## Analyze Syntax

```python
func.array_flatten([[1,2],[3,4]])
```

## Analyze Examples

```python
func.array_flatten([[1, 2], [3, 4]])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQL Syntax

```sql
ARRAY_FLATTEN([[1,2],[3,4]])
```

## SQL Examples

```sql
SELECT ARRAY_FLATTEN([[1, 2], [3, 4]]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
