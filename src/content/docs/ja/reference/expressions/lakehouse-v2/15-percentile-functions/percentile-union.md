---
title: PERCENTILE_UNION (Lakehouse v2)
description: PERCENTILE_UNION — 複数のパーセンタイル状態の和集合を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-union.md
---

複数のパーセンタイル状態の和集合を返します。

## Analyzeの構文

```python
func.percentile_union(<state>)
```

## Analyzeの例

```python
func.percentile_union(get_column(table, 'pct_state'))

┌────────────────┐
│ (merged state)  │
└────────────────┘
```

## SQLの構文

```sql
PERCENTILE_UNION(<state>)
```

## SQLの例

```sql
SELECT PERCENTILE_APPROX_RAW(PERCENTILE_UNION(pct_state), 0.5) FROM agg_table;

┌───────┐
│ 72500  │
└───────┘
```
