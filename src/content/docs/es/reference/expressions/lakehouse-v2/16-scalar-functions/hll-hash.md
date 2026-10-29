---
title: HLL_HASH (Lakehouse v2)
description: HLL_HASH — calcula el hash HLL de un valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-hash.md
---

Calcula el hash HLL de un valor.

## Sintaxis de Analyze

```python
func.hll_hash(<expr>)
```

## Ejemplos de Analyze

```python
func.hll_hash('user_123')

┌───────┐
│ (hll)  │
└───────┘
```

## Sintaxis de SQL

```sql
HLL_HASH(<expr>)
```

## Ejemplos de SQL

```sql
SELECT HLL_CARDINALITY(HLL_HASH('user_123'));

┌───┐
│ 1  │
└───┘
```
