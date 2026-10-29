---
title: TO_START_OF_ISO_YEAR (Lakehouse v1)
description: TO_START_OF_ISO_YEAR – gibt den ersten Tag des ISO-Jahres für ein Datum oder ein Datum mit Uhrzeit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-iso-year.md
---

Gibt den ersten Tag des ISO-Jahres für ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) zurück.

## Analyze-Syntax

```python
func.to_start_of_iso_year(<expr>)
```

## Analyze-Beispiele

```python
func.to_start_of_iso_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_iso_year('2023-11-12 09:38:18.165575')        │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-01-02                                                     │
└────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_START_OF_ISO_YEAR(<expr>)
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
  to_start_of_iso_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ to_start_of_iso_year('2023-11-12 09:38:18.165575') │
│                        Date                        │
├────────────────────────────────────────────────────┤
│ 2023-01-02                                         │
└────────────────────────────────────────────────────┘
```
