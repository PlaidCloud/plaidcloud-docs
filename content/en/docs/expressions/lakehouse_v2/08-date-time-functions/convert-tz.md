---
title: CONVERT_TZ
description: "Learn how to use the CONVERT_TZ date/time function in PlaidCloud Lakehouse. Converts a datetime from one time zone to another - with syntax and examples."
---

Converts a datetime from one time zone to another.

## Analyze Syntax

```python
func.convert_tz(<datetime>, <from_tz>, <to_tz>)
```

## Analyze Examples

```python
func.convert_tz('2024-01-01 12:00:00', 'UTC', 'America/New_York')

┌───────────────────────┐
│ '2024-01-01 07:00:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
CONVERT_TZ(<datetime>, <from_tz>, <to_tz>)
```

## SQL Examples

```sql
SELECT CONVERT_TZ('2024-01-01 12:00:00', 'UTC', 'America/New_York');

┌─────────────────────┐
│ 2024-01-01 07:00:00  │
└─────────────────────┘
```
