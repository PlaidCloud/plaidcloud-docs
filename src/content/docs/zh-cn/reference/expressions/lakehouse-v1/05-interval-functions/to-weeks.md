---
title: TO_WEEKS（Lakehouse v1）
description: TO_WEEKS——将指定数量的周转换为 Interval 类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-weeks.md
---

将指定数量的周转换为 Interval 类型。

- 接受正整数、零和负整数作为输入。

## Analyze 语法

```python
func.to_weeks(<weeks>)
```

## Analyze 示例

```python
func.to_weeks(2)
┌──────────────────────────────────────────────────────┐
│ func.to_weeks(2)                                     │
├──────────────────────────────────────────────────────┤
│ 14 days                                              │
└──────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_WEEKS(<weeks>)
```

## 返回类型

Interval（以天表示）。

## SQL 示例

```sql
SELECT TO_WEEKS(2), TO_WEEKS(0), TO_WEEKS((- 2));

┌───────────────────────────────────────────┐
│ to_weeks(2) │ to_weeks(0) │ to_weeks(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 14 days     │ 00:00:00    │ -14 days      │
└───────────────────────────────────────────┘
```
