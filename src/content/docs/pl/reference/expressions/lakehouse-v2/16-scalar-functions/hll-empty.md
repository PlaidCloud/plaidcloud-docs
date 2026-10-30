---
title: HLL_EMPTY (Lakehouse v2)
description: HLL_EMPTY — zwraca pustą wartość HLL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-empty.md
---

Zwraca pustą wartość HLL.

## Składnia Analyze

```python
func.hll_empty()
```

## Przykłady Analyze

```python
func.hll_empty()

┌─────────────┐
│ (empty hll)  │
└─────────────┘
```

## Składnia SQL

```sql
HLL_EMPTY()
```

## Przykłady SQL

```sql
SELECT HLL_CARDINALITY(HLL_EMPTY());

┌───┐
│ 0  │
└───┘
```
