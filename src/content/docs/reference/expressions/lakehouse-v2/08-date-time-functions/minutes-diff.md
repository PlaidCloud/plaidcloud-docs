---
title: MINUTES_DIFF (Lakehouse v2)
description: MINUTES_DIFF — returns the number of minutes between two datetimes.
---

Returns the number of minutes between two datetimes.

## Analyze Syntax

```python
func.minutes_diff(<end>, <start>)
```

## Analyze Examples

```python
func.minutes_diff('2024-01-01 11:00:00', '2024-01-01 10:00:00')

┌────┐
│ 60  │
└────┘
```

## SQL Syntax

```sql
MINUTES_DIFF(<end>, <start>)
```

## SQL Examples

```sql
SELECT MINUTES_DIFF('2024-01-01 11:00:00', '2024-01-01 10:00:00');

┌────┐
│ 60  │
└────┘
```
