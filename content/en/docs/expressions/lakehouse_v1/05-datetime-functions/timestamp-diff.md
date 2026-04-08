---
title: TIMESTAMP_DIFF
description: "Learn how to use the TIMESTAMP_DIFF datetime function in PlaidCloud Lakehouse. Calculates the difference between two timestamps and returns the result as an..."
---

Calculates the difference between two timestamps and returns the result as an INTERVAL.

## Analyze Syntax

```python
func.timestamp_diff(<timestamp1>, <timestamp2>)
```

## Analyze Examples

```python
func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TIMESTAMP_DIFF(<timestamp1>, <timestamp2>)
```

## Return Type

INTERVAL (formatted as `hours:minutes:seconds`).

## SQL Examples

This example shows that the time difference between February 1, 2025, and January 1, 2025, is 744 hours, corresponding to 31 days:

```sql
SELECT TIMESTAMP_DIFF('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP);

┌──────────────────────────────────────────────────────────────────┐
│ timestamp_diff('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP) │
├──────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                        │
└──────────────────────────────────────────────────────────────────┘
```