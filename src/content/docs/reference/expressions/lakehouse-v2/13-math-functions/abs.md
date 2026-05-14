---
title: ABS
description: "Learn how to use the ABS math function in PlaidCloud Lakehouse. Returns the absolute value of a number - see syntax, examples, and output."
---

Returns the absolute value of a number.

## Analyze Syntax

```python
func.abs(<x>)
```

## Analyze Examples

```python
func.abs(-5)

┌───┐
│ 5  │
└───┘
```

## SQL Syntax

```sql
ABS(<x>)
```

## SQL Examples

```sql
SELECT ABS(-5);

┌───┐
│ 5  │
└───┘
```
