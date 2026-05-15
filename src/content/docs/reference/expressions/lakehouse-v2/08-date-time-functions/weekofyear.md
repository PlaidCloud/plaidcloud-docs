---
title: WEEKOFYEAR (Lakehouse v2)
description: WEEKOFYEAR — returns the week of the year for a date. Alias for `WEEK`.
---

Returns the week of the year for a date. Alias for `WEEK`.

## Analyze Syntax

```python
func.weekofyear(<date>)
```

## Analyze Examples

```python
func.weekofyear('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## SQL Syntax

```sql
WEEKOFYEAR(<date>)
```

## SQL Examples

```sql
SELECT WEEKOFYEAR('2024-06-15');

┌────┐
│ 24  │
└────┘
```
