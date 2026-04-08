---
title: SECONDS_SUB
description: "Learn how to use the SECONDS_SUB date/time function in PlaidCloud Lakehouse. Subtracts a specified number of seconds from a datetime - with syntax and examples."
---

Subtracts a specified number of seconds from a datetime.

## Analyze Syntax

```python
func.seconds_sub(<datetime>, <n>)
```

## Analyze Examples

```python
func.seconds_sub('2024-01-01 00:01:30', 90)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
SECONDS_SUB(<datetime>, <n>)
```

## SQL Examples

```sql
SELECT SECONDS_SUB('2024-01-01 00:01:30', 90);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
