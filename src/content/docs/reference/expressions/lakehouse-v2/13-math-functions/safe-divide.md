---
title: SAFE_DIVIDE (Lakehouse v2)
description: SAFE_DIVIDE — a PlaidCloud function that divides two numbers and returns a value of your choice instead of failing when the denominator is zero.
---

A PlaidCloud function, available on every lakehouse engine. Divides the first number by the second. When the denominator is zero, or either side is NULL, the result is NULL unless a third value is given, in which case that value is returned instead. Both sides are cast to `DECIMAL(38, 10)` first, so integer columns divide without truncation.

## Analyze Syntax

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)

func.safe_divide(<numerator>, <denominator>)
```

## Analyze Examples

```python
func.safe_divide(table.revenue, table.units, 0)

| revenue | units | safe_divide |
|---------|-------|-------------|
| 100     | 8     | 12.5        |
| 100     | 0     | 0           |
| 100     | NULL  | 0           |
```

```python
func.safe_divide(table.revenue, table.units, None)

| revenue | units | safe_divide |
|---------|-------|-------------|
| 100     | 8     | 12.5        |
| 100     | 0     | NULL        |
```

## SQL Equivalent

There is no SQL function of this name. The expression compiles to:

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```

Without the third argument there is no COALESCE, and a zero denominator gives NULL:

```sql
CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0)
```
