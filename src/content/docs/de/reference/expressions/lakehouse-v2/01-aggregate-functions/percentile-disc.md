---
title: "PERCENTILE_DISC (Aggregat, Lakehouse v2)"
description: "Verwenden Sie die Aggregatfunktion PERCENTILE_DISC in PlaidCloud Lakehouse. Gibt den kleinsten Wert zurück, dessen kumulierte Verteilung >= dem angegebenen Perzentil ist."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc.md
---

Gibt den kleinsten Wert zurück, dessen kumulierte Verteilung >= dem angegebenen Perzentil ist.

## Analyze-Syntax

```python
func.percentile_disc(0.5)
```

## Analyze-Beispiele

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## SQL-Syntax

```sql
PERCENTILE_DISC(0.5)
```

## SQL-Beispiele

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
