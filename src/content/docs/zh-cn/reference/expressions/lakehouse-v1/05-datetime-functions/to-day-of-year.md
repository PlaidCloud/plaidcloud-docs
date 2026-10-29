---
title: TO_DAY_OF_YEAR（Lakehouse v1）
description: TO_DAY_OF_YEAR——将日期或带时间的日期（timestamp/datetime）转换为 UInt16 数字。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-year.md
---

将日期或带时间的日期（timestamp/datetime）转换为 UInt16 数字，表示一年中的第几天（1-366）。

## Analyze 语法

```python
func.to_day_of_year(<expr>)
```

## Analyze 示例

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_year('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                316 │
└────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_DAY_OF_YEAR(<expr>)
```

## 参数

| 参数        | 说明        |
| ----------- | ----------- |
| `<expr>` | 日期/时间戳 |

## 返回类型

`SMALLINT`

## SQL 示例

```sql
SELECT
    to_day_of_year('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ to_day_of_year('2023-11-12 09:38:18.165575') │
│                    UInt16                    │
├──────────────────────────────────────────────┤
│                                          316 │
└──────────────────────────────────────────────┘
```
