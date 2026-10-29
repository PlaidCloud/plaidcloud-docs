---
title: HLL_CARDINALITY (Lakehouse v2)
description: HLL_CARDINALITY — renvoie l'estimation de cardinalité d'une valeur HLL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-cardinality.md
---

Renvoie l'estimation de cardinalité d'une valeur HLL.

## Syntaxe Analyze

```python
func.hll_cardinality(<hll>)
```

## Exemples Analyze

```python
func.hll_cardinality(get_column(table, 'hll_col'))

┌───────┐
│ 10000  │
└───────┘
```

## Syntaxe SQL

```sql
HLL_CARDINALITY(<hll>)
```

## Exemples SQL

```sql
SELECT HLL_CARDINALITY(hll_col) FROM sketches;

┌───────┐
│ 10000  │
└───────┘
```
