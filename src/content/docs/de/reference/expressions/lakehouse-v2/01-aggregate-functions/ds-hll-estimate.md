---
title: DS_HLL_ESTIMATE (Lakehouse v2)
description: DS_HLL_ESTIMATE schätzt die Kardinalität anhand eines DataSketches-HLL-Sketches.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-estimate.md
---

Schätzt die Kardinalität anhand eines DataSketches-HLL-Sketches.

## Analyze-Syntax

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))
```

## Analyze-Beispiele

```python
func.ds_hll_estimate(get_column(table, 'hll_sketch'))

┌──────┐
│ 9856 │
└──────┘
```

## SQL-Syntax

```sql
DS_HLL_ESTIMATE(<sketch>)
```

## SQL-Beispiele

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
