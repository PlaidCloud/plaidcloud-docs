---
title: WEEK_ISO
description: "Learn how to use the WEEK_ISO date/time function in PlaidCloud Lakehouse. Returns the ISO week number of the year for a date - with syntax and examples."
---

Returns the ISO week number of the year for a date.

## Analyze Syntax

```python
func.week_iso(<date>)
```

## Analyze Examples

```python
func.week_iso('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQL Syntax

```sql
WEEK_ISO(<date>)
```

## SQL Examples

```sql
SELECT WEEK_ISO('2024-06-15');

┌────┐
│ 24  │
└────┘
```
