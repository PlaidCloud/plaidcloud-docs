---
title: DATE_TRUNC（Lakehouse v1）
description: DATE_TRUNC——将日期、时间或时间戳值截断到指定精度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-trunc.md
---

将日期、时间或时间戳值截断到指定精度。例如，将 `2022-07-07` 截断到 `MONTH`，结果为 `2022-07-01`；将 `2022-07-07 01:01:01.123456` 截断到 `SECOND`，结果为 `2022-07-07 01:01:01.000000`。

## Analyze 语法

```python
func.date_sub(<precision>,  <date_or_time_expr>)
```

## Analyze 示例

```python
func.date_trunc('month', func.to_date('2022-07-07'))
┌──────────────────────────────────────────────────────┐
│ func.date_trunc('month', func.to_date('2022-07-07')) │
├──────────────────────────────────────────────────────┤
│ 2022-07-01                                           │
└──────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
DATE_TRUNC(<precision>, <date_or_time_expr>)
```
## 参数

| 参数                  | 说明                                                                                               |
|-----------------------|----------------------------------------------------------------------------------------------------|
| `<precision>`          | 必须是以下值之一：`YEAR`、`QUARTER`、`MONTH`、`DAY`、`HOUR`、`MINUTE` 和 `SECOND`                 |
| `<date_or_time_expr>` | `DATE` 或 `TIMESTAMP` 类型的值                                                                     |

## 返回类型

函数返回与 `<date_or_time_expr>` 参数相同类型的值。

## SQL 示例

```sql
select date_trunc(month, to_date('2022-07-07'));
┌──────────────────────────────────────────┐
│ date_trunc(month, to_date('2022-07-07')) │
├──────────────────────────────────────────┤
│ 2022-07-01                               │
└──────────────────────────────────────────┘
```
