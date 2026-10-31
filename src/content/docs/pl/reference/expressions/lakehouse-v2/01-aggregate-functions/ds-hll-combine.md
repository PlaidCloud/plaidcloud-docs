---
title: DS_HLL_COMBINE (Lakehouse v2)
description: DS_HLL_COMBINE — łączy wiele szkiców HLL DataSketches w jeden szkic.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-combine.md
---

Łączy wiele szkiców HLL DataSketches w jeden szkic.

## Składnia Analyze

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))
```

## Przykłady Analyze

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))

┌───────────────────┐
│ (combined sketch) │
└───────────────────┘
```

## Składnia SQL

```sql
DS_HLL_COMBINE(<sketch_column>)
```

## Przykłady SQL

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_COMBINE(sketch_col)) FROM daily_sketches;

┌───────┐
│ 25000 │
└───────┘
```
