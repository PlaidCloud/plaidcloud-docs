---
title: LAST_DAY
---

Returns the last day of the month for a given date.

## Analyze Syntax

```python
func.last_day(<date>[, <unit>])
```

## Analyze Examples

```python
func.last_day('2024-02-15')

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## SQL Syntax

```sql
LAST_DAY(<date>[, <unit>])
```

## SQL Examples

```sql
SELECT LAST_DAY('2024-02-15');

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
