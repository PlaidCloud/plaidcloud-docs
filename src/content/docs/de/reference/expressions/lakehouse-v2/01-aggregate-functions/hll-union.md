---
title: HLL_UNION (Lakehouse v2)
description: HLL_UNION gibt die Vereinigung mehrerer HLL-Werte zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union.md
---

Gibt die Vereinigung mehrerer HLL-Werte zurück.

## Analyze-Syntax

```python
func.hll_union(get_column(table, 'hll_col'))
```

## Analyze-Beispiele

```python
func.hll_union(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## SQL-Syntax

```sql
HLL_UNION(<hll_col>)
```

## SQL-Beispiele

```sql
SELECT HLL_CARDINALITY(HLL_UNION(hll_col)) FROM daily_sketches;

┌───────┐
│ 12500 │
└───────┘
```
