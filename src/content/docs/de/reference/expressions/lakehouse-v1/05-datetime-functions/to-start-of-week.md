---
title: TO_START_OF_WEEK (Lakehouse v1)
description: TO_START_OF_WEEK – gibt den ersten Tag der Woche für ein Datum oder ein Datum mit Uhrzeit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-week.md
---

Gibt den ersten Tag der Woche für ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) zurück.
Der erste Tag einer Woche kann Sonntag oder Montag sein, was über das Argument `mode` festgelegt wird.

## Analyze-Syntax

```python
func.to_start_of_week(<expr>)
```

## Analyze-Beispiele

```python
func.to_start_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_week('2023-11-12 09:38:18.165575')            │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12                                                     │
└────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_START_OF_WEEK(<expr> [, mode])
```

## Argumente

| Argumente | Beschreibung                                                                                        |
|-----------|-----------------------------------------------------------------------------------------------------|
| `<expr>`  | Datum/Timestamp                                                                                     |
| `[mode]`  | Optional. Bei 0 ist das Ergebnis ein Sonntag, andernfalls ein Montag. Der Standardwert ist 0        |

## Rückgabetyp

`DATE`, gibt das Datum im Format „YYYY-MM-DD“ zurück.

## SQL-Beispiele

```sql
SELECT
  to_start_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ to_start_of_week('2023-11-12 09:38:18.165575') │
│                      Date                      │
├────────────────────────────────────────────────┤
│ 2023-11-12                                     │
└────────────────────────────────────────────────┘
```
