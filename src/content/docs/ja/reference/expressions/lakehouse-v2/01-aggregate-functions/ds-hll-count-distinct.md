---
title: DS_HLL_COUNT_DISTINCT（Lakehouse v2）
description: "PlaidCloud LakehouseでDS_HLL_COUNT_DISTINCT集計関数を使用します。DataSketches HLLアルゴリズムを使用して、異なる値のおおよその件数を返します。APPROX_COUNT_DISTINCTより高精度です。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-count-distinct.md
---

DataSketches HLLアルゴリズムを使用して、異なる値のおおよその件数を返します。`APPROX_COUNT_DISTINCT` より高精度です。

## Analyzeの構文

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))
```

## Analyzeの例

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10042 │
└───────┘
```

## SQLの構文

```sql
DS_HLL_COUNT_DISTINCT(<expr>)
```

## SQLの例

```sql
SELECT DS_HLL_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10042 │
└───────┘
```
