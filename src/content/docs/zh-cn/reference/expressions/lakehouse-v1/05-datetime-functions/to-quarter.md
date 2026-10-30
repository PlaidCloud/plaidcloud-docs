---
title: TO_QUARTER（Lakehouse v1）
description: TO_QUARTER——从给定的日期或时间戳中检索季度（1、2、3 或 4）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-quarter.md
---

从给定的日期或时间戳中检索季度（1、2、3 或 4）。

## Analyze 语法

```python
func.to_quarter(<expr>)
```

## Analyze 示例

```python
func.now(), func.to_quarter(func.now()), func.quarter(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_quarter(func.now()) │ func.quarter(func.now()) │
├────────────────────────────┼─────────────────────────────┼──────────────────────────┤
│ 2024-03-14 23:32:52.743133 │                           3 │                        3 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_QUARTER( <date_or_time_expr> )
```

## 别名

- [QUARTER](../quarter)

## 返回类型

整数。

## SQL 示例

```sql
SELECT NOW(), TO_QUARTER(NOW()), QUARTER(NOW());

┌─────────────────────────────────────────────────────────────────┐
│            now()           │ to_quarter(now()) │ quarter(now()) │
├────────────────────────────┼───────────────────┼────────────────┤
│ 2024-03-14 23:32:52.743133 │                 1 │              1 │
└─────────────────────────────────────────────────────────────────┘
```
