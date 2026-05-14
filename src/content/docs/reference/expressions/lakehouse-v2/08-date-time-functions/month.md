---
title: MONTH
description: "Learn how to use the MONTH date/time function in PlaidCloud Lakehouse. Returns the month from a date - see syntax, examples, and output."
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
