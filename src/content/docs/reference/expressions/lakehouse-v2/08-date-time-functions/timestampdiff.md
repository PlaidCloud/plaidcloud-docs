---
title: TIMESTAMPDIFF (Lakehouse v2)
description: TIMESTAMPDIFF — returns the difference between two datetimes in the specified unit.
---

Returns the difference between two datetimes in the specified unit.

## Analyze Syntax

```python
func.timestampdiff(<unit>, <start>, <end>)
```

## Analyze Examples

```python
func.timestampdiff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## SQL Syntax

```sql
TIMESTAMPDIFF(<unit>, <start>, <end>)
```

## SQL Examples

```sql
SELECT TIMESTAMPDIFF(DAY, '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```
