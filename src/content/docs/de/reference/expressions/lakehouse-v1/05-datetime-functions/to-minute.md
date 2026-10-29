---
title: TO_MINUTE (Lakehouse v1)
description: TO_MINUTE – wandelt ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt8-Zahl um, die die Minute der Stunde (0–59) enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-minute.md
---

Wandelt ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt8-Zahl um, die die Minute der Stunde (0–59) enthält.


## Analyze-Syntax

```python
func.to_minute(<expr>)
```

## Analyze-Beispiele

```python
func.to_minute('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_minute('2023-11-12 09:38:18.165575')       │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                 38 │
└────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_MINUTE(<expr>)
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
    to_minute('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_minute('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      38 │
└─────────────────────────────────────────┘
```
