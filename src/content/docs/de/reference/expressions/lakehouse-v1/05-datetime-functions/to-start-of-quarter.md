---
title: TO_START_OF_QUARTER (Lakehouse v1)
description: TO_START_OF_QUARTER – rundet ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) auf den ersten Tag des Quartals ab.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-quarter.md
---

Rundet ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) auf den ersten Tag des Quartals ab.
Der erste Tag des Quartals ist der 1. Januar, 1. April, 1. Juli oder 1. Oktober.
Gibt das Datum zurück.

## Analyze-Syntax

```python
func.to_start_of_quarter(<expr>)
```

## Analyze-Beispiele

```python
func.to_start_of_quarter('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_quarter('2023-11-12 09:38:18.165575')         │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-10-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_START_OF_QUARTER(<expr>)
```

## Argumente

| Argumente | Beschreibung   |
|-----------|----------------|
| `<expr>`   | Datum/Timestamp |

## Rückgabetyp

`DATE`, gibt das Datum im Format „YYYY-MM-DD“ zurück.

## SQL-Beispiele

```sql
SELECT
  to_start_of_quarter('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────┐
│ to_start_of_quarter('2023-11-12 09:38:18.165575') │
│                        Date                       │
├───────────────────────────────────────────────────┤
│ 2023-10-01                                        │
└───────────────────────────────────────────────────┘
```
