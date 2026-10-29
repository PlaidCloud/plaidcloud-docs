---
title: HLL_HASH (Lakehouse v2)
description: HLL_HASH — calcula um hash HLL de um valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-hash.md
---

Calcula um hash HLL de um valor.

## Sintaxe do Analyze

```python
func.hll_hash(<expr>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT HLL_CARDINALITY(HLL_HASH('user_123'));

┌───┐
│ 1  │
└───┘
```
