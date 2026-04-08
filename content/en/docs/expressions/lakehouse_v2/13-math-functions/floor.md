---
title: FLOOR
description: "Learn how to use the FLOOR math function in PlaidCloud Lakehouse. Returns the largest integer less than or equal to a number - with syntax and examples."
---

Returns the largest integer less than or equal to a number.

## Analyze Syntax

```python
func.floor(<x>)
```

## Analyze Examples

```python
func.floor(3.7)

┌───┐
│ 3  │
└───┘
```

## SQL Syntax

```sql
FLOOR(<x>)
```

## SQL Examples

```sql
SELECT FLOOR(3.7);

┌───┐
│ 3  │
└───┘
```
