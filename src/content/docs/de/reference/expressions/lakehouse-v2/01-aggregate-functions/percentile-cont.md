---
title: "PERCENTILE_CONT (Aggregat, Lakehouse v2)"
description: PERCENTILE_CONT – gibt einen interpolierten Perzentilwert auf Basis einer stetigen Verteilung zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-cont.md
---

Gibt einen interpolierten Perzentilwert auf Basis einer stetigen Verteilung zurück.

## Analyze-Syntax

```python
func.percentile_cont(0.5)
```

## Analyze-Beispiele

```python
func.percentile_cont(0.5)

┌──────────┐
│ 72500.00 │
└──────────┘
```

## SQL-Syntax

```sql
PERCENTILE_CONT(0.5)
```

## SQL-Beispiele

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌──────────┐
│ 72500.00 │
└──────────┘
```
