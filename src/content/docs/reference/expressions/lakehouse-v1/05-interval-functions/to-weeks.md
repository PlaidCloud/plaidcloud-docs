---
title: TO_WEEKS
description: TO_WEEKS — Converts a specified number of weeks into an Interval type.
---

Converts a specified number of weeks into an Interval type.

- Accepts positive integers, zero, and negative integers as input.

## Analyze Syntax

```python
func.to_weeks(<weeks>)
```

## Analyze Examples

```python
func.to_weeks(2)
┌──────────────────────────────────────────────────────┐
│ func.to_weeks(2)                                     │
├──────────────────────────────────────────────────────┤
│ 14 days                                              │
└──────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_WEEKS(<weeks>)
```

## Return Type

Interval (represented in days).

## SQL Examples

```sql
SELECT TO_WEEKS(2), TO_WEEKS(0), TO_WEEKS((- 2));

┌───────────────────────────────────────────┐
│ to_weeks(2) │ to_weeks(0) │ to_weeks(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 14 days     │ 00:00:00    │ -14 days      │
└───────────────────────────────────────────┘
```
