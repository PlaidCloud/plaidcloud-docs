---
title: TO_MONTH（Lakehouse v1）
description: TO_MONTH——将日期或带时间的日期（timestamp/datetime）转换为包含月份编号的 UInt8 数字。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-month.md
---

将日期或带时间的日期（timestamp/datetime）转换为包含月份编号（1-12）的 UInt8 数字。

## Analyze 语法

```python
func.to_month(<expr>)
```

## Analyze 示例

```python
func.now(), func.to_month(func.now()), func.month(func.now())

┌─────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_month(func.now()) │ func.month(func.now()) │
├────────────────────────────┼───────────────────────────┼────────────────────────┤
│ 2024-03-14 23:34:02.161291 │                         3 │                      3 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_MONTH(<expr>)
```

## 参数

| 参数      | 说明           |
|-----------|----------------|
| `<expr>`  | 日期/时间戳    |

## 别名

- [MONTH](../month)

## 返回类型

 `TINYINT`

## SQL 示例

```sql
SELECT NOW(), TO_MONTH(NOW()), MONTH(NOW());

┌─────────────────────────────────────────────────────────────┐
│            now()           │ to_month(now()) │ month(now()) │
├────────────────────────────┼─────────────────┼──────────────┤
│ 2024-03-14 23:34:02.161291 │               3 │            3 │
└─────────────────────────────────────────────────────────────┘
```
