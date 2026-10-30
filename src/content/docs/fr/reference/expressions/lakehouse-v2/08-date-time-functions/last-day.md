---
title: LAST_DAY (Lakehouse v2)
description: LAST_DAY — renvoie le dernier jour du mois pour une date donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/last-day.md
---

Renvoie le dernier jour du mois pour une date donnée.

## Syntaxe Analyze

```python
func.last_day(<date>[, <unit>])
```

## Exemples Analyze

```python
func.last_day('2024-02-15')

┌──────────────┐
│ '2024-02-29'  │
└──────────────┘
```

## Syntaxe SQL

```sql
LAST_DAY(<date>[, <unit>])
```

## Exemples SQL

```sql
SELECT LAST_DAY('2024-02-15');

┌────────────┐
│ 2024-02-29  │
└────────────┘
```
