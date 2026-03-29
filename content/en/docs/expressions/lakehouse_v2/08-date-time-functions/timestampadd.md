---
title: TIMESTAMPADD
---

Adds a specified time interval to a datetime.

## Analyze Syntax

```python
func.timestampadd(<unit>, <n>, <datetime>)
```

## Analyze Examples

```python
func.timestampadd('DAY', 7, '2024-01-01')

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## SQL Syntax

```sql
TIMESTAMPADD(<unit>, <n>, <datetime>)
```

## SQL Examples

```sql
SELECT TIMESTAMPADD(DAY, 7, '2024-01-01');

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
