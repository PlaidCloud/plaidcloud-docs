---
title: TO_MONDAY（Lakehouse v1）
description: TO_MONDAY——将日期或带时间的日期（timestamp/datetime）向下取整到最近的星期一。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-monday.md
---

将日期或带时间的日期（timestamp/datetime）向下取整到最近的星期一。
返回日期。

## Analyze 语法

```python
func.to_monday(<expr>)
```

## Analyze 示例

```python
func.to_monday('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_monday('2023-11-12 09:38:18.165575')       │
│                      Date                          │
├────────────────────────────────────────────────────┤
│ 2023-11-06                                         │
└────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_MONDAY(<expr>)
```

## 参数

| 参数        | 说明        |
| ----------- | ----------- |
| `<expr>` | 日期/时间戳 |

## 返回类型

`DATE`，以“YYYY-MM-DD”格式返回日期。

## SQL 示例

```sql
SELECT
    to_monday('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_monday('2023-11-12 09:38:18.165575') │
│                   Date                  │
├─────────────────────────────────────────┤
│ 2023-11-06                              │
└─────────────────────────────────────────┘
```
