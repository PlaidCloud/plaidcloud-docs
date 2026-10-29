---
title: "PERCENTILE_CONT (Perzentil, Lakehouse v2)"
description: PERCENTILE_CONT – gibt einen interpolierten Perzentilwert auf Grundlage einer stetigen Verteilung zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-cont.md
---

Gibt einen interpolierten Perzentilwert auf Grundlage einer stetigen Verteilung zurück.

## Analyze-Syntax

```python
func.percentile_cont(<percentile>)
```

## Analyze-Beispiele

```python
func.percentile_cont(0.5)

┌───────┐
│ 72500  │
└───────┘
```

## SQL-Syntax

```sql
PERCENTILE_CONT(<percentile>)
```

## SQL-Beispiele

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72500  │
└───────┘
```
