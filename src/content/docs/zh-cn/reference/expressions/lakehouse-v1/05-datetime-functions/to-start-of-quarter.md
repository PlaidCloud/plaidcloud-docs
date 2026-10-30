---
title: TO_START_OF_QUARTER（Lakehouse v1）
description: TO_START_OF_QUARTER——将日期或带时间的日期（timestamp/datetime）向下取整到季度的第一天。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-quarter.md
---

将日期或带时间的日期（timestamp/datetime）向下取整到所在季度的第一天。
季度的第一天为 1 月 1 日、4 月 1 日、7 月 1 日或 10 月 1 日。
返回日期。

## Analyze 语法

```python
func.to_start_of_quarter(<expr>)
```

## Analyze 示例

```python
func.to_start_of_quarter('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_quarter('2023-11-12 09:38:18.165575')         │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-10-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_START_OF_QUARTER(<expr>)
```

## 参数

| 参数 | 说明    |
|-----------|----------------|
| `<expr>`   | date/timestamp |

## 返回类型

`DATE`，返回“YYYY-MM-DD”格式的日期。

## SQL 示例

```sql
SELECT
  to_start_of_quarter('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────┐
│ to_start_of_quarter('2023-11-12 09:38:18.165575') │
│                        Date                       │
├───────────────────────────────────────────────────┤
│ 2023-10-01                                        │
└───────────────────────────────────────────────────┘
```
