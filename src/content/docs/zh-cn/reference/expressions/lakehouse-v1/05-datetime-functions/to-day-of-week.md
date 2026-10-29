---
title: TO_DAY_OF_WEEK（Lakehouse v1）
description: TO_DAY_OF_WEEK——将日期或带时间的日期（timestamp/datetime）转换为 UInt8 数字。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-week.md
---

将日期或带时间的日期（timestamp/datetime）转换为 UInt8 数字，表示星期几（星期一为 1，星期日为 7）。

## Analyze 语法

```python
func.to_day_of_week(<expr>)
```

## Analyze 示例

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_week('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                  7 │
└────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_DAY_OF_WEEK(<expr>)
```

## 参数

| 参数      | 说明           |
|-----------|----------------|
| `<expr>`  | 日期/时间戳    |

## 返回类型

``TINYINT`

## SQL 示例

```sql

SELECT
    to_day_of_week('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ to_day_of_week('2023-11-12 09:38:18.165575') │
│                     UInt8                    │
├──────────────────────────────────────────────┤
│                                            7 │
└──────────────────────────────────────────────┘
```
