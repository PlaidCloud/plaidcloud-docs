---
title: LN (Lakehouse v2)
description: LN — returns the natural logarithm of a number.
---

Returns the natural logarithm of a number.

## Analyze Syntax

```python
func.ln(<x>)
```

## Analyze Examples

```python
func.ln(2.718281828459045)

┌─────┐
│ 1.0  │
└─────┘
```

## SQL Syntax

```sql
LN(<x>)
```

## SQL Examples

```sql
SELECT LN(EXP(1));

┌─────┐
│ 1.0  │
└─────┘
```
