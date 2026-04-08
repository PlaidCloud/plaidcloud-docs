---
title: MILLISECONDS_DIFF
description: "Learn how to use the MILLISECONDS_DIFF date/time function in PlaidCloud Lakehouse. Returns the number of milliseconds between two datetimes."
---

Returns the number of milliseconds between two datetimes.

## Analyze Syntax

```python
func.milliseconds_diff(<end>, <start>)
```

## Analyze Examples

```python
func.milliseconds_diff('2024-01-01 00:00:01', '2024-01-01 00:00:00')

┌──────┐
│ 1000  │
└──────┘
```

## SQL Syntax

```sql
MILLISECONDS_DIFF(<end>, <start>)
```

## SQL Examples

```sql
SELECT MILLISECONDS_DIFF('2024-01-01 00:00:01', '2024-01-01 00:00:00');

┌──────┐
│ 1000  │
└──────┘
```
