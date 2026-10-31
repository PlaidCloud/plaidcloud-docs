---
title: TO_HOUR (Lakehouse v1)
description: TO_HOUR – wandelt ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt8-Zahl um, die die Stunde im 24-Stunden-Format (0–23) enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-hour.md
---

Wandelt ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt8-Zahl um, die die Stunde im 24-Stunden-Format (0–23) enthält.
Diese Funktion geht davon aus, dass die Uhren bei einer Vorstellung um eine Stunde um 2 Uhr morgens und bei einer Rückstellung um eine Stunde um 3 Uhr morgens umgestellt werden (was nicht immer zutrifft – selbst in Moskau wurden die Uhren zweimal zu einem anderen Zeitpunkt umgestellt).


## Analyze-Syntax

```python
func.to_hour(<expr>)
```

## Analyze-Beispiele

```python
func.to_hour('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_hour('2023-11-12 09:38:18.165575')         │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                  9 │
└────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_HOUR(<expr>)
```

## Argumente

| Argumente | Beschreibung |
|-----------|-------------|
| `<expr>`  | Zeitstempel |

## Rückgabetyp

`TINYINT`

## SQL-Beispiele

```sql
SELECT
    to_hour('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────┐
│ to_hour('2023-11-12 09:38:18.165575') │
│                 UInt8                 │
├───────────────────────────────────────┤
│                                     9 │
└───────────────────────────────────────┘
```
