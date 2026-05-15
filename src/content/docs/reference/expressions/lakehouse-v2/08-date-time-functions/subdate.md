---
title: SUBDATE
description: SUBDATE — subtracts a time interval from a date. Alias for `DATE_SUB`.
---

Subtracts a time interval from a date. Alias for `DATE_SUB`.

## Analyze Syntax

```python
func.subdate(<date>, INTERVAL <n> <unit>)
```

## Analyze Examples

```python
func.subdate('2024-01-31', text('INTERVAL 7 DAY'))

┌──────────────┐
│ '2024-01-24'  │
└──────────────┘
```

## SQL Syntax

```sql
SUBDATE(<date>, INTERVAL <n> <unit>)
```

## SQL Examples

```sql
SELECT SUBDATE('2024-01-31', INTERVAL 7 DAY);

┌────────────┐
│ 2024-01-24  │
└────────────┘
```
