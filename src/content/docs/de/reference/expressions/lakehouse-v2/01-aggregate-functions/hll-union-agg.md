---
title: HLL_UNION_AGG (Lakehouse v2)
description: HLL_UNION_AGG aggregiert HLL-Werte durch Berechnung der Vereinigung.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union-agg.md
---

Aggregiert HLL-Werte durch Berechnung der Vereinigung.

## Analyze-Syntax

```python
func.hll_union_agg(get_column(table, 'hll_col'))
```

## Analyze-Beispiele

```python
func.hll_union_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQL-Syntax

```sql
HLL_UNION_AGG(<hll_col>)
```

## SQL-Beispiele

```sql
SELECT HLL_CARDINALITY(HLL_UNION_AGG(hll_col)) FROM segments;

┌──────┐
│ 8000 │
└──────┘
```
