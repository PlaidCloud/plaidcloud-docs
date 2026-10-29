---
title: TO_DAY_OF_WEEK (Lakehouse v1)
description: TO_DAY_OF_WEEK – wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt8-Zahl um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-week.md
---

Wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt8-Zahl um, die den Wochentag enthält (Montag ist 1, Sonntag ist 7).

## Analyze-Syntax

```python
func.to_day_of_week(<expr>)
```

## Analyze-Beispiele

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_week('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                  7 │
└────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_DAY_OF_WEEK(<expr>)
```

## Argumente

| Argumente | Beschreibung      |
|-----------|-------------------|
| `<expr>`  | Datum/Zeitstempel |

## Rückgabetyp

``TINYINT`

## SQL-Beispiele

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
