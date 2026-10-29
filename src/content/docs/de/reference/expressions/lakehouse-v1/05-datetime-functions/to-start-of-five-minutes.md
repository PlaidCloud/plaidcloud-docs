---
title: TO_START_OF_FIVE_MINUTES (Lakehouse v1)
description: TO_START_OF_FIVE_MINUTES – rundet ein Datum mit Uhrzeit (Timestamp/Datetime) auf den Beginn des Fünf-Minuten-Intervalls ab.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-five-minutes.md
---

Rundet ein Datum mit Uhrzeit (Timestamp/Datetime) auf den Beginn des Fünf-Minuten-Intervalls ab.

## Analyze-Syntax

```python
func.to_start_of_five_minutes(<expr>)
```

## Analyze-Beispiele

```python
func.to_start_of_five_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_five_minutes('2023-11-12 09:38:18.165575')    │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:35:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_START_OF_FIVE_MINUTES(<expr>)
```

## Argumente

| Argumente | Beschreibung |
|-----------|-------------|
| `<expr>`  | Zeitstempel |

## Rückgabetyp

`TIMESTAMP`, gibt das Datum im Format „YYYY-MM-DD hh:mm:ss.ffffff“ zurück.

## SQL-Beispiele

```sql
SELECT
  to_start_of_five_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────┐
│ to_start_of_five_minutes('2023-11-12 09:38:18.165575') │
│                        Timestamp                       │
├────────────────────────────────────────────────────────┤
│ 2023-11-12 09:35:00                                    │
└────────────────────────────────────────────────────────┘
```
