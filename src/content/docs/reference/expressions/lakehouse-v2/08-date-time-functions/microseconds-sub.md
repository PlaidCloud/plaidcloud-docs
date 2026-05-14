---
title: MICROSECONDS_SUB
description: "Learn how to use the MICROSECONDS_SUB date/time function in PlaidCloud Lakehouse. Subtracts a specified number of microseconds from a datetime."
---

Subtracts a specified number of microseconds from a datetime.

## Analyze Syntax

```python
func.microseconds_sub(<datetime>, <n>)
```

## Analyze Examples

```python
func.microseconds_sub('2024-01-01 00:00:01', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
MICROSECONDS_SUB(<datetime>, <n>)
```

## SQL Examples

```sql
SELECT MICROSECONDS_SUB('2024-01-01 00:00:01', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:00  │
└─────────────────────┘
```
