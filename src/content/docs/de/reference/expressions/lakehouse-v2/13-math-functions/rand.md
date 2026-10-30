---
title: RAND (Lakehouse v2)
description: RAND – gibt einen zufälligen Gleitkommawert zwischen 0 (einschließlich) und 1 (ausschließlich) zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/rand.md
---

Gibt einen zufälligen Gleitkommawert zwischen 0 (einschließlich) und 1 (ausschließlich) zurück.

## Analyze-Syntax

```python
func.rand([<seed>])
```

## Analyze-Beispiele

```python
func.rand()

┌───────────┐
│ 0.6347...  │
└───────────┘
```

## SQL-Syntax

```sql
RAND([<seed>])
```

## SQL-Beispiele

```sql
SELECT RAND();

┌───────────┐
│ 0.6347...  │
└───────────┘
```
