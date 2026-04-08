---
title: ASIN
description: "Learn how to use the ASIN math function in PlaidCloud Lakehouse. Returns the arc sine of a number in radians - see syntax, examples, and output."
---

Returns the arc sine of a number in radians.

## Analyze Syntax

```python
func.asin(<x>)
```

## Analyze Examples

```python
func.asin(0.5)

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```

## SQL Syntax

```sql
ASIN(<x>)
```

## SQL Examples

```sql
SELECT ASIN(0.5);

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```
