---
title: MAKEDATE (Lakehouse v2)
description: MAKEDATE — crée une date à partir d'une année et d'un jour de l'année.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/makedate.md
---

Crée une date à partir d'une année et d'un jour de l'année.

## Syntaxe Analyze

```python
func.makedate(<year>, <dayofyear>)
```

## Exemples Analyze

```python
func.makedate(2024, 100)

┌──────────────┐
│ '2024-04-09'  │
└──────────────┘
```

## Syntaxe SQL

```sql
MAKEDATE(<year>, <dayofyear>)
```

## Exemples SQL

```sql
SELECT MAKEDATE(2024, 100);

┌────────────┐
│ 2024-04-09  │
└────────────┘
```
