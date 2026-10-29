---
title: PERCENTILE_APPROX_RAW (Lakehouse v2)
description: "PlaidCloud LakehouseでPERCENTILE_APPROX_RAWパーセンタイル関数を使用します。事前に計算されたパーセンタイル状態から、近似のパーセンタイル値を返します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-approx-raw.md
---

事前に計算されたパーセンタイル状態から、近似のパーセンタイル値を返します。

## Analyzeの構文

```python
func.percentile_approx_raw(<state>, <percentile>)
```

## Analyzeの例

```python
func.percentile_approx_raw(get_column(table, 'pct_state'), 0.95)

┌───────┐
│ 245.3  │
└───────┘
```

## SQLの構文

```sql
PERCENTILE_APPROX_RAW(<state>, <percentile>)
```

## SQLの例

```sql
SELECT PERCENTILE_APPROX_RAW(pct_state, 0.95) FROM agg_table;

┌───────┐
│ 245.3  │
└───────┘
```
