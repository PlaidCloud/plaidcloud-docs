---
title: HLL_RAW_AGG (Lakehouse v2)
description: HLL_RAW_AGG — agreguje wartości HLL do jednej wartości HLL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-raw-agg.md
---

Agreguje wartości HLL do jednej wartości HLL.

## Składnia Analyze

```python
func.hll_raw_agg(get_column(table, 'hll_col'))
```

## Przykłady Analyze

```python
func.hll_raw_agg(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## Składnia SQL

```sql
HLL_RAW_AGG(<hll_col>)
```

## Przykłady SQL

```sql
SELECT HLL_CARDINALITY(HLL_RAW_AGG(hll_col)) FROM sketches;

┌──────┐
│ 5000 │
└──────┘
```
