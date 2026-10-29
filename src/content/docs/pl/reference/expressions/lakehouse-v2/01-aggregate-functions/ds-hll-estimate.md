---
title: DS_HLL_ESTIMATE (Lakehouse v2)
description: DS_HLL_ESTIMATE — szacuje liczność na podstawie szkicu HLL DataSketches.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-estimate.md
---

Szacuje liczność na podstawie szkicu HLL DataSketches.

## Składnia Analyze

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))
```

## Przykłady Analyze

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))

┌──────┐
│ 9856 │
└──────┘
```

## Składnia SQL

```sql
DS_HLL_ESTIMATE(<sketch>)
```

## Przykłady SQL

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
