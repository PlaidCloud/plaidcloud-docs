---
title: STR2DATE
description: STR2DATE — parses a string into a date using a format string. Alias for `STR_TO_DATE`.
---

Parses a string into a date using a format string. Alias for `STR_TO_DATE`.

## Analyze Syntax

```python
func.str2date(<str>, <format>)
```

## Analyze Examples

```python
func.str2date('2024/06/15', '%Y/%m/%d')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQL Syntax

```sql
STR2DATE(<str>, <format>)
```

## SQL Examples

```sql
SELECT STR2DATE('2024/06/15', '%Y/%m/%d');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
