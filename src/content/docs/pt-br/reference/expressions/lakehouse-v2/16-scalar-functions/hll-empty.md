---
title: HLL_EMPTY (Lakehouse v2)
description: HLL_EMPTY — retorna um valor HLL vazio.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-empty.md
---

Retorna um valor HLL vazio.

## Sintaxe do Analyze

```python
func.hll_empty()
```

## Exemplos do Analyze

```python
func.hll_empty()

┌─────────────┐
│ (empty hll)  │
└─────────────┘
```

## Sintaxe SQL

```sql
HLL_EMPTY()
```

## Exemplos de SQL

```sql
SELECT HLL_CARDINALITY(HLL_EMPTY());

┌───┐
│ 0  │
└───┘
```
