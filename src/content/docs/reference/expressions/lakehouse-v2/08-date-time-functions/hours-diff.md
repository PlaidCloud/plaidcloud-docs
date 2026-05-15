---
title: HOURS_DIFF
description: HOURS_DIFF — returns the number of hours between two datetimes.
---

Returns the number of hours between two datetimes.

## Analyze Syntax

```python
func.hours_diff(<end>, <start>)
```

## Analyze Examples

```python
func.hours_diff('2024-01-02 10:00:00', '2024-01-01 10:00:00')

┌────┐
│ 24  │
└────┘
```

## SQL Syntax

```sql
HOURS_DIFF(<end>, <start>)
```

## SQL Examples

```sql
SELECT HOURS_DIFF('2024-01-02 10:00:00', '2024-01-01 10:00:00');

┌────┐
│ 24  │
└────┘
```
