---
title: DS_HLL_ESTIMATE (Lakehouse v2)
description: DS_HLL_ESTIMATE — estime la cardinalité à partir d'un sketch HLL DataSketches.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-estimate.md
---

Estime la cardinalité à partir d'un sketch HLL DataSketches.

## Syntaxe Analyze

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))
```

## Exemples Analyze

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))

┌──────┐
│ 9856 │
└──────┘
```

## Syntaxe SQL

```sql
DS_HLL_ESTIMATE(<sketch>)
```

## Exemples SQL

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
