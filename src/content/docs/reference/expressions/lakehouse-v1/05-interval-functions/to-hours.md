---
title: TO_HOURS
description: TO_HOURS — Converts a specified number of hours into an Interval type.
---

Converts a specified number of hours into an Interval type.

- Accepts positive integers, zero, and negative integers as input.

## Analyze Syntax

```python
func.to_hours(<hours>)
```

## Analyze Examples

```python
func.to_hours(2)
┌──────────────────────────────────────────────────────┐
│ func.to_hours(2)                                     │
├──────────────────────────────────────────────────────┤
│ 2:00:00                                              │
└──────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_HOURS(<hours>)
```

## Return Type

Interval (in the format `hh:mm:ss`).

## SQL Examples

```sql
SELECT TO_HOURS(2), TO_HOURS(0), TO_HOURS((- 2));

┌───────────────────────────────────────────┐
│ to_hours(2) │ to_hours(0) │ to_hours(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 2:00:00     │ 00:00:00    │ -2:00:00      │
└───────────────────────────────────────────┘
```
