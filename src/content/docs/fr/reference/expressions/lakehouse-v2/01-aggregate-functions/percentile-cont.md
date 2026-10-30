---
title: "PERCENTILE_CONT (agrégation, Lakehouse v2)"
description: PERCENTILE_CONT — renvoie une valeur de percentile interpolée à partir d'une distribution continue.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-cont.md
---

Renvoie une valeur de percentile interpolée à partir d'une distribution continue.

## Syntaxe Analyze

```python
func.percentile_cont(0.5)
```

## Exemples Analyze

```python
func.percentile_cont(0.5)

┌──────────┐
│ 72500.00 │
└──────────┘
```

## Syntaxe SQL

```sql
PERCENTILE_CONT(0.5)
```

## Exemples SQL

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌──────────┐
│ 72500.00 │
└──────────┘
```
