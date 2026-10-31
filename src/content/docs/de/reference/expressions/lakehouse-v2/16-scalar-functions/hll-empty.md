---
title: HLL_EMPTY (Lakehouse v2)
description: HLL_EMPTY – gibt einen leeren HLL-Wert zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/16-scalar-functions/hll-empty.md
---

Gibt einen leeren HLL-Wert zurück.

## Analyze-Syntax

```python
func.hll_empty()
```

## Analyze-Beispiele

```python
func.hll_empty()

┌─────────────┐
│ (empty hll)  │
└─────────────┘
```

## SQL-Syntax

```sql
HLL_EMPTY()
```

## SQL-Beispiele

```sql
SELECT HLL_CARDINALITY(HLL_EMPTY());

┌───┐
│ 0  │
└───┘
```
