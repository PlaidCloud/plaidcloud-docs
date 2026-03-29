---
title: DAYOFWEEK_ISO
---

Returns the ISO day of the week index for a date (1=Monday, 7=Sunday).

## Analyze Syntax

```python
func.dayofweek_iso(<date>)
```

## Analyze Examples

```python
func.dayofweek_iso('2024-06-15')

┌───┐
│ 6  │
└───┘
```

## SQL Syntax

```sql
DAYOFWEEK_ISO(<date>)
```

## SQL Examples

```sql
SELECT DAYOFWEEK_ISO('2024-06-15');

┌───┐
│ 6  │
└───┘
```
