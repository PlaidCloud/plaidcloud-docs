---
title: SECONDS_DIFF
---

Returns the number of seconds between two datetimes.

## Analyze Syntax

```python
func.seconds_diff(<end>, <start>)
```

## Analyze Examples

```python
func.seconds_diff('2024-01-01 00:01:30', '2024-01-01 00:00:00')

┌────┐
│ 90  │
└────┘
```

## SQL Syntax

```sql
SECONDS_DIFF(<end>, <start>)
```

## SQL Examples

```sql
SELECT SECONDS_DIFF('2024-01-01 00:01:30', '2024-01-01 00:00:00');

┌────┐
│ 90  │
└────┘
```
