---
title: MINUTES_ADD (Lakehouse v2)
description: MINUTES_ADD — adds a specified number of minutes to a datetime.
---

Adds a specified number of minutes to a datetime.

## Analyze Syntax

```python
func.minutes_add(<datetime>, <n>)
```

## Analyze Examples

```python
func.minutes_add('2024-01-01 10:00:00', 45)

┌───────────────────────┐
│ '2024-01-01 10:45:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
MINUTES_ADD(<datetime>, <n>)
```

## SQL Examples

```sql
SELECT MINUTES_ADD('2024-01-01 10:00:00', 45);

┌─────────────────────┐
│ 2024-01-01 10:45:00  │
└─────────────────────┘
```
