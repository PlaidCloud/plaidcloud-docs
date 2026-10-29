---
title: WEEK_ISO (Lakehouse v2)
description: WEEK_ISO — renvoie le numéro de semaine ISO de l'année pour une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/week-iso.md
---

Renvoie le numéro de semaine ISO de l'année pour une date.

## Syntaxe Analyze

```python
func.week_iso(<date>)
```

## Exemples Analyze

```python
func.week_iso('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## Syntaxe SQL

```sql
WEEK_ISO(<date>)
```

## Exemples SQL

```sql
SELECT WEEK_ISO('2024-06-15');

┌────┐
│ 24  │
└────┘
```
