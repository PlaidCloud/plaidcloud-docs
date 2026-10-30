---
title: HLL_EMPTY (Lakehouse v2)
description: HLL_EMPTY — devolve um valor HLL vazio.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-empty.md
---

Devolve um valor HLL vazio.

## Sintaxe de Analyze

```python
func.hll_empty()
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT HLL_CARDINALITY(HLL_EMPTY());

┌───┐
│ 0  │
└───┘
```
