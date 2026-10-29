---
title: TO_START_OF_SECOND (Lakehouse v1)
description: TO_START_OF_SECOND – rundet ein Datum mit Uhrzeit (Timestamp/Datetime) auf den Beginn der Sekunde ab.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-second.md
---

Rundet ein Datum mit Uhrzeit (Timestamp/Datetime) auf den Beginn der Sekunde ab.

## Analyze-Syntax

```python
func.to_start_of_second(<expr>)
```

## Analyze-Beispiele

```python
func.to_start_of_second('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_second('2023-11-12 09:38:18.165575')          │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:38:18                                            │
└────────────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_START_OF_SECOND(<expr>)
```

## Argumente

| Argumente | Beschreibung |
|-----------|-------------|
| `<expr>`  | Timestamp   |

## Rückgabetyp

`TIMESTAMP`, gibt das Datum im Format „YYYY-MM-DD hh:mm:ss.ffffff“ zurück.

## SQL-Beispiele

```sql
SELECT
  to_start_of_second('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ to_start_of_second('2023-11-12 09:38:18.165575') │
│                     Timestamp                    │
├──────────────────────────────────────────────────┤
│ 2023-11-12 09:38:18                              │
└──────────────────────────────────────────────────┘
```
