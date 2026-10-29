---
title: HLL_CARDINALITY (Lakehouse v2)
description: HLL_CARDINALITY — zwraca szacowaną liczność z wartości HLL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-cardinality.md
---

Zwraca szacowaną liczność z wartości HLL.

## Składnia Analyze

```python
func.hll_cardinality(<hll>)
```

## Przykłady Analyze

```python
func.hll_cardinality(get_column(table, 'hll_col'))

┌───────┐
│ 10000  │
└───────┘
```

## Składnia SQL

```sql
HLL_CARDINALITY(<hll>)
```

## Przykłady SQL

```sql
SELECT HLL_CARDINALITY(hll_col) FROM sketches;

┌───────┐
│ 10000  │
└───────┘
```
