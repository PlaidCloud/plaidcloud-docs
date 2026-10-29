---
title: HLL_RAW_AGG (Lakehouse v2)
description: HLL_RAW_AGG — agrega valores HLL em um único valor HLL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-raw-agg.md
---

Agrega valores HLL em um único valor HLL.

## Sintaxe no Analyze

```python
func.hll_raw_agg(get_column(table, 'hll_col'))
```

## Exemplos no Analyze

```python
func.hll_raw_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## Sintaxe SQL

```sql
HLL_RAW_AGG(<hll_col>)
```

## Exemplos de SQL

```sql
SELECT HLL_CARDINALITY(HLL_RAW_AGG(hll_col)) FROM sketches;

┌──────┐
│ 5000 │
└──────┘
```
