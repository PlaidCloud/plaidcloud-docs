---
title: SQRT
description: "Learn how to use the SQRT math function in PlaidCloud Lakehouse. Returns the square root of a number - see syntax, examples, and output."
---

Returns the square root of a number.

## Analyze Syntax

```python
func.sqrt(<x>)
```

## Analyze Examples

```python
func.sqrt(144)

┌──────┐
│ 12.0  │
└──────┘
```

## SQL Syntax

```sql
SQRT(<x>)
```

## SQL Examples

```sql
SELECT SQRT(144);

┌──────┐
│ 12.0  │
└──────┘
```
