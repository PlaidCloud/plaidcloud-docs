---
title: HLL_UNION (Lakehouse v2)
description: HLL_UNION devuelve la unión de varios valores HLL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union.md
---

Devuelve la unión de varios valores HLL.

## Sintaxis de Analyze

```python
func.hll_union(get_column(table, 'hll_col'))
```

## Ejemplos de Analyze

```python
func.hll_union(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## Sintaxis de SQL

```sql
HLL_UNION(<hll_col>)
```

## Ejemplos de SQL

```sql
SELECT HLL_CARDINALITY(HLL_UNION(hll_col)) FROM daily_sketches;

┌───────┐
│ 12500 │
└───────┘
```
