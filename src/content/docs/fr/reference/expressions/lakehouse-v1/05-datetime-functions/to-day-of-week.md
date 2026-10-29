---
title: TO_DAY_OF_WEEK (Lakehouse v1)
description: TO_DAY_OF_WEEK — convertit une date ou une date avec heure (horodatage/datetime) en nombre UInt8.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-week.md
---

Convertit une date ou une date avec heure (horodatage/datetime) en nombre UInt8 contenant le numéro du jour de la semaine (le lundi vaut 1 et le dimanche 7).

## Syntaxe Analyze

```python
func.to_day_of_week(<expr>)
```

## Exemples Analyze

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_week('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                  7 │
└────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_DAY_OF_WEEK(<expr>)
```

## Arguments

| Arguments | Description      |
|-----------|------------------|
| `<expr>`  | date/horodatage  |

## Type de retour

``TINYINT`

## Exemples SQL

```sql

SELECT
    to_day_of_week('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ to_day_of_week('2023-11-12 09:38:18.165575') │
│                     UInt8                    │
├──────────────────────────────────────────────┤
│                                            7 │
└──────────────────────────────────────────────┘
```
