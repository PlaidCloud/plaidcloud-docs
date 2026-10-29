---
title: TO_YYYYMMDDHH (Lakehouse v1)
description: TO_YYYYMMDDHH – formatiert ein angegebenes Datum oder einen Timestamp als Zeichenfolge im Format YYYYMMDDHH.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhh.md
---

Formatiert ein angegebenes Datum oder einen Timestamp als Zeichenfolge im Format „YYYYMMDDHH“ (Jahr, Monat, Tag, Stunde).

## Analyze-Syntax

```python
func.to_yyyymmddhh(<expr>)
```

## Analyze-Beispiele

```python
func.to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ func.to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                   UInt32                         │
├──────────────────────────────────────────────────┤
│                                       2023111209 │
└──────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_YYYYMMDDHH(<expr>)
```

## Argumente

| Argumente | Beschreibung  |
|-----------|---------------|
| `<expr>`  | Datum/Datetime |

## Rückgabetyp

Gibt eine vorzeichenlose 64-Bit-Ganzzahl (UInt64) im Format „YYYYMMDDHH“ zurück.

## SQL-Beispiele

```sql
SELECT
  to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────┐
│ to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                    UInt32                   │
├─────────────────────────────────────────────┤
│                                  2023111209 │
└─────────────────────────────────────────────┘
```
