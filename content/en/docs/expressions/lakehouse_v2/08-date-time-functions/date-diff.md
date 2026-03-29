---
title: DATE_DIFF
---

Returns the difference between two dates in the specified unit.

## Analyze Syntax

```python
func.date_diff(<unit>, <start>, <end>)
```

## Analyze Examples

```python
func.date_diff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## SQL Syntax

```sql
DATE_DIFF(<unit>, <start>, <end>)
```

## SQL Examples

```sql
SELECT DATE_DIFF('DAY', '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```
