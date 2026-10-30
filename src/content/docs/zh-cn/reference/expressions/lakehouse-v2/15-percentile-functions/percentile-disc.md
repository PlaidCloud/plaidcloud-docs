---
title: "PERCENTILE_DISC (Percentile, Lakehouse v2)"
description: "在 PlaidCloud Lakehouse 中使用 PERCENTILE_DISC 百分位函数。返回累积分布大于或等于指定百分位的最小值。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-disc.md
---

返回累积分布大于或等于指定百分位的最小值。

## Analyze 语法

```python
func.percentile_disc(<percentile>)
```

## Analyze 示例

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000  │
└───────┘
```

## SQL 语法

```sql
PERCENTILE_DISC(<percentile>)
```

## SQL 示例

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000  │
└───────┘
```
