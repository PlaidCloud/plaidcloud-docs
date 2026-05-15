---
title: ATAN2 (Lakehouse v2)
description: ATAN2 — returns the arc tangent of y/x, using the signs to determine the quadrant.
---

Returns the arc tangent of y/x, using the signs to determine the quadrant.

## Analyze Syntax

```python
func.atan2(<y>, <x>)
```

## Analyze Examples

```python
func.atan2(1, 1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## SQL Syntax

```sql
ATAN2(<y>, <x>)
```

## SQL Examples

```sql
SELECT ATAN2(1, 1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
