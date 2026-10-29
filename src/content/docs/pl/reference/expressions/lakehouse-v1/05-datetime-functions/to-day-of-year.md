---
title: TO_DAY_OF_YEAR (Lakehouse v1)
description: TO_DAY_OF_YEAR — konwertuje datę lub datę z czasem (znacznik czasu/datetime) na liczbę UInt16.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-year.md
---

Konwertuje datę lub datę z czasem (znacznik czasu/datetime) na liczbę UInt16 zawierającą numer dnia roku (1–366).

## Składnia Analyze

```python
func.to_day_of_year(<expr>)
```

## Przykłady Analyze

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_year('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                316 │
└────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
TO_DAY_OF_YEAR(<expr>)
```

## Argumenty

| Argumenty   | Opis        |
| ----------- | ----------- |
| `<expr>` | data/znacznik czasu |

## Zwracany typ

`SMALLINT`

## Przykłady SQL

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
