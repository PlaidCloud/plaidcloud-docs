---
title: PERCENTILE_UNION (Lakehouse v2)
description: PERCENTILE_UNION — 返回多个百分位状态的并集。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-union.md
---

返回多个百分位状态的并集。

## Analyze 语法

```python
func.percentile_union(<state>)
```

## Analyze 示例

```python
func.percentile_union(get_column(table, 'pct_state'))

┌────────────────┐
│ (merged state)  │
└────────────────┘
```

## SQL 语法

```sql
PERCENTILE_UNION(<state>)
```

## SQL 示例

```sql
SELECT PERCENTILE_APPROX_RAW(PERCENTILE_UNION(pct_state), 0.5) FROM agg_table;

┌───────┐
│ 72500  │
└───────┘
```
