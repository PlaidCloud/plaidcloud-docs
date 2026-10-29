---
title: DATE_ADD（Lakehouse v1）
description: DATE_ADD——为指定的日期或带时间的日期增加时间间隔或日期间隔。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/date-add.md
---

为指定的日期或带时间的日期（timestamp/datetime）增加时间间隔或日期间隔。

## Analyze 语法

```python
func.date_add(<unit>, <value>,  <date_or_time_expr>)
```

## Analyze 示例

```python
func.date_add('YEAR', 1, func.to_date('2018-01-02'))
┌──────────────────────────────────────────────────────┐
│ func.date_add('YEAR', 1, func.to_date('2018-01-02')) │
├──────────────────────────────────────────────────────┤
│ 2019-01-02                                           │
└──────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
DATE_ADD(<unit>, <value>,  <date_or_time_expr>)
```
## 参数

| 参数                  | 说明                                                                                                              |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| `<unit>`              | 必须是以下值之一：`YEAR`、`QUARTER`、`MONTH`、`DAY`、`HOUR`、`MINUTE` 和 `SECOND`                                 |
| `<value>`             | 要增加的时间单位数量。例如，要增加 2 天，此值为 2。                                                               |
| `<date_or_time_expr>` | `DATE` 或 `TIMESTAMP` 类型的值                                                                                    |

## 返回类型

函数返回与 `<date_or_time_expr>` 参数相同类型的值。

## SQL 示例

```sql
SELECT date_add(YEAR, 1, to_date('2018-01-02'));
┌───────────────────────────────────────────────────┐
│ DATE_ADD(YEAR, INTERVAL 1, to_date('2018-01-02')) │
├───────────────────────────────────────────────────┤
│ 2019-01-02                                        │
└───────────────────────────────────────────────────┘
```
