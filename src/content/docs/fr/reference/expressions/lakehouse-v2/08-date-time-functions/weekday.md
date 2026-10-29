---
title: WEEKDAY (Lakehouse v2)
description: WEEKDAY — renvoie l'indice du jour de la semaine pour une date (0 = lundi, 6 = dimanche).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/weekday.md
---

Renvoie l'indice du jour de la semaine pour une date (0 = lundi, 6 = dimanche).

## Syntaxe Analyze

```python
func.weekday(<date>)
```

## Exemples Analyze

```python
func.weekday('2024-06-15')

┌───┐
│ 5  │
└───┘
```

## Syntaxe SQL

```sql
WEEKDAY(<date>)
```

## Exemples SQL

```sql
SELECT WEEKDAY('2024-06-15');

┌───┐
│ 5  │
└───┘
```
