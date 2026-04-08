---
title: MOD
description: "Learn how to use the MOD math function in PlaidCloud Lakehouse. Returns the remainder of dividing two numbers - see syntax, examples, and output."
---

Returns the remainder of dividing two numbers.

## Analyze Syntax

```python
func.mod(<x>, <y>)
```

## Analyze Examples

```python
func.mod(10, 3)

┌───┐
│ 1  │
└───┘
```

## SQL Syntax

```sql
MOD(<x>, <y>)
```

## SQL Examples

```sql
SELECT MOD(10, 3);

┌───┐
│ 1  │
└───┘
```
