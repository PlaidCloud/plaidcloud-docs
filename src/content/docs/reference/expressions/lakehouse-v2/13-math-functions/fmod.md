---
title: FMOD (Lakehouse v2)
description: FMOD — Returns the floating-point remainder of dividing two numbers.
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
