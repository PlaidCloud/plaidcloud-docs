---
title: TO_MINUTES
description: "Learn how to use the TO_MINUTES interval function in PlaidCloud Lakehouse. Converts a specified number of minutes into an Interval type. Includes syntax and..."
---

Converts a specified number of minutes into an Interval type.

- Accepts positive integers, zero, and negative integers as input.

## Analyze Syntax

```python
func.to_minutes(<minutes>)
```

## Analyze Examples

```python
func.to_minutes(2)
┌──────────────────────────────────────────────────────┐
│ func.to_minutes(2)                                   │
├──────────────────────────────────────────────────────┤
│ 0:02:00                                              │
└──────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_MINUTES(<minutes>)
```

## Return Type

Interval (in the format `hh:mm:ss`).

## SQL Examples

```sql
SELECT TO_MINUTES(2), TO_MINUTES(0), TO_MINUTES((- 2));

┌─────────────────────────────────────────────────┐
│ to_minutes(2) │ to_minutes(0) │ to_minutes(- 2) │
├───────────────┼───────────────┼─────────────────┤
│ 0:02:00       │ 00:00:00      │ -0:02:00        │
└─────────────────────────────────────────────────┘
```