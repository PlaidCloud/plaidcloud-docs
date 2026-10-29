---
title: TO_DAY_OF_MONTH（Lakehouse v1）
description: TO_DAY_OF_MONTH——将日期或带时间的日期（timestamp/datetime）转换为 UInt8 数字。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-month.md
---

将日期或带时间的日期（timestamp/datetime）转换为 UInt8 数字，表示当月的第几天（1-31）。

## Analyze 语法

```python
func.to_day_of_month(<expr>)
```

## Analyze 示例

```python
func.now(), func.to_day_of_month(func.now()), func.day(func.now())

┌──────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_day_of_month(func.now()) │ func.day(func.now()) │
├────────────────────────────┼──────────────────────────────────┼──────────────────────┤
│ 2024-03-14 23:35:41.947962 │                               14 │                   14 │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_DAY_OF_MONTH(<expr>)
```

## 参数

| 参数      | 说明           |
|-----------|----------------|
| `<expr>`  | 日期/时间戳    |

## 别名

- [DAY](../day)

## 返回类型

`TINYINT`

## SQL 示例

```sql
SELECT NOW(), TO_DAY_OF_MONTH(NOW()), DAY(NOW());

┌──────────────────────────────────────────────────────────────────┐
│            now()           │ to_day_of_month(now()) │ day(now()) │
├────────────────────────────┼────────────────────────┼────────────┤
│ 2024-03-14 23:35:41.947962 │                     14 │         14 │
└──────────────────────────────────────────────────────────────────┘
```
