---
title: PERCENTILE_APPROX_RAW (Lakehouse v2)
description: "Verwenden Sie die Perzentilfunktion PERCENTILE_APPROX_RAW in PlaidCloud Lakehouse. Gibt einen näherungsweisen Perzentilwert aus einem vorab berechneten Perzentilzustand zurück."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-approx-raw.md
---

Gibt einen näherungsweisen Perzentilwert aus einem vorab berechneten Perzentilzustand zurück.

## Analyze-Syntax

```python
func.percentile_approx_raw(<state>, <percentile>)
```

## Analyze-Beispiele

```python
func.percentile_approx_raw(get_column(table, 'pct_state'), 0.95)

┌───────┐
│ 245.3  │
└───────┘
```

## SQL-Syntax

```sql
PERCENTILE_APPROX_RAW(<state>, <percentile>)
```

## SQL-Beispiele

```sql
SELECT PERCENTILE_APPROX_RAW(pct_state, 0.95) FROM agg_table;

┌───────┐
│ 245.3  │
└───────┘
```
