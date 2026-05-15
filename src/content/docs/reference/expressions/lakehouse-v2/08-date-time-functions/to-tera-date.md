---
title: TO_TERA_DATE (Lakehouse v2)
description: TO_TERA_DATE — converts a VARCHAR value to a DATE value according to a Teradata format string.
---

Converts a VARCHAR value to a DATE value according to a Teradata format string.

## Analyze Syntax

```python
func.to_tera_date(<str>, <format>)
```

## Analyze Examples

```python
func.to_tera_date('20240615', 'YYYYMMDD')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL Syntax

```sql
TO_TERA_DATE(<str>, <format>)
```

## SQL Examples

```sql
SELECT TO_TERA_DATE('20240615', 'YYYYMMDD');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
