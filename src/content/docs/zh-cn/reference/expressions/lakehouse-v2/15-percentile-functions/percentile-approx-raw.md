---
title: PERCENTILE_APPROX_RAW (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 PERCENTILE_APPROX_RAW 百分位函数。从预先计算的百分位状态返回近似的百分位值。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-approx-raw.md
---

从预先计算的百分位状态返回近似的百分位值。

## Analyze 语法

```python
func.percentile_approx_raw(<state>, <percentile>)
```

## Analyze 示例

```python
func.percentile_approx_raw(get_column(table, 'pct_state'), 0.95)

┌───────┐
│ 245.3  │
└───────┘
```

## SQL 语法

```sql
PERCENTILE_APPROX_RAW(<state>, <percentile>)
```

## SQL 示例

```sql
SELECT PERCENTILE_APPROX_RAW(pct_state, 0.95) FROM agg_table;

┌───────┐
│ 245.3  │
└───────┘
```
