---
title: HLL_RAW_AGG (Lakehouse v2)
description: HLL_RAW_AGG aggregiert HLL-Werte zu einem einzigen HLL-Wert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-raw-agg.md
---

Aggregiert HLL-Werte zu einem einzigen HLL-Wert.

## Analyze-Syntax

```python
func.hll_raw_agg(get_column(table, 'hll_col'))
```

## Analyze-Beispiele

```python
func.hll_raw_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQL-Syntax

```sql
HLL_RAW_AGG(<hll_col>)
```

## SQL-Beispiele

```sql
SELECT HLL_CARDINALITY(HLL_RAW_AGG(hll_col)) FROM sketches;

┌──────┐
│ 5000 │
└──────┘
```
