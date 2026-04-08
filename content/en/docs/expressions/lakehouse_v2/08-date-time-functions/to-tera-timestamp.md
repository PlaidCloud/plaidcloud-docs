---
title: TO_TERA_TIMESTAMP
description: "Use the TO_TERA_TIMESTAMP date/time function in PlaidCloud Lakehouse. Converts a VARCHAR value to a DATETIME value according to a Teradata format string."
---

Converts a VARCHAR value to a DATETIME value according to a Teradata format string.

## Analyze Syntax

```python
func.to_tera_timestamp(<str>, <format>)
```

## Analyze Examples

```python
func.to_tera_timestamp('20240615143000', 'YYYYMMDDHH24MISS')

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## SQL Syntax

```sql
TO_TERA_TIMESTAMP(<str>, <format>)
```

## SQL Examples

```sql
SELECT TO_TERA_TIMESTAMP('20240615143000', 'YYYYMMDDHH24MISS');

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
