---
title: HLL_UNION (Lakehouse v2)
description: HLL_UNION — devolve a união de vários valores HLL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union.md
---

Devolve a união de vários valores HLL.

## Sintaxe do Analyze

```python
func.hll_union(get_column(table, 'hll_col'))
```

## Exemplos do Analyze

```python
func.hll_union(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## Sintaxe SQL

```sql
HLL_UNION(<hll_col>)
```

## Exemplos de SQL

```sql
SELECT HLL_CARDINALITY(HLL_UNION(hll_col)) FROM daily_sketches;

┌───────┐
│ 12500 │
└───────┘
```
