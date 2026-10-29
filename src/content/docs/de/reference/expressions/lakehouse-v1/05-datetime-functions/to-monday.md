---
title: TO_MONDAY (Lakehouse v1)
description: TO_MONDAY – rundet ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) auf den nächstliegenden vorherigen Montag ab.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-monday.md
---

Rundet ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) auf den nächstliegenden vorherigen Montag ab.
Gibt das Datum zurück.

## Analyze-Syntax

```python
func.to_monday(<expr>)
```

## Analyze-Beispiele

```python
func.to_monday('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_monday('2023-11-12 09:38:18.165575')       │
│                      Date                          │
├────────────────────────────────────────────────────┤
│ 2023-11-06                                         │
└────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_MONDAY(<expr>)
```

## Argumente

| Argumente   | Beschreibung |
| ----------- | ----------- |
| `<expr>` | Datum/Zeitstempel |

## Rückgabetyp

`DATE`, gibt das Datum im Format „YYYY-MM-DD“ zurück.

## SQL-Beispiele

```sql
SELECT
    to_monday('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_monday('2023-11-12 09:38:18.165575') │
│                   Date                  │
├─────────────────────────────────────────┤
│ 2023-11-06                              │
└─────────────────────────────────────────┘
```
