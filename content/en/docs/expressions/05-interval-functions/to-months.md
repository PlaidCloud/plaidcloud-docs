---
title: TO_MONTHS
---

Converts a specified number of months into an Interval type.

- Accepts positive integers, zero, and negative integers as input.

## Analyze Syntax

```python
func.to_months(<months>)
```

## Analyze Examples

```python
func.to_months(2)
+------------------------------------------------------+
| func.to_months(2)                                    |
+------------------------------------------------------+
| 2 months                                             |
+------------------------------------------------------+
```

## SQL Syntax

```sql
TO_MONTHS(<months>)
```

## Return Type

Interval (represented in months).

## SQL Examples

```sql
SELECT TO_MONTHS(2), TO_MONTHS(0), TO_MONTHS((- 2));

┌──────────────────────────────────────────────┐
│ to_months(2) │ to_months(0) │ to_months(- 2) │
├──────────────┼──────────────┼────────────────┤
│ 2 months     │ 00:00:00     │ -2 months      │
└──────────────────────────────────────────────┘
```