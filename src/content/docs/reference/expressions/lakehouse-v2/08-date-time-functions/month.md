---
title: MONTH (Lakehouse v2)
description: MONTH — returns the month from a date.
---

Returns the month from a date.

## Analyze Syntax

```python
func.month(<date>)
```

## Analyze Examples

```python
func.month('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## SQL Syntax

```sql
MONTH(<date>)
```

## SQL Examples

```sql
SELECT MONTH('2024-06-15');

┌───┐
│ 6  │
└───┘
```
