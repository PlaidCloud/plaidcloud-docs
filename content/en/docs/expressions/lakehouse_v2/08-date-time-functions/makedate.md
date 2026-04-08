---
title: MAKEDATE
description: "Learn how to use the MAKEDATE date/time function in PlaidCloud Lakehouse. Creates a date from a year and day-of-year value - with syntax and examples."
---

Creates a date from a year and day-of-year value.

## Analyze Syntax

```python
func.makedate(<year>, <dayofyear>)
```

## Analyze Examples

```python
func.makedate(2024, 100)

┌──────────────┐
│ '2024-04-09'  │
└──────────────┘
```

## SQL Syntax

```sql
MAKEDATE(<year>, <dayofyear>)
```

## SQL Examples

```sql
SELECT MAKEDATE(2024, 100);

┌────────────┐
│ 2024-04-09  │
└────────────┘
```
