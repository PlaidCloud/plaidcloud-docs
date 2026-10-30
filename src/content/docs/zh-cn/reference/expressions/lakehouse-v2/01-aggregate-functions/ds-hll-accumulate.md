---
title: DS_HLL_ACCUMULATE (Lakehouse v2)
description: "在 PlaidCloud Lakehouse 中使用 DS_HLL_ACCUMULATE 聚合函数。将值累积到 DataSketches HLL 草图中，用于近似去重计数。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-accumulate.md
---

将值累积到 DataSketches HLL 草图中，用于近似去重计数。

## Analyze 语法

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))
```

## Analyze 示例

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))

┌──────────────┐
│ (hll sketch) │
└──────────────┘
```

## SQL 语法

```sql
DS_HLL_ACCUMULATE(<expr>)
```

## SQL 示例

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
