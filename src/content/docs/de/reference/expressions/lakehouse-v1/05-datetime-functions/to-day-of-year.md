---
title: TO_DAY_OF_YEAR (Lakehouse v1)
description: TO_DAY_OF_YEAR – wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt16-Zahl um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-day-of-year.md
---

Wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt16-Zahl um, die den Tag des Jahres (1–366) enthält.

## Analyze-Syntax

```python
func.to_day_of_year(<expr>)
```

## Analyze-Beispiele

```python
func.to_day_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_day_of_year('2023-11-12 09:38:18.165575')  │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                316 │
└────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_DAY_OF_YEAR(<expr>)
```

## Argumente

| Argumente   | Beschreibung |
| ----------- | ----------- |
| `<expr>` | Datum/Zeitstempel |

## Rückgabetyp

`SMALLINT`

## SQL-Beispiele

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
