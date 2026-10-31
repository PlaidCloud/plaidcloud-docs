---
title: "PERCENTILE_DISC (Percentile, Lakehouse v2)"
description: "Utilisez la fonction de centile PERCENTILE_DISC dans PlaidCloud Lakehouse. Renvoie la plus petite valeur dont la distribution cumulative est >= au centile spécifié."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-disc.md
---

Renvoie la plus petite valeur dont la distribution cumulative est >= au centile spécifié.

## Syntaxe Analyze

```python
func.percentile_disc(<percentile>)
```

## Exemples Analyze

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000  │
└───────┘
```

## Syntaxe SQL

```sql
PERCENTILE_DISC(<percentile>)
```

## Exemples SQL

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000  │
└───────┘
```
