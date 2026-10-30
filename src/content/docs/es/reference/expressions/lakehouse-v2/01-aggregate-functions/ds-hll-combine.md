---
title: DS_HLL_COMBINE (Lakehouse v2)
description: DS_HLL_COMBINE combina varios esbozos HLL de DataSketches en un único esbozo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-combine.md
---

Combina varios esbozos HLL de DataSketches en un único esbozo.

## Sintaxis de Analyze

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))
```

## Ejemplos de Analyze

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))

┌───────────────────┐
│ (combined sketch) │
└───────────────────┘
```

## Sintaxis de SQL

```sql
DS_HLL_COMBINE(<sketch_column>)
```

## Ejemplos de SQL

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_COMBINE(sketch_col)) FROM daily_sketches;

┌───────┐
│ 25000 │
└───────┘
```
