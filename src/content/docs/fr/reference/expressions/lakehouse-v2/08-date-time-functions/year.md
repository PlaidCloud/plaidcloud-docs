---
title: YEAR (Lakehouse v2)
description: YEAR — renvoie l'année d'une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/year.md
---

Renvoie l'année d'une date.

## Syntaxe Analyze

```python
func.year(<date>)
```

## Exemples Analyze

```python
func.year('2024-06-15')

┌──────┐
│ 2024  │
└──────┘
```

## Syntaxe SQL

```sql
YEAR(<date>)
```

## Exemples SQL

```sql
SELECT YEAR('2024-06-15');

┌──────┐
│ 2024  │
└──────┘
```
