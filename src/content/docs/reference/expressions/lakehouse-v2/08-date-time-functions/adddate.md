---
title: ADDDATE (Lakehouse v2)
description: ADDDATE — adds a specified time interval to a date. Alias for `DATE_ADD`.
---

Adds a specified time interval to a date. Alias for `DATE_ADD`.

## Analyze Syntax

```python
func.adddate(<date>, INTERVAL <n> <unit>)
```

## Analyze Examples

```python
func.adddate('2024-01-01', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-08'  │
└──────────────┘
```

## SQL Syntax

```sql
ADDDATE(<date>, INTERVAL <n> <unit>)
```

## SQL Examples

```sql
SELECT ADDDATE('2024-01-01', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-08  │
└────────────┘
```
