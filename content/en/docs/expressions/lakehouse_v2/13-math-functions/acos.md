---
title: ACOS
description: "Learn how to use the ACOS math function in PlaidCloud Lakehouse. Returns the arc cosine of a number in radians - see syntax, examples, and output."
---

Returns the arc cosine of a number in radians.

## Analyze Syntax

```python
func.acos(<x>)
```

## Analyze Examples

```python
func.acos(0.5)

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```

## SQL Syntax

```sql
ACOS(<x>)
```

## SQL Examples

```sql
SELECT ACOS(0.5);

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```
