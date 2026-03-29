---
title: RETENTION
---

Calculates retention for a set of events. Returns an array of 0s and 1s.

## Analyze Syntax

```python
func.retention(cond1, cond2)
```

## Analyze Examples

```python
func.retention(get_column(table, 'day1'), get_column(table, 'day2'))
```

## SQL Syntax

```sql
RETENTION(cond1, cond2)
```

## SQL Examples

```sql
SELECT uid, RETENTION(dt='2024-01-01', dt='2024-01-02', dt='2024-01-03')
FROM events GROUP BY uid;

┌─────┬────────────┐
│ uid │ retention  │
├─────┼────────────┤
│   1 │ [1,1,0]    │
│   2 │ [1,0,0]    │
│   3 │ [1,1,1]    │
└─────┴────────────┘
```
