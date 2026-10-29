---
title: HLL_UNION_AGG (Lakehouse v2)
description: HLL_UNION_AGG — agrega valores HLL calculando a união.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union-agg.md
---

Agrega valores HLL calculando a união.

## Sintaxe no Analyze

```python
func.hll_union_agg(get_column(table, 'hll_col'))
```

## Exemplos no Analyze

```python
func.hll_union_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## Sintaxe SQL

```sql
HLL_UNION_AGG(<hll_col>)
```

## Exemplos de SQL

```sql
SELECT HLL_CARDINALITY(HLL_UNION_AGG(hll_col)) FROM segments;

┌──────┐
│ 8000 │
└──────┘
```
