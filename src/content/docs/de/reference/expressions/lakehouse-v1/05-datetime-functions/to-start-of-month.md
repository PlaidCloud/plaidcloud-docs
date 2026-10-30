---
title: TO_START_OF_MONTH (Lakehouse v1)
description: TO_START_OF_MONTH – rundet ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) auf den ersten Tag des Monats ab.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-month.md
---

Rundet ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) auf den ersten Tag des Monats ab.
Gibt das Datum zurück.

## Analyze-Syntax

```python
func.to_start_of_month(<expr>)
```

## Analyze-Beispiele

```python
func.to_start_of_month('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_month('2023-11-12 09:38:18.165575')           │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_START_OF_MONTH(<expr>)
```

## Argumente

| Argumente | Beschreibung      |
|-----------|-------------------|
| `<expr>`  | Datum/Zeitstempel |

## Rückgabetyp

`DATE`, gibt das Datum im Format „YYYY-MM-DD“ zurück.

## SQL-Beispiele

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
