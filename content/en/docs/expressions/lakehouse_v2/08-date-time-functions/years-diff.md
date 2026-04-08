---
title: YEARS_DIFF
description: "Learn how to use the YEARS_DIFF date/time function in PlaidCloud Lakehouse. Returns the number of years between two dates - with syntax and examples."
---

Returns the number of years between two dates.

## Analyze Syntax

```python
func.years_diff(<end_date>, <start_date>)
```

## Analyze Examples

```python
func.years_diff('2029-01-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## SQL Syntax

```sql
YEARS_DIFF(<end_date>, <start_date>)
```

## SQL Examples

```sql
SELECT YEARS_DIFF('2029-01-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
