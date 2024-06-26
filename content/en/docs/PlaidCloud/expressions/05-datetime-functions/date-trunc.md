---
title: DATE_TRUNC
---

Truncates a date, time, or timestamp value to a specified precision. For example, if you truncate `2022-07-07` to `MONTH`, the result will be `2022-07-01`; if you truncate `2022-07-07 01:01:01.123456` to `SECOND`, the result will be `2022-07-07 01:01:01.000000`.

## Analyze Syntax

```python
func.date_sub(<precision>,  <date_or_time_expr>)
```

## Analyze Examples

```python
func.date_trunc('month', func.to_date('2022-07-07'))
+------------------------------------------------------+
| func.date_trunc('month', func.to_date('2022-07-07')) |
+------------------------------------------------------+
| 2022-07-01                                           |
+------------------------------------------------------+
```

## SQL Syntax

```sql
DATE_TRUNC(<precision>, <date_or_time_expr>)
```
## Arguments

| Arguments             | Description                                                                                        |
|-----------------------|----------------------------------------------------------------------------------------------------|
| `<precision>`          | Must be of the following values: `YEAR`, `QUARTER`, `MONTH`, `DAY`, `HOUR`, `MINUTE` and `SECOND`  |
| `<date_or_time_expr>` | A value of `DATE` or `TIMESTAMP` type                                                              |

## Return Type

The function returns a value of the same type as the `<date_or_time_expr>` argument.

## SQL Examples

```sql
select date_trunc(month, to_date('2022-07-07'));
+------------------------------------------+
| date_trunc(month, to_date('2022-07-07')) |
+------------------------------------------+
| 2022-07-01                               |
+------------------------------------------+
```
