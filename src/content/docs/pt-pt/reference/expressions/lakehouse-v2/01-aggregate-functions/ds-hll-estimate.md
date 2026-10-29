---
title: DS_HLL_ESTIMATE (Lakehouse v2)
description: DS_HLL_ESTIMATE — estima a cardinalidade a partir de um sketch HLL do DataSketches.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-estimate.md
---

Estima a cardinalidade a partir de um sketch HLL do DataSketches.

## Sintaxe do Analyze

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))
```

## Exemplos do Analyze

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))

┌──────┐
│ 9856 │
└──────┘
```

## Sintaxe SQL

```sql
DS_HLL_ESTIMATE(<sketch>)
```

## Exemplos de SQL

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
