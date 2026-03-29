---
title: TIME_SLICE
---

Converts a given time to the beginning or end of a time interval.

## Analyze Syntax

```python
func.time_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Analyze Examples

```python
func.time_slice('2024-06-15 14:35:00', text('INTERVAL 15 MINUTE'))

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
TIME_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## SQL Examples

```sql
SELECT TIME_SLICE('2024-06-15 14:35:00', INTERVAL 15 MINUTE);

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
