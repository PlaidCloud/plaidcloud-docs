---
title: ARRAY_REPEAT
description: "Learn how to use the ARRAY_REPEAT array function in PlaidCloud Lakehouse. Creates an array containing a specified element repeated N times."
---

Creates an array containing a specified element repeated N times.

## Analyze Syntax

```python
func.array_repeat('x', 3)
```

## Analyze Examples

```python
func.array_repeat('x', 3)

┌───────────────┐
│ ['x','x','x'] │
└───────────────┘
```

## SQL Syntax

```sql
ARRAY_REPEAT('x', 3)
```

## SQL Examples

```sql
SELECT ARRAY_REPEAT('x', 3);

┌───────────────┐
│ ["x","x","x"] │
└───────────────┘
```
