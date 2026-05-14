---
title: ATAN
description: "Learn how to use the ATAN math function in PlaidCloud Lakehouse. Returns the arc tangent of a number in radians - see syntax, examples, and output."
---

Returns the arc tangent of a number in radians.

## Analyze Syntax

```python
func.atan(<x>)
```

## Analyze Examples

```python
func.atan(1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## SQL Syntax

```sql
ATAN(<x>)
```

## SQL Examples

```sql
SELECT ATAN(1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
