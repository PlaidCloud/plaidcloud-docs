---
title: CBRT
description: "Learn how to use the CBRT math function in PlaidCloud Lakehouse. Returns the cube root of a number - see syntax, examples, and output."
---

Returns the cube root of a number.

## Analyze Syntax

```python
func.cbrt(<x>)
```

## Analyze Examples

```python
func.cbrt(27)

┌─────┐
│ 3.0  │
└─────┘
```

## SQL Syntax

```sql
CBRT(<x>)
```

## SQL Examples

```sql
SELECT CBRT(27);

┌─────┐
│ 3.0  │
└─────┘
```
