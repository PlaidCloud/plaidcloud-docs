---
title: DAYOFYEAR
description: "Learn how to use the DAYOFYEAR date/time function in PlaidCloud Lakehouse. Returns the day of the year from a date - see syntax, examples, and output."
---

Returns the day of the year from a date.

## Analyze Syntax

```python
func.dayofyear(<date>)
```

## Analyze Examples

```python
func.dayofyear('2024-06-15')

┌─────┐
│ 167  │
└─────┘
```

## SQL Syntax

```sql
DAYOFYEAR(<date>)
```

## SQL Examples

```sql
SELECT DAYOFYEAR('2024-06-15');

┌─────┐
│ 167  │
└─────┘
```
