---
title: HLL_CARDINALITY (Lakehouse v2)
description: HLL_CARDINALITY — retorna a estimativa de cardinalidade de um valor HLL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-cardinality.md
---

Retorna a estimativa de cardinalidade de um valor HLL.

## Sintaxe do Analyze

```python
func.hll_cardinality(<hll>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT HLL_CARDINALITY(hll_col) FROM sketches;

┌───────┐
│ 10000  │
└───────┘
```
