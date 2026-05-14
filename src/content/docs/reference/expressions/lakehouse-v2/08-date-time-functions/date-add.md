---
title: DATE_ADD
description: "Learn how to use the DATE_ADD date/time function in PlaidCloud Lakehouse. Adds a specified time interval to a date or datetime - with syntax and examples."
---

Adds a specified time interval to a date or datetime.

## Analyze Syntax

```python
func.date_add(<date>, INTERVAL <n> <unit>)
```

## Analyze Examples

```python
func.date_add('2024-01-01', text('INTERVAL 30 DAY'))

┌──────────────┐
│ '2024-01-31'  │
└──────────────┘
```

## SQL Syntax

```sql
DATE_ADD(<date>, INTERVAL <n> <unit>)
```

## SQL Examples

```sql
SELECT DATE_ADD('2024-01-01', INTERVAL 30 DAY);

┌────────────┐
│ 2024-01-31  │
└────────────┘
```
