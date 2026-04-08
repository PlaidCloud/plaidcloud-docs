---
title: DAYOFMONTH
description: "Learn how to use the DAYOFMONTH date/time function in PlaidCloud Lakehouse. Returns the day of the month from a date. Alias for `DAY`."
---

Returns the day of the month from a date. Alias for `DAY`.

## Analyze Syntax

```python
func.dayofmonth(<date>)
```

## Analyze Examples

```python
func.dayofmonth('2024-06-15')

┌────┐
│ 15  │
└────┘
```

## SQL Syntax

```sql
DAYOFMONTH(<date>)
```

## SQL Examples

```sql
SELECT DAYOFMONTH('2024-06-15');

┌────┐
│ 15  │
└────┘
```
