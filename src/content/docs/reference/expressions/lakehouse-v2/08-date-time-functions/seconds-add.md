---
title: SECONDS_ADD
description: SECONDS_ADD — adds a specified number of seconds to a datetime.
---

Adds a specified number of seconds to a datetime.

## Analyze Syntax

```python
func.seconds_add(<datetime>, <n>)
```

## Analyze Examples

```python
func.seconds_add('2024-01-01 00:00:00', 90)

┌───────────────────────┐
│ '2024-01-01 00:01:30'  │
└───────────────────────┘
```

## SQL Syntax

```sql
SECONDS_ADD(<datetime>, <n>)
```

## SQL Examples

```sql
SELECT SECONDS_ADD('2024-01-01 00:00:00', 90);

┌─────────────────────┐
│ 2024-01-01 00:01:30  │
└─────────────────────┘
```
