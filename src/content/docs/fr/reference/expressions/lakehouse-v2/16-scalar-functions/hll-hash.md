---
title: HLL_HASH (Lakehouse v2)
description: HLL_HASH — calcule le hachage HLL d'une valeur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-hash.md
---

Calcule le hachage HLL d'une valeur.

## Syntaxe Analyze

```python
func.hll_hash(<expr>)
```

## Exemples Analyze

```python
func.hll_hash('user_123')

┌───────┐
│ (hll)  │
└───────┘
```

## Syntaxe SQL

```sql
HLL_HASH(<expr>)
```

## Exemples SQL

```sql
SELECT HLL_CARDINALITY(HLL_HASH('user_123'));

┌───┐
│ 1  │
└───┘
```
