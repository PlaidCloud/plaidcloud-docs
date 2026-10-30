---
title: "PERCENTILE_CONT (Percentile, Lakehouse v2)"
description: PERCENTILE_CONT — renvoie une valeur de centile interpolée à partir d'une distribution continue.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-cont.md
---

Renvoie une valeur de centile interpolée à partir d'une distribution continue.

## Syntaxe Analyze

```python
func.percentile_cont(<percentile>)
```

## Exemples Analyze

```python
func.percentile_cont(0.5)

┌───────┐
│ 72500  │
└───────┘
```

## Syntaxe SQL

```sql
PERCENTILE_CONT(<percentile>)
```

## Exemples SQL

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72500  │
└───────┘
```
