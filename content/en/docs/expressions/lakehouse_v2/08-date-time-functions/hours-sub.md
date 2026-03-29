---
title: HOURS_SUB
---

Subtracts a specified number of hours from a datetime.

## Analyze Syntax

```python
func.hours_sub(<datetime>, <n>)
```

## Analyze Examples

```python
func.hours_sub('2024-01-01 15:00:00', 5)

┌───────────────────────┐
│ '2024-01-01 10:00:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
HOURS_SUB(<datetime>, <n>)
```

## SQL Examples

```sql
SELECT HOURS_SUB('2024-01-01 15:00:00', 5);

┌─────────────────────┐
│ 2024-01-01 10:00:00  │
└─────────────────────┘
```
