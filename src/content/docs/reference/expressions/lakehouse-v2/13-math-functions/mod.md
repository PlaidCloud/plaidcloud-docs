---
title: MOD (Lakehouse v2)
description: MOD — returns the remainder of dividing two numbers.
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
