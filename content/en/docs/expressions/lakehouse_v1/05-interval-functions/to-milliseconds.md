---
title: TO_MILLISECONDS
description: "Learn how to use the TO_MILLISECONDS interval function in PlaidCloud Lakehouse. Converts a specified number of milliseconds into an Interval type."
---

Converts a specified number of milliseconds into an Interval type.

- Accepts positive integers, zero, and negative integers as input.

## Analyze Syntax

```python
func.to_milliseconds(<milliseconds>)
```

## Analyze Examples

```python
func.to_milliseconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_milliseconds(2)                              │
├──────────────────────────────────────────────────────┤
│  0:00:00.002                                         │
└──────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_MILLISECONDS(<milliseconds>)
```

## Return Type

Interval (in the format `hh:mm:ss.sss`).

## SQL Examples

```sql
SELECT TO_MILLISECONDS(2), TO_MILLISECONDS(0), TO_MILLISECONDS((- 2));

┌────────────────────────────────────────────────────────────────┐
│ to_milliseconds(2) │ to_milliseconds(0) │ to_milliseconds(- 2) │
├────────────────────┼────────────────────┼──────────────────────┤
│ 0:00:00.002        │ 00:00:00           │ -0:00:00.002         │
└────────────────────────────────────────────────────────────────┘
```