---
title: HOURS_ADD
description: "Learn how to use the HOURS_ADD date/time function in PlaidCloud Lakehouse. Adds a specified number of hours to a datetime - with syntax and examples."
---

Adds a specified number of hours to a datetime.

## Analyze Syntax

```python
func.hours_add(<datetime>, <n>)
```

## Analyze Examples

```python
func.hours_add('2024-01-01 10:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 15:00:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
HOURS_ADD(<datetime>, <n>)
```

## SQL Examples

```sql
SELECT HOURS_ADD('2024-01-01 10:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 15:00:00  │
└─────────────────────┘
```
