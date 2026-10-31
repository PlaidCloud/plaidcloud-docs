---
title: HLL_CARDINALITY (Lakehouse v2)
description: HLL_CARDINALITY — devolve a estimativa de cardinalidade de um valor HLL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-cardinality.md
---

Devolve a estimativa de cardinalidade de um valor HLL.

## Sintaxe de Analyze

```python
func.hll_cardinality(<hll>)
```

## Exemplos de Analyze

```python
func.hll_cardinality(get_column(table, 'hll_col'))

┌───────┐
│ 10000  │
└───────┘
```

## Sintaxe SQL

```sql
HLL_CARDINALITY(<hll>)
```

## Exemplos SQL

```sql
SELECT HLL_CARDINALITY(hll_col) FROM sketches;

┌───────┐
│ 10000  │
└───────┘
```
