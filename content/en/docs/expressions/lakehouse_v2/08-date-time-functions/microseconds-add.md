---
title: MICROSECONDS_ADD
---

Adds a specified number of microseconds to a datetime.

## Analyze Syntax

```python
func.microseconds_add(<datetime>, <n>)
```

## Analyze Examples

```python
func.microseconds_add('2024-01-01 00:00:00', 1000000)

┌───────────────────────┐
│ '2024-01-01 00:00:01'  │
└───────────────────────┘
```

## SQL Syntax

```sql
MICROSECONDS_ADD(<datetime>, <n>)
```

## SQL Examples

```sql
SELECT MICROSECONDS_ADD('2024-01-01 00:00:00', 1000000);

┌─────────────────────┐
│ 2024-01-01 00:00:01  │
└─────────────────────┘
```
