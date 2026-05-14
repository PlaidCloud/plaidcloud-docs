---
title: CEIL
description: "Learn how to use the CEIL math function in PlaidCloud Lakehouse. Returns the smallest integer greater than or equal to a number - with syntax and examples."
---

Returns the smallest integer greater than or equal to a number.

## Analyze Syntax

```python
func.ceil(<x>)
```

## Analyze Examples

```python
func.ceil(3.2)

┌───┐
│ 4  │
└───┘
```

## SQL Syntax

```sql
CEIL(<x>)
```

## SQL Examples

```sql
SELECT CEIL(3.2);

┌───┐
│ 4  │
└───┘
```
