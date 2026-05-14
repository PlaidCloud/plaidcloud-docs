---
title: STR_TO_DATE
description: "Learn how to use the STR_TO_DATE date/time function in PlaidCloud Lakehouse. Parses a string into a date using a format string - with syntax and examples."
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
