---
title: SECONDS_DIFF
description: "Learn how to use the SECONDS_DIFF date/time function in PlaidCloud Lakehouse. Returns the number of seconds between two datetimes - with syntax and examples."
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
