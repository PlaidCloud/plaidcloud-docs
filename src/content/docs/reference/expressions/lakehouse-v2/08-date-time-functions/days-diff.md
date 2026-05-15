---
title: DAYS_DIFF
description: DAYS_DIFF — returns the number of days between two dates - see syntax, examples, and output.
---

Returns the number of days between two dates.

## Analyze Syntax

```python
func.days_diff(<end_date>, <start_date>)
```

## Analyze Examples

```python
func.days_diff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## SQL Syntax

```sql
DAYS_DIFF(<end_date>, <start_date>)
```

## SQL Examples

```sql
SELECT DAYS_DIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```
