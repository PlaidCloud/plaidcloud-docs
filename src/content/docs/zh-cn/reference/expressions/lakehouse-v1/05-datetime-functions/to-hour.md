---
title: TO_HOUR（Lakehouse v1）
description: TO_HOUR——将带时间的日期（timestamp/datetime）转换为 UInt8 数字，表示 24 小时制的小时数（0-23）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-hour.md
---

将带时间的日期（timestamp/datetime）转换为 UInt8 数字，表示 24 小时制的小时数（0-23）。
该函数假定：如果时钟向前拨，则拨快一小时且发生在凌晨 2 点；如果时钟向后拨，则拨慢一小时且发生在凌晨 3 点（这并不总是成立，即使在莫斯科，时钟也曾两次在不同时间调整）。


## Analyze 语法

```python
func.to_hour(<expr>)
```

## Analyze 示例

```python
func.to_hour('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_hour('2023-11-12 09:38:18.165575')         │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                  9 │
└────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_HOUR(<expr>)
```

## 参数

| 参数      | 说明        |
|-----------|-------------|
| `<expr>`  | 时间戳      |

## 返回类型

`TINYINT`

## SQL 示例

```sql
SELECT
    to_hour('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────┐
│ to_hour('2023-11-12 09:38:18.165575') │
│                 UInt8                 │
├───────────────────────────────────────┤
│                                     9 │
└───────────────────────────────────────┘
```
