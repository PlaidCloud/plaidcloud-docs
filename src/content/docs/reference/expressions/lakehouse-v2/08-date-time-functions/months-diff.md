---
title: MONTHS_DIFF
description: MONTHS_DIFF — returns the number of months between two dates.
---

Returns the number of months between two dates.

## Analyze Syntax

```python
func.months_diff(<end_date>, <start_date>)
```

## Analyze Examples

```python
func.months_diff('2024-06-01', '2024-01-01')

┌───┐
│ 5  │
└───┘
```

## SQL Syntax

```sql
MONTHS_DIFF(<end_date>, <start_date>)
```

## SQL Examples

```sql
SELECT MONTHS_DIFF('2024-06-01', '2024-01-01');

┌───┐
│ 5  │
└───┘
```
