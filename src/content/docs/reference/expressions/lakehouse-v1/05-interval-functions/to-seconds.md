---
title: TO_SECONDS
description: "Learn how to use the TO_SECONDS interval function in PlaidCloud Lakehouse. Converts a specified number of seconds into an Interval type. Includes syntax and..."
---

Converts a specified number of seconds into an Interval type.

- Accepts positive integers, zero, and negative integers as input.

## Analyze Syntax

```python
func.to_seconds(<seconds>)
```

## Analyze Examples

```python
func.to_seconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_seconds(2)                                   │
├──────────────────────────────────────────────────────┤
│ 0:00:02                                              │
└──────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_SECONDS(<seconds>)
```

## Aliases

- [EPOCH](../epoch)

## Return Type

Interval (in the format `hh:mm:ss`).

## sQL Examples

```sql
SELECT TO_SECONDS(2), TO_SECONDS(0), TO_SECONDS((- 2));

┌─────────────────────────────────────────────────┐
│ to_seconds(2) │ to_seconds(0) │ to_seconds(- 2) │
├───────────────┼───────────────┼─────────────────┤
│ 0:00:02       │ 00:00:00      │ -0:00:02        │
└─────────────────────────────────────────────────┘
```
