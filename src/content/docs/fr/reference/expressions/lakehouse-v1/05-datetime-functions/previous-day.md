---
title: PREVIOUS_DAY (Lakehouse v1)
description: PREVIOUS_DAY — renvoie la date du jour de la semaine indiqué le plus récent avant la date donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/previous-day.md
---

Renvoie la date du jour de la semaine indiqué le plus récent avant la date ou l'horodatage donné.

## Syntaxe Analyze

```python
func.next_day(date_expression>, <target_day>)
```

## Exemples Analyze

```python
func.next_day(func.to_date('2024-11-13'), 'friday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'friday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-08                                           │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
PREVIOUS_DAY(<date_expression>, <target_day>)
```

| Paramètre           | Description                                                                                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Valeur `DATE` ou `TIMESTAMP` servant à calculer l'occurrence précédente du jour indiqué.                                                                                 |
| `<target_day>`      | Jour de la semaine dont vous cherchez l'occurrence précédente. Valeurs acceptées : `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday` et `sunday`.      |

## Type de retour

Date.

## Exemples SQL

Pour trouver le vendredi précédant une date donnée, par exemple 2024-11-13 :

```sql
SELECT PREVIOUS_DAY(to_date('2024-11-13'), friday) AS last_friday;

┌─────────────┐
│ last_friday │
├─────────────┤
│ 2024-11-08  │
└─────────────┘
```
