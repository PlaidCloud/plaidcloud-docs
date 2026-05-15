---
title: WEEKS_DIFF (Lakehouse v2)
description: WEEKS_DIFF — returns the number of weeks between two dates.
---

Returns the number of weeks between two dates.

## Analyze Syntax

```python
func.weeks_diff(<end_date>, <start_date>)
```

## Analyze Examples

```python
func.weeks_diff('2024-03-01', '2024-01-01')

┌───┐
│ 8  │
└───┘
```

## SQL Syntax

```sql
WEEKS_DIFF(<end_date>, <start_date>)
```

## SQL Examples

```sql
SELECT WEEKS_DIFF('2024-03-01', '2024-01-01');

┌───┐
│ 8  │
└───┘
```
