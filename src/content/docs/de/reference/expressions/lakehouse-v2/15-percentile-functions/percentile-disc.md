---
title: "PERCENTILE_DISC (Perzentil, Lakehouse v2)"
description: "Verwenden Sie die Perzentilfunktion PERCENTILE_DISC in PlaidCloud Lakehouse. Gibt den kleinsten Wert zurück, dessen kumulative Verteilung >= dem angegebenen Perzentil ist."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-disc.md
---

Gibt den kleinsten Wert zurück, dessen kumulative Verteilung >= dem angegebenen Perzentil ist.

## Analyze-Syntax

```python
func.percentile_disc(<percentile>)
```

## Analyze-Beispiele

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000  │
└───────┘
```

## SQL-Syntax

```sql
PERCENTILE_DISC(<percentile>)
```

## SQL-Beispiele

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000  │
└───────┘
```
