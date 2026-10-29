---
title: HLL_EMPTY (Lakehouse v2)
description: HLL_EMPTY — devuelve un valor HLL vacío.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-empty.md
---

Devuelve un valor HLL vacío.

## Sintaxis de Analyze

```python
func.hll_empty()
```

## Ejemplos de Analyze

```python
func.hll_empty()

┌─────────────┐
│ (empty hll)  │
└─────────────┘
```

## Sintaxis de SQL

```sql
HLL_EMPTY()
```

## Ejemplos de SQL

```sql
SELECT HLL_CARDINALITY(HLL_EMPTY());

┌───┐
│ 0  │
└───┘
```
