---
title: PMOD
description: "Learn how to use the PMOD math function in PlaidCloud Lakehouse. Returns the positive modulus of dividing two numbers - see syntax, examples, and output."
---

Returns the positive modulus of dividing two numbers.

## Analyze Syntax

```python
func.pmod(<x>, <y>)
```

## Analyze Examples

```python
func.pmod(-10, 3)

┌───┐
│ 2  │
└───┘
```

## SQL Syntax

```sql
PMOD(<x>, <y>)
```

## SQL Examples

```sql
SELECT PMOD(-10, 3);

┌───┐
│ 2  │
└───┘
```
