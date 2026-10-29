---
title: PREVIOUS_DAY (Lakehouse v2)
description: PREVIOUS_DAY — renvoie la date du jour de la semaine spécifié précédant une date donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/previous-day.md
---

Renvoie la date du jour de la semaine spécifié précédant une date donnée.

## Syntaxe Analyze

```python
func.previous_day(<date>, <weekday>)
```

## Exemples Analyze

```python
func.previous_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-10'  │
└──────────────┘
```

## Syntaxe SQL

```sql
PREVIOUS_DAY(<date>, <weekday>)
```

## Exemples SQL

```sql
SELECT PREVIOUS_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-10  │
└────────────┘
```
