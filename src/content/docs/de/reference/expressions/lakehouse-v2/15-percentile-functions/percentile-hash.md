---
title: PERCENTILE_HASH (Lakehouse v2)
description: PERCENTILE_HASH – berechnet einen Perzentilzustand aus einem numerischen Wert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-hash.md
---

Berechnet einen Perzentilzustand aus einem numerischen Wert.

## Analyze-Syntax

```python
func.percentile_hash(<value>)
```

## Analyze-Beispiele

```python
func.percentile_hash(42.5)

┌─────────┐
│ (state)  │
└─────────┘
```

## SQL-Syntax

```sql
PERCENTILE_HASH(<value>)
```

## SQL-Beispiele

```sql
SELECT PERCENTILE_HASH(42.5);

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
