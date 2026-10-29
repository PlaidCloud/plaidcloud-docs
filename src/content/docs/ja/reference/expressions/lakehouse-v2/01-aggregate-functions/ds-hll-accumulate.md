---
title: DS_HLL_ACCUMULATE（Lakehouse v2）
description: "PlaidCloud LakehouseでDS_HLL_ACCUMULATE集計関数を使用します。値をDataSketches HLLスケッチに蓄積し、異なる値のおおよその件数を求められるようにします。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-accumulate.md
---

値をDataSketches HLLスケッチに蓄積し、異なる値のおおよその件数を求められるようにします。

## Analyzeの構文

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))
```

## Analyzeの例

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))

┌──────────────┐
│ (hll sketch) │
└──────────────┘
```

## SQLの構文

```sql
DS_HLL_ACCUMULATE(<expr>)
```

## SQLの例

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
