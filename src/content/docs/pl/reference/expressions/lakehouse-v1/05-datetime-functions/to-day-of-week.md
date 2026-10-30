---
title: TO_DAY_OF_WEEK (Lakehouse v1)
description: TO_DAY_OF_WEEK — konwertuje datę lub datę z czasem (znacznik czasu/datetime) na liczbę UInt8.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-week.md
---

Konwertuje datę lub datę z czasem (znacznik czasu/datetime) na liczbę UInt8 zawierającą numer dnia tygodnia (poniedziałek to 1, a niedziela to 7).

## Składnia Analyze

```python
func.to_day_of_week(<expr>)
```

## Przykłady Analyze

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_week('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                  7 │
└────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_DAY_OF_WEEK(<expr>)
```

## Argumenty

| Argumenty | Opis                |
|-----------|---------------------|
| `<expr>`  | data/znacznik czasu |

## Zwracany typ

``TINYINT`

## Przykłady SQL

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
