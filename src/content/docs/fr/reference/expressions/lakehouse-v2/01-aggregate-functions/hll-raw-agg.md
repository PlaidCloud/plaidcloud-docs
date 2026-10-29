---
title: HLL_RAW_AGG (Lakehouse v2)
description: HLL_RAW_AGG — agrège des valeurs HLL en une seule valeur HLL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-raw-agg.md
---

Agrège des valeurs HLL en une seule valeur HLL.

## Syntaxe Analyze

```python
func.hll_raw_agg(get_column(table, 'hll_col'))
```

## Exemples Analyze

```python
func.hll_raw_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## Syntaxe SQL

```sql
HLL_RAW_AGG(<hll_col>)
```

## Exemples SQL

```sql
SELECT HLL_CARDINALITY(HLL_RAW_AGG(hll_col)) FROM sketches;

┌──────┐
│ 5000 │
└──────┘
```
