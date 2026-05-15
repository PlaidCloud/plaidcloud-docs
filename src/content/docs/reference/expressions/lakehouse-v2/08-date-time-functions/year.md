---
title: YEAR (Lakehouse v2)
description: YEAR — returns the year from a date.
---

Returns the year from a date.

## Analyze Syntax

```python
func.year(<date>)
```

## Analyze Examples

```python
func.year('2024-06-15')

┌──────┐
│ 2024  │
└──────┘
```

## SQL Syntax

```sql
YEAR(<date>)
```

## SQL Examples

```sql
SELECT YEAR('2024-06-15');

┌──────┐
│ 2024  │
└──────┘
```
