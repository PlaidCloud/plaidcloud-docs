---
title: FMOD
description: "Learn how to use the FMOD math function in PlaidCloud Lakehouse. Returns the floating-point remainder of dividing two numbers - with syntax and examples."
---

Returns the floating-point remainder of dividing two numbers.

## Analyze Syntax

```python
func.fmod(<x>, <y>)
```

## Analyze Examples

```python
func.fmod(10.5, 3.0)

┌─────┐
│ 1.5  │
└─────┘
```

## SQL Syntax

```sql
FMOD(<x>, <y>)
```

## SQL Examples

```sql
SELECT FMOD(10.5, 3.0);

┌─────┐
│ 1.5  │
└─────┘
```
