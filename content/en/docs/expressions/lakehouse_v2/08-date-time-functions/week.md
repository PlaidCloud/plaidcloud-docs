---
title: WEEK
description: "Learn how to use the WEEK date/time function in PlaidCloud Lakehouse. Returns the week number of the year for a date - see syntax, examples, and output."
---

Returns the week number of the year for a date.

## Analyze Syntax

```python
func.week(<date>[, <mode>])
```

## Analyze Examples

```python
func.week('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQL Syntax

```sql
WEEK(<date>[, <mode>])
```

## SQL Examples

```sql
SELECT WEEK('2024-06-15');

┌────┐
│ 24  │
└────┘
```
