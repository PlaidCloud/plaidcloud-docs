---
title: TO_CENTURIES
description: "Learn how to use the TO_CENTURIES interval function in PlaidCloud Lakehouse. Converts a specified number of centuries into an Interval type."
---

Converts a specified number of centuries into an Interval type.

- Accepts positive integers, zero, and negative integers as input.

## Analyze Syntax

```python
func.to_centuries(<centuries>)
```

## Analyze Examples

```python
func.to_centuries(2)
┌──────────────────────────────────────────────────────┐
│ func.to_centuries(2)                                 │
├──────────────────────────────────────────────────────┤
│ 200 years                                            │
└──────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
TO_CENTURIES(<centuries>)
```

## Return Type

Interval (represented in years).

## SQL Examples

```sql
SELECT TO_CENTURIES(2), TO_CENTURIES(0), TO_CENTURIES(-2);

┌───────────────────────────────────────────────────────┐
│ to_centuries(2) │ to_centuries(0) │ to_centuries(- 2) │
├─────────────────┼─────────────────┼───────────────────┤
│ 200 years       │ 00:00:00        │ -200 years        │
└───────────────────────────────────────────────────────┘
```