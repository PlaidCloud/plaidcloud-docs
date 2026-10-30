---
title: PERCENTILE_EMPTY (Lakehouse v2)
description: PERCENTILE_EMPTY – gibt einen leeren Perzentilzustand zur Initialisierung zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-empty.md
---

Gibt einen leeren Perzentilzustand zur Initialisierung zurück.

## Analyze-Syntax

```python
func.percentile_empty()
```

## Analyze-Beispiele

```python
func.percentile_empty()

┌───────────────┐
│ (empty state)  │
└───────────────┘
```

## SQL-Syntax

```sql
PERCENTILE_EMPTY()
```

## SQL-Beispiele

```sql
SELECT PERCENTILE_EMPTY();

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
