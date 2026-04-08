---
title: TO_DECADES
description: "Learn how to use the TO_DECADES interval function in PlaidCloud Lakehouse. Converts a specified number of decades into an Interval type. Includes syntax and..."
---

Converts a specified number of decades into an Interval type.

- Accepts positive integers, zero, and negative integers as input.

## Analyze Syntax

```python
func.to_decades(<decades>)
```

## Analyze Examples

```python
func.to_decades(2)
┌──────────────────────────────────────────────────────┐
│ func.to_decades(2)                                   │
├──────────────────────────────────────────────────────┤
│ 20 years                                             │
└──────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_DECADES(<decades>)
```

## Return Type

Interval (represented in years).

## SQL Examples

```sql
SELECT TO_DECADES(2), TO_DECADES(0), TO_DECADES((- 2));

┌─────────────────────────────────────────────────┐
│ to_decades(2) │ to_decades(0) │ to_decades(- 2) │
├───────────────┼───────────────┼─────────────────┤
│ 20 years      │ 00:00:00      │ -20 years       │
└─────────────────────────────────────────────────┘
```