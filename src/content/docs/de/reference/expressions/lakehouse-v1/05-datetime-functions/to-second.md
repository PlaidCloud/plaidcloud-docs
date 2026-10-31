---
title: TO_SECOND (Lakehouse v1)
description: TO_SECOND – wandelt ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt8-Zahl um, die die Sekunde der Minute (0–59) enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-second.md
---

Wandelt ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt8-Zahl um, die die Sekunde der Minute (0–59) enthält.

## Analyze-Syntax

```python
func.to_second(<expr>)
```

## Analyze-Beispiele

```python
func.to_second('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_second('2023-11-12 09:38:18.165575') │
│                   UInt8                      │
├──────────────────────────────────────────────┤
│                                           18 │
└──────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_SECOND(<expr>)
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
    to_second('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_second('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      18 │
└─────────────────────────────────────────┘
```
