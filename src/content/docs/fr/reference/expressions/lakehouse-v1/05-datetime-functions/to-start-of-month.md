---
title: TO_START_OF_MONTH (Lakehouse v1)
description: TO_START_OF_MONTH — arrondit une date ou une date avec heure (horodatage/datetime) au premier jour du mois.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-month.md
---

Arrondit une date ou une date avec heure (horodatage/datetime) au premier jour du mois.
Renvoie la date.

## Syntaxe Analyze

```python
func.to_start_of_month(<expr>)
```

## Exemples Analyze

```python
func.to_start_of_month('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_month('2023-11-12 09:38:18.165575')           │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_START_OF_MONTH(<expr>)
```

## Arguments

| Arguments | Description     |
|-----------|-----------------|
| `<expr>`  | date/horodatage |

## Type de retour

`DATE`, renvoie la date au format « YYYY-MM-DD ».

## Exemples SQL

```sql
SELECT
  to_start_of_month('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_start_of_month('2023-11-12 09:38:18.165575') │
│                       Date                      │
├─────────────────────────────────────────────────┤
│ 2023-11-01                                      │
└─────────────────────────────────────────────────┘
```
