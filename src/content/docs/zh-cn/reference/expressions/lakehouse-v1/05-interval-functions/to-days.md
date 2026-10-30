---
title: TO_DAYS（Lakehouse v1）
description: TO_DAYS——将指定数量的天转换为 Interval 类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-days.md
---

将指定数量的天转换为 Interval 类型。

- 接受正整数、零和负整数作为输入。

## Analyze 语法

```python
func.to_days(<days>)
```

## Analyze 示例

```python
func.to_days(2)
┌──────────────────────────────────────────────────────┐
│ func.to_days(2)                                      │
├──────────────────────────────────────────────────────┤
│ 200 days                                             │
└──────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
TO_DAYS(<days>)
```

## 返回类型

Interval（以天表示）。

## SQL 示例

```sql
SELECT TO_DAYS(2), TO_DAYS(0), TO_DAYS(-2);

┌────────────────────────────────────────┐
│ to_days(2) │ to_days(0) │ to_days(- 2) │
├────────────┼────────────┼──────────────┤
│ 2 days     │ 00:00:00   │ -2 days      │
└────────────────────────────────────────┘
```
