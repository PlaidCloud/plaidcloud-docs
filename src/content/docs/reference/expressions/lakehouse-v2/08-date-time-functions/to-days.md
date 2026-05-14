---
title: TO_DAYS
description: "Learn how to use the TO_DAYS date/time function in PlaidCloud Lakehouse. Converts a date to a day count - see syntax, examples, and output."
---

Converts a date to a day count.

## Analyze Syntax

```python
func.to_days(<date>)
```

## Analyze Examples

```python
func.to_days('2024-01-01')

┌────────┐
│ 738886  │
└────────┘
```

## SQL Syntax

```sql
TO_DAYS(<date>)
```

## SQL Examples

```sql
SELECT TO_DAYS('2024-01-01');

┌────────┐
│ 738886  │
└────────┘
```
