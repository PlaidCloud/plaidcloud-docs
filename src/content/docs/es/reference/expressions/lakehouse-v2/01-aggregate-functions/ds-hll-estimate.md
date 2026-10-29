---
title: DS_HLL_ESTIMATE (Lakehouse v2)
description: DS_HLL_ESTIMATE estima la cardinalidad a partir de un esbozo HLL de DataSketches.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-estimate.md
---

Estima la cardinalidad a partir de un esbozo HLL de DataSketches.

## Sintaxis de Analyze

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))
```

## Ejemplos de Analyze

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))

┌──────┐
│ 9856 │
└──────┘
```

## Sintaxis de SQL

```sql
DS_HLL_ESTIMATE(<sketch>)
```

## Ejemplos de SQL

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
