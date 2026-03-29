---
title: DATE_FORMAT
---

Formats a date or datetime value according to a format string.

## Analyze Syntax

```python
func.date_format(<date>, <format>)
```

## Analyze Examples

```python
func.date_format('2024-06-15', '%Y/%m/%d')

┌──────────────┐
│ '2024/06/15'  │
└──────────────┘
```

## SQL Syntax

```sql
DATE_FORMAT(<date>, <format>)
```

## SQL Examples

```sql
SELECT DATE_FORMAT('2024-06-15', '%Y/%m/%d');

┌────────────┐
│ 2024/06/15  │
└────────────┘
```
