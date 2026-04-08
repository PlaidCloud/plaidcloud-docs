---
title: DEGREES
description: "Learn how to use the DEGREES math function in PlaidCloud Lakehouse. Converts radians to degrees - see syntax, examples, and output."
---

Converts radians to degrees.

## Analyze Syntax

```python
func.degrees(<x>)
```

## Analyze Examples

```python
func.degrees(3.141592653589793)

┌───────┐
│ 180.0  │
└───────┘
```

## SQL Syntax

```sql
DEGREES(<x>)
```

## SQL Examples

```sql
SELECT DEGREES(PI());

┌───────┐
│ 180.0  │
└───────┘
```
