---
title: MINUTES_SUB
description: "Learn how to use the MINUTES_SUB date/time function in PlaidCloud Lakehouse. Subtracts a specified number of minutes from a datetime - with syntax and examples."
---

Subtracts a specified number of minutes from a datetime.

## Analyze Syntax

```python
func.minutes_sub(<datetime>, <n>)
```

## Analyze Examples

```python
func.minutes_sub('2024-01-01 10:45:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
MINUTES_SUB(<datetime>, <n>)
```

## SQL Examples

```sql
SELECT MINUTES_SUB('2024-01-01 10:45:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
