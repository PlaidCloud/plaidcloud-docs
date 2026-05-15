---
title: DEGREES (Lakehouse v2)
description: DEGREES — converts radians to degrees.
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
