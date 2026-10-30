---
title: PERCENTILE_UNION (Lakehouse v2)
description: PERCENTILE_UNION – gibt die Vereinigung mehrerer Perzentilzustände zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-union.md
---

Gibt die Vereinigung mehrerer Perzentilzustände zurück.

## Analyze-Syntax

```python
func.percentile_union(<state>)
```

## Analyze-Beispiele

```python
func.percentile_union(get_column(table, 'pct_state'))

┌────────────────┐
│ (merged state)  │
└────────────────┘
```

## SQL-Syntax

```sql
PERCENTILE_UNION(<state>)
```

## SQL-Beispiele

```sql
SELECT PERCENTILE_APPROX_RAW(PERCENTILE_UNION(pct_state), 0.5) FROM agg_table;

┌───────┐
│ 72500  │
└───────┘
```
