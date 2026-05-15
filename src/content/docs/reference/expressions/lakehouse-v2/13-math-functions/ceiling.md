---
title: CEILING
description: CEILING — returns the smallest integer greater than or equal to a number. Alias for `CEIL`.
---

Returns the smallest integer greater than or equal to a number. Alias for `CEIL`.

## Analyze Syntax

```python
func.ceiling(<x>)
```

## Analyze Examples

```python
func.ceiling(3.2)

┌───┐
│ 4  │
└───┘
```

## SQL Syntax

```sql
CEILING(<x>)
```

## SQL Examples

```sql
SELECT CEILING(3.2);

┌───┐
│ 4  │
└───┘
```
