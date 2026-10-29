---
title: HLL_UNION (Lakehouse v2)
description: HLL_UNION — zwraca sumę wielu wartości HLL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union.md
---

Zwraca sumę wielu wartości HLL.

## Składnia Analyze

```python
func.hll_union(get_column(table, 'hll_col'))
```

## Przykłady Analyze

```python
func.hll_union(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## Składnia SQL

```sql
HLL_UNION(<hll_col>)
```

## Przykłady SQL

```sql
SELECT HLL_CARDINALITY(HLL_UNION(hll_col)) FROM daily_sketches;

┌───────┐
│ 12500 │
└───────┘
```
