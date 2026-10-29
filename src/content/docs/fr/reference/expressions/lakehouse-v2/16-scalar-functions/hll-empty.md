---
title: HLL_EMPTY (Lakehouse v2)
description: HLL_EMPTY — renvoie une valeur HLL vide.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-empty.md
---

Renvoie une valeur HLL vide.

## Syntaxe Analyze

```python
func.hll_empty()
```

## Exemples Analyze

```python
func.hll_empty()

┌─────────────┐
│ (empty hll)  │
└─────────────┘
```

## Syntaxe SQL

```sql
HLL_EMPTY()
```

## Exemples SQL

```sql
SELECT HLL_CARDINALITY(HLL_EMPTY());

┌───┐
│ 0  │
└───┘
```
