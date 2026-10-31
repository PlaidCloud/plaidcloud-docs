---
title: HLL_UNION_AGG (Lakehouse v2)
description: HLL_UNION_AGG — agreguje wartości HLL, obliczając ich sumę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union-agg.md
---

Agreguje wartości HLL, obliczając ich sumę.

## Składnia Analyze

```python
func.hll_union_agg(get_column(table, 'hll_col'))
```

## Przykłady Analyze

```python
func.hll_union_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## Składnia SQL

```sql
HLL_UNION_AGG(<hll_col>)
```

## Przykłady SQL

```sql
SELECT HLL_CARDINALITY(HLL_UNION_AGG(hll_col)) FROM segments;

┌──────┐
│ 8000 │
└──────┘
```
