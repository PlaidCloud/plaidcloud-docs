---
title: TO_DATETIME_NTZ (Lakehouse v2)
description: TO_DATETIME_NTZ — converts a value to a DATETIME without time zone (NTZ).
---

Converts a value to a DATETIME without time zone (NTZ). The result is not affected by session time zone settings.

## Analyze Syntax

```python
func.to_datetime_ntz('2024-06-15 14:30:00')
```

## Analyze Examples

```python
func.to_datetime_ntz('2024-06-15 14:30:00')

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```

## SQL Syntax

```sql
TO_DATETIME_NTZ(<expr>)
```

## SQL Examples

```sql
SELECT TO_DATETIME_NTZ('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```
