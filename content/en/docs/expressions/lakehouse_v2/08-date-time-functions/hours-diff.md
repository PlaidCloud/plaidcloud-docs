---
title: HOURS_DIFF
description: "Learn how to use the HOURS_DIFF date/time function in PlaidCloud Lakehouse. Returns the number of hours between two datetimes - with syntax and examples."
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
