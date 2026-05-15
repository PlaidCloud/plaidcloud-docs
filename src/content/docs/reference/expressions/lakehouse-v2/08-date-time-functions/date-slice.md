---
title: DATE_SLICE (Lakehouse v2)
description: "Use the DATE_SLICE date/time function in PlaidCloud Lakehouse. Converts a given time to the beginning or end of a time interval based on the specified period."
---

Converts a given time to the beginning or end of a time interval based on the specified period.

## Analyze Syntax

```python
func.date_slice(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## Analyze Examples

```python
func.date_slice('2024-06-15 14:35:00', text('INTERVAL 1 HOUR'))

┌───────────────────────┐
│ '2024-06-15 14:00:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
DATE_SLICE(<datetime>, INTERVAL <n> <unit>[, <boundary>])
```

## SQL Examples

```sql
SELECT DATE_SLICE('2024-06-15 14:35:00', INTERVAL 1 HOUR);

┌─────────────────────┐
│ 2024-06-15 14:00:00  │
└─────────────────────┘
```
