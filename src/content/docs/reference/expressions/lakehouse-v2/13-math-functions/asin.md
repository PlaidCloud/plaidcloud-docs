---
title: ASIN (Lakehouse v2)
description: ASIN — returns the arc sine of a number in radians.
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
