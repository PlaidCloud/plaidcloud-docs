---
title: TO_YYYYMMDDHHMMSS (Lakehouse v1)
description: TO_YYYYMMDDHHMMSS – wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt64-Zahl um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhhmmss.md
---

Wandelt ein Datum oder ein Datum mit Uhrzeit (Timestamp/Datetime) in eine UInt64-Zahl um, die Jahr, Monat, Tag, Stunde, Minute und Sekunde enthält (YYYY * 10000000000 + MM * 100000000 + DD * 1000000 + hh * 10000 + mm * 100 + ss).

## Analyze-Syntax

```python
func.to_yyyymmddhhmmss(<expr>)
```

## Analyze-Beispiele

```python
func.to_yyyymmddhhmmss('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────────┐
│ func.to_yyyymmddhhmmss('2023-11-12 09:38:18.165575') │
│                   UInt64                             │
├──────────────────────────────────────────────────────┤
│                                       20231112092818 │
└──────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TO_YYYYMMDDHHMMSS(<expr>)
```

## Argumente

| Argumente | Beschreibung   |
|-----------|----------------|
| `<expr>`  | Datum/Timestamp |

## Rückgabetyp

`BIGINT`, gibt den Wert im Format `YYYYMMDDhhmmss` zurück.

## SQL-Beispiele

```sql
SELECT
  to_yyyymmddhhmmss('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_yyyymmddhhmmss('2023-11-12 09:38:18.165575') │
│                      UInt64                     │
├─────────────────────────────────────────────────┤
│                                  20231112092818 │
└─────────────────────────────────────────────────┘
```
