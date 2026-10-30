---
title: HLL_HASH (Lakehouse v2)
description: HLL_HASH — calcula o hash HLL de um valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-hash.md
---

Calcula o hash HLL de um valor.

## Sintaxe de Analyze

```python
func.hll_hash(<expr>)
```

## Exemplos de Analyze

```python
func.hll_hash('user_123')

┌───────┐
│ (hll)  │
└───────┘
```

## Sintaxe SQL

```sql
HLL_HASH(<expr>)
```

## Exemplos SQL

```sql
SELECT HLL_CARDINALITY(HLL_HASH('user_123'));

┌───┐
│ 1  │
└───┘
```
