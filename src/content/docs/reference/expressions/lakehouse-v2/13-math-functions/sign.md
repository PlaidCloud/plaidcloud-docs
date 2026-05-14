---
title: SIGN
description: "Learn how to use the SIGN math function in PlaidCloud Lakehouse. Returns the sign of a number: -1, 0, or 1 - see syntax, examples, and output."
---

Returns the sign of a number: -1, 0, or 1.

## Analyze Syntax

```python
func.sign(<x>)
```

## Analyze Examples

```python
func.sign(-42)

┌────┐
│ -1  │
└────┘
```

## SQL Syntax

```sql
SIGN(<x>)
```

## SQL Examples

```sql
SELECT SIGN(-42);

┌────┐
│ -1  │
└────┘
```
