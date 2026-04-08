---
title: MONTHNAME
description: "Learn how to use the MONTHNAME date/time function in PlaidCloud Lakehouse. Returns the name of the month for a date - see syntax, examples, and output."
---

Returns the name of the month for a date.

## Analyze Syntax

```python
func.monthname(<date>)
```

## Analyze Examples

```python
func.monthname('2024-06-15')

┌────────┐
│ 'June'  │
└────────┘
```

## SQL Syntax

```sql
MONTHNAME(<date>)
```

## SQL Examples

```sql
SELECT MONTHNAME('2024-06-15');

┌──────┐
│ June  │
└──────┘
```
