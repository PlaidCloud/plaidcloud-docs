---
title: "PERCENTILE_DISC (Aggregate, Lakehouse v2)"
description: "在 PlaidCloud Lakehouse 中使用 PERCENTILE_DISC 聚合函数。返回累积分布大于或等于指定百分位数的最小值。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc.md
---

返回累积分布大于或等于指定百分位数的最小值。

## Analyze 语法

```python
func.percentile_disc(0.5)
```

## Analyze 示例

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## SQL 语法

```sql
PERCENTILE_DISC(0.5)
```

## SQL 示例

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
