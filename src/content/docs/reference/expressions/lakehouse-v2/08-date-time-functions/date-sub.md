---
title: DATE_SUB
description: "Learn how to use the DATE_SUB date/time function in PlaidCloud Lakehouse. Subtracts a specified time interval from a date or datetime."
---

Subtracts a specified time interval from a date or datetime.

## Analyze Syntax

```python
func.date_sub(<date>, INTERVAL <n> <unit>)
```

## Analyze Examples

```python
func.date_sub('2024-03-01', text('INTERVAL 1 MONTH'))

┌──────────────┐
│ '2024-02-01'  │
└──────────────┘
```

## SQL Syntax

```sql
DATE_SUB(<date>, INTERVAL <n> <unit>)
```

## SQL Examples

```sql
SELECT DATE_SUB('2024-03-01', INTERVAL 1 MONTH);

┌────────────┐
│ 2024-02-01  │
└────────────┘
```
