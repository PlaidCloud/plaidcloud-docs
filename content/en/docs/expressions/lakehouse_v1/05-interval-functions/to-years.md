---
title: TO_YEARS
description: "Learn how to use the TO_YEARS interval function in PlaidCloud Lakehouse. Converts a specified number of years into an Interval type. With syntax and examples."
---

Converts a specified number of years into an Interval type.

- Accepts positive integers, zero, and negative integers as input.

## Analyze Syntax

```python
func.to_years(<years>)
```

## Analyze Examples

```python
func.to_years(2)
┌──────────────────────────────────────────────────────┐
│ func.to_years(2)                                     │
├──────────────────────────────────────────────────────┤
│ 2 years                                              │
└──────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_YEARS(<years>)
```

## Return Type

Interval (represented in years).

## SQL Examples

```sql
SELECT TO_YEARS(2), TO_YEARS(0), TO_YEARS((- 2));

┌───────────────────────────────────────────┐
│ to_years(2) │ to_years(0) │ to_years(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 2 years     │ 00:00:00    │ -2 years      │
└───────────────────────────────────────────┘
```