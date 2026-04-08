---
title: WEEKDAY
description: "Learn how to use the WEEKDAY date/time function in PlaidCloud Lakehouse. Returns the weekday index for a date (0=Monday, 6=Sunday) - with syntax and examples."
---

Returns the weekday index for a date (0=Monday, 6=Sunday).

## Analyze Syntax

```python
func.weekday(<date>)
```

## Analyze Examples

```python
func.weekday('2024-06-15')

┌───┐
│ 5  │
└───┘
```

## SQL Syntax

```sql
WEEKDAY(<date>)
```

## SQL Examples

```sql
SELECT WEEKDAY('2024-06-15');

┌───┐
│ 5  │
└───┘
```
