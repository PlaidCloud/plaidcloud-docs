---
title: TO_HOURS（Lakehouse v1）
description: TO_HOURS——将指定数量的小时转换为 Interval 类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-hours.md
---

将指定数量的小时转换为 Interval 类型。

- 接受正整数、零和负整数作为输入。

## Analyze 语法

```python
func.to_hours(<hours>)
```

## Analyze 示例

```python
func.to_hours(2)
┌──────────────────────────────────────────────────────┐
│ func.to_hours(2)                                     │
├──────────────────────────────────────────────────────┤
│ 2:00:00                                              │
└──────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_HOURS(<hours>)
```

## 返回类型

Interval（格式为 `hh:mm:ss`）。

## SQL 示例

```sql
SELECT TO_HOURS(2), TO_HOURS(0), TO_HOURS((- 2));

┌───────────────────────────────────────────┐
│ to_hours(2) │ to_hours(0) │ to_hours(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 2:00:00     │ 00:00:00    │ -2:00:00      │
└───────────────────────────────────────────┘
```
