---
title: NEXT_DAY (Lakehouse v2)
description: NEXT_DAY — renvoie la date du prochain jour de la semaine spécifié après une date donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/next-day.md
---

Renvoie la date du prochain jour de la semaine spécifié après une date donnée.

## Syntaxe Analyze

```python
func.next_day(<date>, <weekday>)
```

## Exemples Analyze

```python
func.next_day('2024-06-15', 'Monday')

┌──────────────┐
│ '2024-06-17'  │
└──────────────┘
```

## Syntaxe SQL

```sql
NEXT_DAY(<date>, <weekday>)
```

## Exemples SQL

```sql
SELECT NEXT_DAY('2024-06-15', 'Monday');

┌────────────┐
│ 2024-06-17  │
└────────────┘
```
