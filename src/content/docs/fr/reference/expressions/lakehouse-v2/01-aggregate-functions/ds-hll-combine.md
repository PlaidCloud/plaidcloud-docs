---
title: DS_HLL_COMBINE (Lakehouse v2)
description: DS_HLL_COMBINE — combine plusieurs sketches HLL DataSketches en un seul sketch.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-combine.md
---

Combine plusieurs sketches HLL DataSketches en un seul sketch.

## Syntaxe Analyze

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))
```

## Exemples Analyze

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))

┌───────────────────┐
│ (combined sketch) │
└───────────────────┘
```

## Syntaxe SQL

```sql
DS_HLL_COMBINE(<sketch_column>)
```

## Exemples SQL

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_COMBINE(sketch_col)) FROM daily_sketches;

┌───────┐
│ 25000 │
└───────┘
```
