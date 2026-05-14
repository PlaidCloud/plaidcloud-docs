---
title: YEAR
description: "Learn how to use the YEAR date/time function in PlaidCloud Lakehouse. Returns the year from a date - see syntax, examples, and output."
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
