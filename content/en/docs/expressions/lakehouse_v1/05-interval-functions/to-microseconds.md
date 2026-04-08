---
title: TO_MICROSECONDS
description: "Learn how to use the TO_MICROSECONDS interval function in PlaidCloud Lakehouse. Converts a specified number of microseconds into an Interval type."
---

Converts a specified number of microseconds into an Interval type.

- Accepts positive integers, zero, and negative integers as input.

## Analyze Syntax

```python
func.to_microseconds(<microseconds>)
```

## Analyze Examples

```python
func.to_microseconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_microseconds(2)                              │
├──────────────────────────────────────────────────────┤
│ 0:00:00.000002                                       │
└──────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_MICROSECONDS(<microseconds>)
```

## Return Type

Interval (in the format `hh:mm:ss.sssssss`).

## SQL Examples

```sql
SELECT TO_MICROSECONDS(2), TO_MICROSECONDS(0), TO_MICROSECONDS((- 2));

┌────────────────────────────────────────────────────────────────┐
│ to_microseconds(2) │ to_microseconds(0) │ to_microseconds(- 2) │
├────────────────────┼────────────────────┼──────────────────────┤
│ 0:00:00.000002     │ 00:00:00           │ -0:00:00.000002      │
└────────────────────────────────────────────────────────────────┘
```