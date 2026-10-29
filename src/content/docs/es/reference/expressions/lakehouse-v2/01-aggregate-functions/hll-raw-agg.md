---
title: HLL_RAW_AGG (Lakehouse v2)
description: HLL_RAW_AGG agrega valores HLL en un único valor HLL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-raw-agg.md
---

Agrega valores HLL en un único valor HLL.

## Sintaxis de Analyze

```python
func.hll_raw_agg(get_column(table, 'hll_col'))
```

## Ejemplos de Analyze

```python
func.hll_raw_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## Sintaxis de SQL

```sql
HLL_RAW_AGG(<hll_col>)
```

## Ejemplos de SQL

```sql
SELECT HLL_CARDINALITY(HLL_RAW_AGG(hll_col)) FROM sketches;

┌──────┐
│ 5000 │
└──────┘
```
