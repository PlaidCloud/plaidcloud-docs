---
title: HLL_CARDINALITY (Lakehouse v2)
description: HLL_CARDINALITY – gibt die Kardinalitätsschätzung aus einem HLL-Wert zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-cardinality.md
---

Gibt die Kardinalitätsschätzung aus einem HLL-Wert zurück.

## Analyze-Syntax

```python
func.hll_cardinality(<hll>)
```

## Analyze-Beispiele

```python
func.hll_cardinality(get_column(table, 'hll_col'))

┌───────┐
│ 10000  │
└───────┘
```

## SQL-Syntax

```sql
HLL_CARDINALITY(<hll>)
```

## SQL-Beispiele

```sql
SELECT HLL_CARDINALITY(hll_col) FROM sketches;

┌───────┐
│ 10000  │
└───────┘
```
