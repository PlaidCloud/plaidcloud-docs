---
title: DS_HLL_COMBINE (Lakehouse v2)
description: DS_HLL_COMBINE kombiniert mehrere DataSketches-HLL-Sketches zu einem einzigen Sketch.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-combine.md
---

Kombiniert mehrere DataSketches-HLL-Sketches zu einem einzigen Sketch.

## Analyze-Syntax

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))
```

## Analyze-Beispiele

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))

┌───────────────────┐
│ (combined sketch) │
└───────────────────┘
```

## SQL-Syntax

```sql
DS_HLL_COMBINE(<sketch_column>)
```

## SQL-Beispiele

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_COMBINE(sketch_col)) FROM daily_sketches;

┌───────┐
│ 25000 │
└───────┘
```
