---
title: DS_HLL_COMBINE (Lakehouse v2)
description: DS_HLL_COMBINE — combina vários sketches HLL do DataSketches em um único sketch.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-combine.md
---

Combina vários sketches HLL do DataSketches em um único sketch.

## Sintaxe no Analyze

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))
```

## Exemplos no Analyze

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))

┌───────────────────┐
│ (combined sketch) │
└───────────────────┘
```

## Sintaxe SQL

```sql
DS_HLL_COMBINE(<sketch_column>)
```

## Exemplos de SQL

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_COMBINE(sketch_col)) FROM daily_sketches;

┌───────┐
│ 25000 │
└───────┘
```
