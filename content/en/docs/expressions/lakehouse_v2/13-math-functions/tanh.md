---
title: TANH
description: "Learn how to use the TANH math function in PlaidCloud Lakehouse. Returns the hyperbolic tangent of a number - see syntax, examples, and output."
---

Returns the hyperbolic tangent of a number.

## Analyze Syntax

```python
func.tanh(<x>)
```

## Analyze Examples

```python
func.tanh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQL Syntax

```sql
TANH(<x>)
```

## SQL Examples

```sql
SELECT TANH(0);

┌─────┐
│ 0.0  │
└─────┘
```
