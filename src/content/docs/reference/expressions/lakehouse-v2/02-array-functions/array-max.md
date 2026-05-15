---
title: ARRAY_MAX (Lakehouse v2)
description: ARRAY_MAX — returns the maximum element in an array.
---

Returns the maximum element in an array.

## Analyze Syntax

```python
func.array_max([3, 1, 4, 1, 5])
```

## Analyze Examples

```python
func.array_max([3, 1, 4, 1, 5])

┌───┐
│ 5 │
└───┘
```

## SQL Syntax

```sql
ARRAY_MAX([3, 1, 4, 1, 5])
```

## SQL Examples

```sql
SELECT ARRAY_MAX([3, 1, 4, 1, 5]);

┌───┐
│ 5 │
└───┘
```
