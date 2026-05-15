---
title: SECONDS_SUB
description: SECONDS_SUB — subtracts a specified number of seconds from a datetime.
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
