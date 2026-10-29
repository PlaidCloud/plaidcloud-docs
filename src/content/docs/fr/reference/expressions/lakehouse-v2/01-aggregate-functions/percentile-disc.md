---
title: "PERCENTILE_DISC (agrégation, Lakehouse v2)"
description: "Utilisez la fonction d'agrégation PERCENTILE_DISC dans PlaidCloud Lakehouse. Renvoie la plus petite valeur dont la distribution cumulée est >= au percentile indiqué."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc.md
---

Renvoie la plus petite valeur dont la distribution cumulée est >= au percentile indiqué.

## Syntaxe Analyze

```python
func.percentile_disc(0.5)
```

## Exemples Analyze

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## Syntaxe SQL

```sql
PERCENTILE_DISC(0.5)
```

## Exemples SQL

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
