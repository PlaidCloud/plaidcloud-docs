---
title: HLL_UNION_AGG (Lakehouse v2)
description: HLL_UNION_AGG — agrège des valeurs HLL en calculant leur union.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union-agg.md
---

Agrège des valeurs HLL en calculant leur union.

## Syntaxe Analyze

```python
func.hll_union_agg(get_column(table, 'hll_col'))
```

## Exemples Analyze

```python
func.hll_union_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## Syntaxe SQL

```sql
HLL_UNION_AGG(<hll_col>)
```

## Exemples SQL

```sql
SELECT HLL_CARDINALITY(HLL_UNION_AGG(hll_col)) FROM segments;

┌──────┐
│ 8000 │
└──────┘
```
