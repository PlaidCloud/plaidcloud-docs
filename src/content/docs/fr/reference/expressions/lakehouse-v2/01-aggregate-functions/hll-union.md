---
title: HLL_UNION (Lakehouse v2)
description: HLL_UNION — renvoie l'union de plusieurs valeurs HLL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/hll-union.md
---

Renvoie l'union de plusieurs valeurs HLL.

## Syntaxe Analyze

```python
func.hll_union(get_column(table, 'hll_col'))
```

## Exemples Analyze

```python
func.hll_union(get_column(table, 'hll_col'))

┌─────────────┐
│ (hll value) │
└─────────────┘
```

## Syntaxe SQL

```sql
HLL_UNION(<hll_col>)
```

## Exemples SQL

```sql
SELECT HLL_CARDINALITY(HLL_UNION(hll_col)) FROM daily_sketches;

┌───────┐
│ 12500 │
└───────┘
```
