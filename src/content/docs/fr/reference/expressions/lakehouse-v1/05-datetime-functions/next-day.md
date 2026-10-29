---
title: NEXT_DAY (Lakehouse v1)
description: NEXT_DAY — renvoie la date du prochain jour de la semaine indiqué après la date ou l'horodatage donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/next-day.md
---

Renvoie la date du prochain jour de la semaine indiqué après la date ou l'horodatage donné.

## Syntaxe Analyze

```python
func.next_day(date_expression>, <target_day>)
```

## Exemples Analyze

```python
func.next_day(func.to_date('2024-11-13'), 'monday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'monday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-18                                           │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
NEXT_DAY(<date_expression>, <target_day>)
```

| Paramètre           | Description                                                                                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Valeur `DATE` ou `TIMESTAMP` servant à calculer la prochaine occurrence du jour indiqué.                                                                                 |
| `<target_day>`      | Jour de la semaine dont vous cherchez la prochaine occurrence. Valeurs acceptées : `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday` et `sunday`.      |

## Type de retour

Date.

## Exemples SQL

Pour trouver le lundi suivant une date donnée, par exemple 2024-11-13 :

```sql
SELECT NEXT_DAY(to_date('2024-11-13'), monday) AS next_monday;

┌─────────────┐
│ next_monday │
├─────────────┤
│ 2024-11-18  │
└─────────────┘
```
