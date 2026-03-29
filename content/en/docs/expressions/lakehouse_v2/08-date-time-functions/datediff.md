---
title: DATEDIFF
---

Returns the number of days between two dates.

## Analyze Syntax

```python
func.datediff(<end_date>, <start_date>)
```

## Analyze Examples

```python
func.datediff('2024-03-01', '2024-01-01')

┌────┐
│ 60  │
└────┘
```

## SQL Syntax

```sql
DATEDIFF(<end_date>, <start_date>)
```

## SQL Examples

```sql
SELECT DATEDIFF('2024-03-01', '2024-01-01');

┌────┐
│ 60  │
└────┘
```
