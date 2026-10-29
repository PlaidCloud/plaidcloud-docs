---
title: WEEK (Lakehouse v2)
description: WEEK — renvoie le numéro de semaine de l'année pour une date.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/week.md
---

Renvoie le numéro de semaine de l'année pour une date.

## Syntaxe Analyze

```python
func.week(<date>[, <mode>])
```

## Exemples Analyze

```python
func.week('2024-06-15')

┌────┐
│ 24  │
└────┘
```

## Syntaxe SQL

```sql
WEEK(<date>[, <mode>])
```

## Exemples SQL

```sql
SELECT WEEK('2024-06-15');

┌────┐
│ 24  │
└────┘
```
