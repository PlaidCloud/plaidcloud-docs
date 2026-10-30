---
title: PERCENTILE_DISC_LC (Lakehouse v2)
description: PERCENTILE_DISC_LC – gibt den Perzentilwert mit einem für niedrige Kardinalität optimierten Algorithmus zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc-lc.md
---

Gibt den Perzentilwert mit einem für niedrige Kardinalität optimierten Algorithmus zurück.

## Analyze-Syntax

```python
func.percentile_disc_lc(0.5)
```

## Analyze-Beispiele

```python
func.percentile_disc_lc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## SQL-Syntax

```sql
PERCENTILE_DISC_LC(0.5)
```

## SQL-Beispiele

```sql
SELECT PERCENTILE_DISC_LC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
