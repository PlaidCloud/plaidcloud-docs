---
title: YEARWEEK (Lakehouse v2)
description: YEARWEEK — renvoie l'année et le numéro de semaine d'une date sous forme d'entier.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/yearweek.md
---

Renvoie l'année et le numéro de semaine d'une date sous forme d'entier.

## Syntaxe Analyze

```python
func.yearweek(<date>[, <mode>])
```

## Exemples Analyze

```python
func.yearweek('2024-06-15')

┌────────┐
│ 202424  │
└────────┘
```

## Syntaxe SQL

```sql
YEARWEEK(<date>[, <mode>])
```

## Exemples SQL

```sql
SELECT YEARWEEK('2024-06-15');

┌────────┐
│ 202424  │
└────────┘
```
