---
title: STR_TO_DATE (Lakehouse v2)
description: STR_TO_DATE — parses a string into a date using a format string.
---

Parses a string into a date using a format string.

## Analyze Syntax

```python
func.str_to_date(<str>, <format>)
```

## Analyze Examples

```python
func.str_to_date('Jun 15 2024', '%b %d %Y')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL Syntax

```sql
STR_TO_DATE(<str>, <format>)
```

## SQL Examples

```sql
SELECT STR_TO_DATE('Jun 15 2024', '%b %d %Y');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
