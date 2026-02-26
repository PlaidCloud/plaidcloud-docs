---
title: TO_DAYS
---

Converts a specified number of days into an Interval type.

- Accepts positive integers, zero, and negative integers as input.

## Analyze Syntax

```python
func.to_days(<days>)
```

## Analyze Examples

```python
func.to_days(2)
+------------------------------------------------------+
| func.to_days(2)                                      |
+------------------------------------------------------+
| 200 days                                             |
+------------------------------------------------------+
```

## SQL Syntax

```sql
TO_DAYS(<days>)
```

## Return Type

Interval (represented in days).

## SQL Examples

```sql
SELECT TO_DAYS(2), TO_DAYS(0), TO_DAYS(-2);

┌────────────────────────────────────────┐
│ to_days(2) │ to_days(0) │ to_days(- 2) │
├────────────┼────────────┼──────────────┤
│ 2 days     │ 00:00:00   │ -2 days      │
└────────────────────────────────────────┘
```