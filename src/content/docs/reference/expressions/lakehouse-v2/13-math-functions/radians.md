---
title: RADIANS
description: "Learn how to use the RADIANS math function in PlaidCloud Lakehouse. Converts degrees to radians - see syntax, examples, and output."
---

Converts degrees to radians.

## Analyze Syntax

```python
func.radians(<x>)
```

## Analyze Examples

```python
func.radians(180)

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```

## SQL Syntax

```sql
RADIANS(<x>)
```

## SQL Examples

```sql
SELECT RADIANS(180);

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```
