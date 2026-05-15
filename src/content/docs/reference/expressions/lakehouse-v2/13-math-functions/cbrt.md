---
title: CBRT (Lakehouse v2)
description: CBRT — returns the cube root of a number.
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
