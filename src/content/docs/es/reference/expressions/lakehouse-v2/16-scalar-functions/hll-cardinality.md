---
title: HLL_CARDINALITY (Lakehouse v2)
description: HLL_CARDINALITY — devuelve la estimación de cardinalidad de un valor HLL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-cardinality.md
---

Devuelve la estimación de cardinalidad de un valor HLL.

## Sintaxis de Analyze

```python
func.hll_cardinality(<hll>)
```

## Ejemplos de Analyze

```python
func.hll_cardinality(get_column(table, 'hll_col'))

┌───────┐
│ 10000  │
└───────┘
```

## Sintaxis de SQL

```sql
HLL_CARDINALITY(<hll>)
```

## Ejemplos de SQL

```sql
SELECT HLL_CARDINALITY(hll_col) FROM sketches;

┌───────┐
│ 10000  │
└───────┘
```
