---
title: MULTIPLY
description: "Learn how to use the MULTIPLY math function in PlaidCloud Lakehouse. Returns the product of two numbers - see syntax, examples, and output."
---

Returns the product of two numbers.

## Analyze Syntax

```python
func.multiply(<x>, <y>)
```

## Analyze Examples

```python
func.multiply(6, 7)

┌────┐
│ 42  │
└────┘
```

## SQL Syntax

```sql
MULTIPLY(<x>, <y>)
```

## SQL Examples

```sql
SELECT MULTIPLY(6, 7);

┌────┐
│ 42  │
└────┘
```
