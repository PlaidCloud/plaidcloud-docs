---
title: LAST_DAY (Lakehouse v1)
description: LAST_DAY — renvoie le dernier jour de l'intervalle indiqué (semaine, mois, trimestre ou année).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/last-day.md
---

Renvoie le dernier jour de l'intervalle indiqué (semaine, mois, trimestre ou année) d'après la date ou l'horodatage fourni.

## Syntaxe Analyze

```python
func.last_day(<date_expression>, <interval>)
```

## Exemples Analyze

```python
func.last_day(func.to_date('2024-11-13'), 'month')
┌──────────────────────────────────────────────────────┐
│ func.last_day(func.to_date('2024-11-13'), 'month')   │
├──────────────────────────────────────────────────────┤
│ 2024-11-30                                           │
└──────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
LAST_DAY(<date_expression>, <interval>)
```

| Paramètre           | Description                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | Valeur DATE ou TIMESTAMP servant à calculer le dernier jour de l'intervalle indiqué.                          |
| `<interval>`        | Type d'intervalle dont vous voulez le dernier jour. Valeurs acceptées : `week`, `month`, `quarter` et `year`. |

## Type de retour

Date.

## Exemples SQL

Supposons que vous souhaitiez déterminer la date de facturation, qui est toujours le dernier jour du mois, à partir d'une date de transaction quelconque (par ex. 2024-11-13) :

```sql
SELECT LAST_DAY(to_date('2024-11-13'), month) AS billing_date;

┌──────────────┐
│ billing_date │
├──────────────┤
│ 2024-11-30   │
└──────────────┘
```
