---
title: TO_DAY_OF_YEAR (Lakehouse v1)
description: TO_DAY_OF_YEAR — convertit une date ou une date avec heure (horodatage/datetime) en nombre UInt16.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-year.md
---

Convertit une date ou une date avec heure (horodatage/datetime) en nombre UInt16 contenant le numéro du jour de l'année (1-366).

## Syntaxe Analyze

```python
func.to_day_of_year(<expr>)
```

## Exemples Analyze

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_year('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                316 │
└────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_DAY_OF_YEAR(<expr>)
```

## Arguments

| Arguments   | Description |
| ----------- | ----------- |
| `<expr>` | date/horodatage |

## Type de retour

`SMALLINT`

## Exemples SQL

```sql
SELECT
    to_day_of_year('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ to_day_of_year('2023-11-12 09:38:18.165575') │
│                    UInt16                    │
├──────────────────────────────────────────────┤
│                                          316 │
└──────────────────────────────────────────────┘
```
